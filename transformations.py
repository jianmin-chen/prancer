from copy import copy
from math import cos, sin
from matrix import Matrix, identity_matrix
from tuple import Tuple, normalize, cross


def translation(x: float, y: float, z: float) -> Matrix:
    """
    Returns a translation matrix.

        Parameters:
            x (float)
            y (float)
            z (float)

        Returns:
            translation_matrix (Matrix)
    """

    translation_matrix = copy(identity_matrix)
    translation_matrix.set_cell(0, 3, x)
    translation_matrix.set_cell(1, 3, y)
    translation_matrix.set_cell(2, 3, z)
    return translation_matrix


def scaling(x: float, y: float, z: float) -> Matrix:
    """
    Returns a scaling matrix.

        Parameters:
            x (float)
            y (float)
            z (float)

        Returns:
            scaling_matrix (Matrix)
    """

    scaling_matrix = copy(identity_matrix)
    scaling_matrix.set_cell(0, 0, x)
    scaling_matrix.set_cell(1, 1, y)
    scaling_matrix.set_cell(2, 2, z)
    return scaling_matrix


def rotation_x(radians: float) -> Matrix:
    """
    Returns a matrix for rotating around X-axis.

        Parameters:
            radians (float)

        Returns:
            rotated_x (Matrix)
    """

    rotated_x = copy(identity_matrix)
    rotated_x.set_cell(1, 1, cos(radians))
    rotated_x.set_cell(1, 2, -sin(radians))
    rotated_x.set_cell(2, 1, sin(radians))
    rotated_x.set_cell(2, 2, cos(radians))
    return rotated_x


def rotation_y(radians: float) -> Matrix:
    """
    Returns a matrix for rotating around Y-axis.

        Parameters:
            radians (float)

        Returns:
            rotated_y (Matrix)
    """

    rotated_y = copy(identity_matrix)
    rotated_y.set_cell(0, 0, cos(radians))
    rotated_y.set_cell(0, 2, sin(radians))
    rotated_y.set_cell(2, 0, -sin(radians))
    rotated_y.set_cell(2, 2, cos(radians))
    return rotated_y


def rotation_z(radians: float) -> Matrix:
    """
    Returns a matrix for rotating around Z-axis.

        Parameters:
            radians (float)

        Returns:
            rotated_z (Matrix)
    """

    rotated_z = copy(identity_matrix)
    rotated_z.set_cell(0, 0, cos(radians))
    rotated_z.set_cell(0, 1, -sin(radians))
    rotated_z.set_cell(1, 0, sin(radians))
    rotated_z.set_cell(1, 1, cos(radians))
    return rotated_z


def shearing(
    xy: float, xz: float, yx: float, yz: float, zx: float, zy: float
) -> Matrix:
    """
    Returns a matrix for shearing.

        Parameters:
            xy (float): X moved in proportion to y.
            xz (float): X moved in proportion to z.
            yx (float): Y moved in proportion to x.
            yz (float): Y moved in proportion to z.
            zx (float): Z moved in proportion to x.
            zy (float): Z moved in proportion to y.

        Returns:
            sheared (Matrix)
    """

    sheared = copy(identity_matrix)
    sheared.set_cell(0, 1, xy)
    sheared.set_cell(0, 2, xz)
    sheared.set_cell(1, 0, yx)
    sheared.set_cell(1, 2, yz)
    sheared.set_cell(2, 0, zx)
    sheared.set_cell(2, 1, zy)
    return sheared


def view_transform(start: Tuple, to: Tuple, up: Tuple):
    forward = normalize(to - start)
    upn = normalize(up)
    left = cross(forward, upn)
    true_up = cross(left, forward)
    orientation = Matrix(
        4,
        4,
        [
            left.x,
            left.y,
            left.z,
            0,
            true_up.x,
            true_up.y,
            true_up.z,
            0,
            -forward.x,
            -forward.y,
            -forward.z,
            0,
            0,
            0,
            0,
            1,
        ],
    )
    return orientation * translation(-start.x, -start.y, -start.z)
