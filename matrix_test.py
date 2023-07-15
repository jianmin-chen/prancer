from matrix import (
    Matrix,
    identity_matrix,
    transpose,
    determinant,
    submatrix,
    minor,
    cofactor,
    invertible,
    inverse,
)
from tuple import Tuple
from utils import equal
import unittest


def to_array(s):
    array = [
        float(i)
        for i in filter(lambda c: c.strip() not in ["\n", "", ","], s.split("|"))
    ]
    return array


class Tests(unittest.TestCase):
    def test_scenario1(self):
        """
        Scenario: Constructing and inspecting a 4x4 matrix
            Given the following 4x4 matrix M:
              | 1    | 2    | 3    | 4    |
              | 5.5  | 6.5  | 7.5  | 8.5  |
              | 9    | 10   | 11   | 12   |
              | 13.5 | 14.5 | 15.5 | 16.5 |
            Then M[0,0] = 1
            And M[0,3] = 4
            And M[1,0] = 5.5
            And M[1,2] = 7.5
            And M[2,2] = 11
            And M[3,0] = 13.5
            And M[3,2] = 15.5
        """

        M = Matrix(
            4,
            4,
            [1, 2, 3, 4, 5.5, 6.5, 7.5, 8.5, 9, 10, 11, 12, 13.5, 14.5, 15.5, 16.5],
        )
        self.assertEqual(M[0][0], 1)
        self.assertEqual(M[0][3], 4)
        self.assertEqual(M[1][0], 5.5)
        self.assertEqual(M[1][2], 7.5)
        self.assertEqual(M[2][2], 11)
        self.assertEqual(M[3][0], 13.5)
        self.assertEqual(M[3][2], 15.5)

    def test_scenario2(self):
        """
        Scenario: A 2x2 matrix ought to be representable
            Given the following 2x2 matrix M:
              | -3 | 5  |
              | 1  | -2 |
            Then M[0,0] = -3
            And M[0,1] = 5
            And M[1,0] = 1
            And M[1,1] = -2
        """

        M = Matrix(2, 2, [-3, 5, 1, -2])
        self.assertEqual(M[0][0], -3)
        self.assertEqual(M[0][1], 5)
        self.assertEqual(M[1][0], 1)
        self.assertEqual(M[1][1], -2)

    def test_scenario3(self):
        """
        Scenario: A 3x3 matrix ought to be representable
            Given the following 3x3 matrix M:
              | -3 | 5  | 0  |
              | 1  | -2 | -7 |
              | 0  | 1  | 1  |
            Then M[0,0] = -3
            And M[1,1] = -2
            And M[2,2] = 1
        """

        M = Matrix(3, 3, [-3, 5, 0, 1, -2, -7, 0, 1, 1])
        self.assertEqual(M[0][0], -3)
        self.assertEqual(M[1][1], -2)
        self.assertEqual(M[2][2], 1)

    def test_scenario4(self):
        """
        Scenario: Matrix equality with identical matrices
            Given the following matrix A:
              | 1 | 2 | 3 | 4 |
              | 5 | 6 | 7 | 8 |
              | 9 | 8 | 7 | 6 |
              | 5 | 4 | 3 | 2 |
            And the following matrix B:
              | 1 | 2 | 3 | 4 |
              | 5 | 6 | 7 | 8 |
              | 9 | 8 | 7 | 6 |
              | 5 | 4 | 3 | 2 |
            Then A = B
        """

        A = Matrix(4, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2])
        B = Matrix(4, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2])
        self.assertTrue(A == B)

    def test_scenario5(self):
        """
        Scenario: Matrix equality with different matrices
            Given the following matrix A:
              | 1 | 2 | 3 | 4 |
              | 5 | 6 | 7 | 8 |
              | 9 | 8 | 7 | 6 |
              | 5 | 4 | 3 | 2 |
            And the following matrix B:
              | 2 | 3 | 4 | 5 |
              | 6 | 7 | 8 | 9 |
              | 8 | 7 | 6 | 5 |
              | 4 | 3 | 2 | 1 |
            Then A != B
        """

        A = Matrix(4, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2])
        B = Matrix(4, 4, [2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertFalse(A == B)

    def test_scenario6(self):
        """
        Scenario: Multiplying two matrices
            Given the following matrix A:
              | 1 | 2 | 3 | 4 |
              | 5 | 6 | 7 | 8 |
              | 9 | 8 | 7 | 6 |
              | 5 | 4 | 3 | 2 |
            And the following matrix B:
              | -2 | 1 | 2 | 3  |
              | 3  | 2 | 1 | -1 |
              | 4  | 3 | 6 | 5  |
              | 1  | 2 | 7 | 8  |
            Then A * B is the following 4x4 matrix:
              | 20 | 22 | 50  | 48  |
              | 44 | 54 | 114 | 108 |
              | 40 | 58 | 110 | 102 |
              | 16 | 26 | 46  | 42  |
        """

        A = Matrix(4, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2])
        B = Matrix(4, 4, [-2, 1, 2, 3, 3, 2, 1, -1, 4, 3, 6, 5, 1, 2, 7, 8])
        self.assertEqual(
            A * B,
            Matrix(
                4,
                4,
                [20, 22, 50, 48, 44, 54, 114, 108, 40, 58, 110, 102, 16, 26, 46, 42],
            ),
        )

    def test_scenario7(self):
        """
        Scenario: A matrix multiplied by a tuple
            Given the following matrix A:
              | 1 | 2 | 3 | 4 |
              | 2 | 4 | 4 | 2 |
              | 8 | 6 | 4 | 1 |
              | 0 | 0 | 0 | 1 |
            And b ← tuple(1, 2, 3, 1)
            Then A * b = tuple(18, 24, 33, 1)
        """

        A = Matrix(4, 4, [1, 2, 3, 4, 2, 4, 4, 2, 8, 6, 4, 1, 0, 0, 0, 1])
        b = Tuple(1, 2, 3, 1)
        self.assertEqual(A * b, Tuple(18, 24, 33, 1))

    def test_scenario8(self):
        """
        Scenario: Multiplying a matrix by the identity matrix
            Given the following matrix A:
              | 0 | 1 | 2  | 4  |
              | 1 | 2 | 4  | 8  |
              | 2 | 4 | 8  | 16 |
              | 4 | 8 | 16 | 32 |
            Then A * identity_matrix = A
        """

        A = Matrix(4, 4, [0, 1, 2, 4, 1, 2, 4, 8, 2, 4, 8, 16, 4, 8, 16, 32])
        self.assertEqual(A * identity_matrix, A)

    def test_scenario9(self):
        """
        Scenario: Multiplying the identity matrix by a tuple
            Given a ← tuple(1, 2, 3, 4)
            Then identity_matrix * a = a
        """

        a = Tuple(1, 2, 3, 4)
        self.assertEqual(identity_matrix * a, a)

    def test_scenario10(self):
        """
        Scenario: Transposing a matrix
            Given the following matrix A:
              | 0 | 9 | 3 | 0 |
              | 9 | 8 | 0 | 8 |
              | 1 | 8 | 5 | 3 |
              | 0 | 0 | 5 | 8 |
            Then transpose(A) is the following matrix:
              | 0 | 9 | 1 | 0 |
              | 9 | 8 | 8 | 0 |
              | 3 | 0 | 5 | 5 |
              | 0 | 8 | 3 | 8 |
        """

        A = Matrix(4, 4, [0, 9, 3, 0, 9, 8, 0, 8, 1, 8, 5, 3, 0, 0, 5, 8])
        self.assertEqual(
            transpose(A), Matrix(4, 4, [0, 9, 1, 0, 9, 8, 8, 0, 3, 0, 5, 5, 0, 8, 3, 8])
        )

    def test_scenario11(self):
        """
        Scenario: Transposing the identity matrix
            Given A ← transpose(identity_matrix)
            Then A = identity_matrix
        """

        A = transpose(identity_matrix)
        self.assertEqual(A, identity_matrix)

    def test_scenario12(self):
        """
        Scenario: Calculating the determinant of a 2x2 matrix
            Given the following 2x2 matrix A:
              | 1  | 5 |
              | -3 | 2 |
            Then determinant(A) = 17
        """

        A = Matrix(2, 2, [1, 5, -3, 2])
        self.assertEqual(determinant(A), 17)

    def test_scenario13(self):
        """
        Scenario: A submatrix of a 3x3 matrix is a 2x2 matrix
            Given the following 3x3 matrix A:
              | 1  | 5 | 0  |
              | -3 | 2 | 7  |
              | 0  | 6 | -3 |
            Then submatrix(A, 0, 2) is the following 2x2 matrix:
              | -3 | 2 |
              | 0  | 6 |
        """

        A = Matrix(3, 3, [1, 5, 0, -3, 2, 7, 0, 6, -3])
        self.assertEqual(submatrix(A, 0, 2), Matrix(2, 2, [-3, 2, 0, 6]))

    def test_scenario14(self):
        """
        Scenario: A submatrix of a 4x4 matrix is a 3x3 matrix
            Given the following 4x4 matrix A:
              | -6 | 1 | 1  | 6 |
              | -8 | 5 | 8  | 6 |
              | -1 | 0 | 8  | 2 |
              | -7 | 1 | -1 | 1 |
            Then submatrix(A, 2, 1) is the following 3x3 matrix:
              | -6 | 1  | 6 |
              | -8 | 8  | 6 |
              | -7 | -1 | 1 |
        """

        A = Matrix(4, 4, [-6, 1, 1, 6, -8, 5, 8, 6, -1, 0, 8, 2, -7, 1, -1, 1])
        self.assertEqual(
            submatrix(A, 2, 1), Matrix(3, 3, [-6, 1, 6, -8, 8, 6, -7, -1, 1])
        )

    def test_scenario15(self):
        """
        Scenario: Calculating a minor of a 3x3 matrix
          Given the following 3x3 matrix A:
            | 3 | 5  | 0  |
            | 2 | -1 | -7 |
            | 6 | -1 | 5  |
          And B ← submatrix(A, 1, 0)
          Then determinant(B) = 25
          And minor(A, 1, 0) = 25
        """

        A = Matrix(3, 3, [3, 5, 0, 2, -1, -7, 6, -1, 5])
        B = submatrix(A, 1, 0)
        self.assertEqual(determinant(B), 25)
        self.assertEqual(minor(A, 1, 0), 25)

    def test_scenario16(self):
        """
        Scenario: Calculating a cofactor of a 3x3 matrix
            Given the following 3x3 matrix A:
              | 3 | 5  | 0  |
              | 2 | -1 | -7 |
              | 6 | -1 | 5  |
            Then minor(A, 0, 0) = -12
            And cofactor(A, 0, 0) = -12
            And minor(A, 1, 0) = 25
            And cofactor(A, 1, 0) = -25
        """

        A = Matrix(3, 3, [3, 5, 0, 2, -1, -7, 6, -1, 5])
        self.assertEqual(minor(A, 0, 0), -12)
        self.assertEqual(cofactor(A, 0, 0), -12)
        self.assertEqual(minor(A, 1, 0), 25)
        self.assertEqual(cofactor(A, 1, 0), -25)

    def test_scenario17(self):
        """
        Scenario: Calculating the determinant of a 3x3 matrix
            Given the following 3x3 matrix A:
              | 1  | 2 | 6  |
              | -5 | 8 | -4 |
              | 2  | 6 | 4  |
            Then cofactor(A, 0, 0) = 56
            And cofactor(A, 0, 1) = 12
            And cofactor(A, 0, 2) = -46
            And determinant(A) = -196
        """

        A = Matrix(3, 3, [1, 2, 6, -5, 8, -4, 2, 6, 4])
        self.assertEqual(cofactor(A, 0, 0), 56)
        self.assertEqual(cofactor(A, 0, 1), 12)
        self.assertEqual(cofactor(A, 0, 2), -46)
        self.assertEqual(determinant(A), -196)

    def test_scenario18(self):
        """
        Scenario: Calculating the determinant of a 4x4 matrix
            Given the following 4x4 matrix A:
              | -2 | -8 | 3  | 5  |
              | -3 | 1  | 7  | 3  |
              | 1  | 2  | -9 | 6  |
              | -6 | 7  | 7  | -9 |
            Then cofactor(A, 0, 0) = 690
            And cofactor(A, 0, 1) = 447
            And cofactor(A, 0, 2) = 210
            And cofactor(A, 0, 3) = 51
            And determinant(A) = -4071
        """

        A = Matrix(4, 4, [-2, -8, 3, 5, -3, 1, 7, 3, 1, 2, -9, 6, -6, 7, 7, -9])
        self.assertEqual(cofactor(A, 0, 0), 690)
        self.assertEqual(cofactor(A, 0, 1), 447)
        self.assertEqual(cofactor(A, 0, 2), 210)
        self.assertEqual(cofactor(A, 0, 3), 51)
        self.assertEqual(determinant(A), -4071)

    def test_scenario19(self):
        """
        Scenario: Testing an invertible matrix for invertibility
            Given the following 4x4 matrix A:
              | 6 | 4  | 4 | 4  |
              | 5 | 5  | 7 | 6  |
              | 4 | -9 | 3 | -7 |
              | 9 | 1  | 7 | -6 |
            Then determinant(A) = -2120
            And A is invertible
        """

        A = Matrix(4, 4, [6, 4, 4, 4, 5, 5, 7, 6, 4, -9, 3, -7, 9, 1, 7, -6])
        self.assertEqual(determinant(A), -2120)
        self.assertTrue(invertible(A))

    def test_scenario20(self):
        """
        Scenario: Testing a noninvertible matrix for invertibility
            Given the following 4x4 matrix A:
              | -4 | 2  | -2 | -3 |
              | 9  | 6  | 2  | 6  |
              | 0  | -5 | 1  | -5 |
              | 0  | 0  | 0  | 0  |
            Then determinant(A) = 0
            And A is not invertible
        """

        A = Matrix(4, 4, [-4, 2, -2, -3, 9, 6, 2, 6, 0, -5, 1, -5, 0, 0, 0, 0])
        self.assertEqual(determinant(A), 0)
        self.assertFalse(invertible(A))

    def test_scenario21(self):
        """
        Scenario: Calculating the inverse of a matrix
            Given the following 4x4 matrix A:
              | -5 | 2  | 6  | -8 |
              | 1  | -5 | 1  | 8  |
              | 7  | 7  | -6 | -7 |
              | 1  | -3 | 7  | 4  |
            And B ← inverse(A)
            Then determinant(A) = 532
            And cofactor(A, 2, 3) = -160
            And B[3,2] = -160/532
            And cofactor(A, 3, 2) = 105
            And B[2,3] = 105/532
            And B is the following 4x4 matrix:
              | 0.21805  | 0.45113  | 0.24060  | -0.04511 |
              | -0.80827 | -1.45677 | -0.44361 | 0.52068  |
              | -0.07895 | -0.22368 | -0.05263 | 0.19737  |
              | -0.52256 | -0.81391 | -0.30075 | 0.30639  |
        """

        A = Matrix(4, 4, [-5, 2, 6, -8, 1, -5, 1, 8, 7, 7, -6, -7, 1, -3, 7, 4])
        B = inverse(A)
        self.assertEqual(determinant(A), 532)
        self.assertEqual(cofactor(A, 2, 3), -160)
        self.assertTrue(equal(B[3][2], -160 / 532))
        self.assertEqual(cofactor(A, 3, 2), 105)
        self.assertEqual(B[2][3], 105 / 532)
        self.assertTrue(
            B
            == Matrix(
                4,
                4,
                to_array(
                    """| 0.21805  | 0.45113  | 0.24060  | -0.04511 |
              | -0.80827 | -1.45677 | -0.44361 | 0.52068  |
              | -0.07895 | -0.22368 | -0.05263 | 0.19737  |
              | -0.52256 | -0.81391 | -0.30075 | 0.30639  |"""
                ),
            )
        )

    def test_scenario22(self):
        """
        Scenario: Calculating the inverse of another matrix
            Given the following 4x4 matrix A:
              | 8  | -5 | 9  | 2  |
              | 7  | 5  | 6  | 1  |
              | -6 | 0  | 9  | 6  |
              | -3 | 0  | -9 | -4 |
            Then inverse(A) is the following 4x4 matrix:
              | -0.15385 | -0.15385 | -0.28205 | -0.53846 |
              | -0.07692 | 0.12308  | 0.02564  | 0.03077  |
              | 0.35897  | 0.35897  | 0.43590  | 0.92308  |
              | -0.69231 | -0.69231 | -0.76923 | -1.92308 |
        """

        A = Matrix(4, 4, [8, -5, 9, 2, 7, 5, 6, 1, -6, 0, 9, 6, -3, 0, -9, -4])
        self.assertTrue(
            inverse(A)
            == Matrix(
                4,
                4,
                to_array(
                    """| -0.15385 | -0.15385 | -0.28205 | -0.53846 |
              | -0.07692 | 0.12308  | 0.02564  | 0.03077  |
              | 0.35897  | 0.35897  | 0.43590  | 0.92308  |
              | -0.69231 | -0.69231 | -0.76923 | -1.92308 |"""
                ),
            ),
        )

    def test_scenario23(self):
        """
        Scenario: Calculating the inverse of a third matrix
            Given the following 4x4 matrix A:
              | 9  | 3  | 0  | 9  |
              | -5 | -2 | -6 | -3 |
              | -4 | 9  | 6  | 4  |
              | -7 | 6  | 6  | 2  |
            Then inverse(A) is the following 4x4 matrix:
              | -0.04074 | -0.07778 | 0.14444  | -0.22222 |
              | -0.07778 | 0.03333  | 0.36667  | -0.33333 |
              | -0.02901 | -0.14630 | -0.10926 | 0.12963  |
              | 0.17778  | 0.06667  | -0.26667 | 0.33333  |
        """

        A = Matrix(4, 4, [9, 3, 0, 9, -5, -2, -6, -3, -4, 9, 6, 4, -7, 6, 6, 2])
        self.assertTrue(
            inverse(A)
            == Matrix(
                4,
                4,
                to_array(
                    """| -0.04074 | -0.07778 | 0.14444  | -0.22222 |
              | -0.07778 | 0.03333  | 0.36667  | -0.33333 |
              | -0.02901 | -0.14630 | -0.10926 | 0.12963  |
              | 0.17778  | 0.06667  | -0.26667 | 0.33333  |"""
                ),
            )
        )

    def test_scenario24(self):
        """
        Scenario: Multiplying a product by its inverse
            Given the following 4x4 matrix A:
              | 3  | -9 | 7  | 3  |
              | 3  | -8 | 2  | -9 |
              | -4 | 4  | 4  | 1  |
              | -6 | 5  | -1 | 1  |
            And the following 4x4 matrix B:
              | 8 | 2  | 2 | 2 |
              | 3 | -1 | 7 | 0 |
              | 7 | 0  | 5 | 4 |
              | 6 | -2 | 0 | 5 |
            And C ← A * B
            Then C * inverse(B) = A
        """

        A = Matrix(4, 4, [3, -9, 7, 3, 3, -8, 2, -9, -4, 4, 4, 1, -6, 5, -1, 1])
        B = Matrix(4, 4, [8, 2, 2, 2, 3, -1, 7, 0, 7, 0, 5, 4, 6, -2, 0, 5])
        C = A * B
        self.assertEqual(C * inverse(B), A)


if __name__ == "__main__":
    unittest.main()
