from math import pi, sqrt
from matrix import inverse
from transformations import (
    scaling,
    translation,
    rotation_x,
    rotation_y,
    rotation_z,
    shearing,
)
from tuple import point, vector
import unittest


class Tests(unittest.TestCase):
    def test_scenario1(self):
        """
        Scenario: Multiplying by a translation matrix
          Given transform ← translation(5, -3, 2)
            And p ← point(-3, 4, 5)
           Then transform * p = point(2, 1, 7)
        """

        transform = translation(5, -3, 2)
        p = point(-3, 4, 5)
        self.assertEqual(transform * p, point(2, 1, 7))

    def test_scenario2(self):
        """
        Scenario: Multiplying by the inverse of a translation matrix
            Given transform ← translation(5, -3, 2)
            And inv ← inverse(transform)
            And p ← point(-3, 4, 5)
            Then inv * p = point(-8, 7, 3)
        """

        transform = translation(5, -3, 2)
        inv = inverse(transform)
        p = point(-3, 4, 5)
        self.assertEqual(inv * p, point(-8, 7, 3))

    def test_scenario3(self):
        """
        Scenario: Translation does not affect vectors
            Given transform ← translation(5, -3, 2)
            And v ← vector(-3, 4, 5)
            Then transform * v = v
        """

        transform = translation(5, -3, 2)
        v = vector(-3, 4, 5)
        self.assertEqual(transform * v, v)

    def test_scenario4(self):
        """
        Scenario: A scaling matrix applied to a point
            Given transform ← scaling(2, 3, 4)
            And p ← point(-4, 6, 8)
            Then transform * p = point(-8, 18, 32)
        """

        transform = scaling(2, 3, 4)
        p = point(-4, 6, 8)
        self.assertEqual(transform * p, point(-8, 18, 32))

    def test_scenario5(self):
        """
        Scenario: A scaling matrix applied to a vector
            Given transform ← scaling(2, 3, 4)
            And v ← vector(-4, 6, 8)
            Then transform * v = vector(-8, 18, 32)
        """

        transform = scaling(2, 3, 4)
        v = vector(-4, 6, 8)
        self.assertEqual(transform * v, vector(-8, 18, 32))

    def test_scenario6(self):
        """
        Scenario: Multiplying by the inverse of a scaling matrix
            Given transform ← scaling(2, 3, 4)
            And inv ← inverse(transform)
            And v ← vector(-4, 6, 8)
            Then inv * v = vector(-2, 2, 2)
        """

        transform = scaling(2, 3, 4)
        inv = inverse(transform)
        v = vector(-4, 6, 8)
        self.assertEqual(inv * v, vector(-2, 2, 2))

    def test_scenario7(self):
        """
        Scenario: Reflection is scaling by a negative value
            Given transform ← scaling(-1, 1, 1)
            And p ← point(2, 3, 4)
            Then transform * p = point(-2, 3, 4)
        """

        transform = scaling(-1, 1, 1)
        p = point(2, 3, 4)
        self.assertEqual(transform * p, point(-2, 3, 4))

    def test_scenario8(self):
        """
        Scenario: Rotating a point around the x axis
            Given p ← point(0, 1, 0)
            And half_quarter ← rotation_x(π / 4)
            And full_quarter ← rotation_x(π / 2)
            Then half_quarter * p = point(0, √2/2, √2/2)
            And full_quarter * p = point(0, 0, 1)
        """

        p = point(0, 1, 0)
        half_quarter = rotation_x(pi / 4)
        full_quarter = rotation_x(pi / 2)
        self.assertEqual(half_quarter * p, point(0, sqrt(2) / 2, sqrt(2) / 2))
        self.assertEqual(full_quarter * p, point(0, 0, 1))

    def test_scenario9(self):
        """
        Scenario: The inverse of an x-rotation rotates in the opposite direction
            Given p ← point(0, 1, 0)
            And half_quarter ← rotation_x(π / 4)
            And inv ← inverse(half_quarter)
            Then inv * p = point(0, √2/2, -√2/2)
        """

        p = point(0, 1, 0)
        half_quarter = rotation_x(pi / 4)
        inv = inverse(half_quarter)
        self.assertEqual(inv * p, point(0, sqrt(2) / 2, -(sqrt(2) / 2)))

    def test_scenario10(self):
        """
        Scenario: Rotating a point around the y axis
            Given p ← point(0, 0, 1)
            And half_quarter ← rotation_y(π / 4)
            And full_quarter ← rotation_y(π / 2)
            Then half_quarter * p = point(√2/2, 0, √2/2)
            And full_quarter * p = point(1, 0, 0)
        """

        p = point(0, 0, 1)
        half_quarter = rotation_y(pi / 4)
        full_quarter = rotation_y(pi / 2)
        self.assertEqual(half_quarter * p, point(sqrt(2) / 2, 0, sqrt(2) / 2))
        self.assertEqual(full_quarter * p, point(1, 0, 0))

    def test_scenario11(self):
        """
        Scenario: Rotating a point around the z axis
            Given p ← point(0, 1, 0)
            And half_quarter ← rotation_z(π / 4)
            And full_quarter ← rotation_z(π / 2)
            Then half_quarter * p = point(-√2/2, √2/2, 0)
            And full_quarter * p = point(-1, 0, 0)
        """

        p = point(0, 1, 0)
        half_quarter = rotation_z(pi / 4)
        full_quarter = rotation_z(pi / 2)
        self.assertEqual(half_quarter * p, point(-(sqrt(2) / 2), sqrt(2) / 2, 0))
        self.assertEqual(full_quarter * p, point(-1, 0, 0))

    def test_scenario12(self):
        """
        Scenario: A shearing transformation moves x in proportion to y
            Given transform ← shearing(1, 0, 0, 0, 0, 0)
            And p ← point(2, 3, 4)
            Then transform * p = point(5, 3, 4)
        """

        transform = shearing(1, 0, 0, 0, 0, 0)
        p = point(2, 3, 4)
        self.assertEqual(transform * p, point(5, 3, 4))

    def test_scenario13(self):
        """
        Scenario: A shearing transformation moves x in proportion to z
            Given transform ← shearing(0, 1, 0, 0, 0, 0)
            And p ← point(2, 3, 4)
            Then transform * p = point(6, 3, 4)
        """

        transform = shearing(0, 1, 0, 0, 0, 0)
        p = point(2, 3, 4)
        self.assertEqual(transform * p, point(6, 3, 4))

    def test_scenario14(self):
        """
        Scenario: A shearing transformation moves y in proportion to x
            Given transform ← shearing(0, 0, 1, 0, 0, 0)
            And p ← point(2, 3, 4)
            Then transform * p = point(2, 5, 4)
        """

        transform = shearing(0, 0, 1, 0, 0, 0)
        p = point(2, 3, 4)
        self.assertEqual(transform * p, point(2, 5, 4))

    def test_scenario15(self):
        """
        Scenario: A shearing transformation moves y in proportion to z
            Given transform ← shearing(0, 0, 0, 1, 0, 0)
            And p ← point(2, 3, 4)
            Then transform * p = point(2, 7, 4)
        """

        transform = shearing(0, 0, 0, 1, 0, 0)
        p = point(2, 3, 4)
        self.assertEqual(transform * p, point(2, 7, 4))

    def test_scenario16(self):
        """
        Scenario: A shearing transformation moves z in proportion to x
            Given transform ← shearing(0, 0, 0, 0, 1, 0)
            And p ← point(2, 3, 4)
            Then transform * p = point(2, 3, 6)
        """

        transform = shearing(0, 0, 0, 0, 1, 0)
        p = point(2, 3, 4)
        self.assertEqual(transform * p, point(2, 3, 6))

    def test_scenario17(self):
        """
        Scenario: A shearing transformation moves z in proportion to y
            Given transform ← shearing(0, 0, 0, 0, 0, 1)
            And p ← point(2, 3, 4)
            Then transform * p = point(2, 3, 7)
        """

        transform = shearing(0, 0, 0, 0, 0, 1)
        p = point(2, 3, 4)
        self.assertEqual(transform * p, point(2, 3, 7))

    def test_scenario18(self):
        """
        Scenario: Individual transformations are applied in sequence
            Given p ← point(1, 0, 1)
            And A ← rotation_x(π / 2)
            And B ← scaling(5, 5, 5)
            And C ← translation(10, 5, 7)
            # apply rotation first
            When p2 ← A * p
            Then p2 = point(1, -1, 0)
            # then apply scaling
            When p3 ← B * p2
            Then p3 = point(5, -5, 0)
            # then apply translation
            When p4 ← C * p3
            Then p4 = point(15, 0, 7)
        """

        p = point(1, 0, 1)
        A = rotation_x(pi / 2)
        B = scaling(5, 5, 5)
        C = translation(10, 5, 7)
        p2 = A * p
        self.assertEqual(p2, point(1, -1, 0))
        p3 = B * p2
        self.assertEqual(p3, point(5, -5, 0))
        p4 = C * p3
        self.assertEqual(p4, point(15, 0, 7))

    def test_scenario19(self):
        """
        Scenario: Chained transformations must be applied in reverse order
            Given p ← point(1, 0, 1)
            And A ← rotation_x(π / 2)
            And B ← scaling(5, 5, 5)
            And C ← translation(10, 5, 7)
            When T ← C * B * A
            Then T * p = point(15, 0, 7)
        """

        p = point(1, 0, 1)
        A = rotation_x(pi / 2)
        B = scaling(5, 5, 5)
        C = translation(10, 5, 7)
        T = C * B * A
        self.assertEqual(T * p, point(15, 0, 7))


if __name__ == "__main__":
    unittest.main()
