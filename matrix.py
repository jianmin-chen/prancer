from __future__ import annotations
from tuple import Tuple
from utils import equal


class Matrix:
    def __init__(self, rows: int, cols: int, matrix: list = []):
        self.rows = rows
        self.cols = cols
        self.matrix = (
            [0 for cell in range(self.rows * self.cols)] if len(matrix) == 0 else matrix
        )

    def set_cell(self, row, col, value):
        self.matrix[row * self.cols + col] = value

    def __copy__(self) -> Matrix:
        return Matrix(self.rows, self.cols, self.matrix.copy())

    def __mul__(self, other) -> Matrix:
        if isinstance(other, Matrix):
            # ! Only applied to 4x4 matrices in this raytracer
            matrix = []
            for row in range(self.rows):
                for col in range(self.cols):
                    matrix.append(
                        self[row][0] * other[0][col]
                        + self[row][1] * other[1][col]
                        + self[row][2] * other[2][col]
                        + self[row][3] * other[3][col]
                    )
            return Matrix(self.rows, self.cols, matrix)
        elif isinstance(other, Tuple):
            # Multiply by tuple
            t = []
            for row in range(self.rows):
                r = []
                for col in range(self.cols):
                    r.append(self[row][col] * other[col])
                t.append(sum(r))
            return Tuple(*t)

    def __eq__(self, other: Matrix) -> bool:
        if self.rows == other.rows and self.cols == other.cols:
            for cell in range(self.rows * self.cols):
                if not equal(self.matrix[cell], other.matrix[cell]):
                    return False
            return True
        return False

    def __getitem__(self, row):
        return self.matrix[row * self.cols : row * self.cols + self.cols]

    def __repr__(self):
        # TODO: Deal with padding
        rows = ["|".join([str(col) for col in self[row]]) for row in range(self.rows)]
        return "\n".join(rows)


def transpose(matrix: Matrix) -> Matrix:
    """
    Transpose (swap rows with columns) a matrix.

        Parameters:
            matrix (Matrix)

        Return:
            transposed (Matrix)
    """

    transposed = []
    for row in range(matrix.rows):
        for col in range(matrix.cols):
            transposed.append(matrix[col][row])
    return Matrix(matrix.rows, matrix.cols, transposed)


def determinant(matrix: Matrix) -> float:
    """
    Finds the determinant of a 2x2 matrix.

        Parameters:
            matrix (Matrix): 2x2 matrix

        Returns:
            determinant (float)
    """

    det = 0

    if matrix.rows == 2 and matrix.cols == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for col in range(matrix.cols):
            det = det + matrix[0][col] * cofactor(matrix, 0, col)

    return det


def submatrix(matrix: Matrix, row: int, col: int) -> Matrix:
    """
    Returns a submatrix by removing a singular row and column.

        Parameters:
            matrix (Matrix)
            row (int)
            col (int)

        Returns:
            submatrix (Matrix)
    """

    submatrix = []
    for r in range(matrix.rows):
        if r == row:
            continue
        for c in range(matrix.cols):
            if c == col:
                continue
            submatrix.append(matrix[r][c])
    return Matrix(matrix.rows - 1, matrix.cols - 1, submatrix)


def minor(matrix: Matrix, row: int, col: int) -> float:
    """
    Determinant of a submatrix of matrix.

        Parameters:
            matrix (Matrix)
            row (int)
            col (int)

        Returns:
            minor (float)
    """

    minor = determinant(submatrix(matrix, row, col))
    return minor


def cofactor(matrix: Matrix, row: int, col: int) -> float:
    """
    Returns cofactor of matrix.

        Parameters:
            matrix (Matrix)
            row (int)
            col (int)

        Returns:
            cofactor (float)
    """

    m = minor(matrix, row, col)
    if (row + col) % 2 != 0:
        return -m
    return m


def invertible(matrix: Matrix) -> bool:
    """
    Determines whether or not a matrix can be inverted.

        Parameters:
            matrix (Matrix)

        Returns:
            invertible (bool)
    """

    return False if determinant(matrix) == 0 else True


def inverse(matrix: Matrix) -> Matrix:
    """
    Finds the inverse of a given matrix.

        Parameters:
            matrix (Matrix)
    """

    if not invertible(matrix):
        raise ValueError("Matrix cannot be inverted")

    m2 = Matrix(matrix.rows, matrix.cols)

    for row in range(matrix.rows):
        for col in range(matrix.cols):
            c = cofactor(matrix, row, col)
            m2.set_cell(col, row, c / determinant(matrix))

    return m2


identity_matrix = Matrix(4, 4, [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1])
