from __future__ import annotations
import math


class Tuple:
    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.type = "point" if w == 1 else "vector"

    def __eq__(self, other: Tuple) -> bool:
        return (
            other.x == self.x
            and other.y == self.y
            and other.z == self.z
            and other.type == self.type
        )

    def __add__(self, other: Tuple) -> Tuple:
        return Tuple(
            self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w
        )

    def __sub__(self, other: Tuple) -> Tuple:
        return Tuple(
            self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w
        )

    def __mul__(self, other) -> Tuple:
        return Tuple(self.x * other, self.y * other, self.z * other, self.w * other)

    def __truediv__(self, other) -> Tuple:
        return Tuple(self.x / other, self.y / other, self.z / other, self.w / other)

    def __neg__(self) -> Tuple:
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


def point(x: float, y: float, z: float) -> Tuple:
    """
    Returns Tuple with type=point.

        Parameters:
            x (float)
            y (float)
            z (float)

        Returns:
            p (Tuple)
    """

    p = Tuple(x, y, z, 1)
    return p


def vector(x: float, y: float, z: float) -> Tuple:
    """
    Returns Tuple with type=vector.

        Parameters:
            x (float)
            y (float)
            z (float)

        Returns:
            p (Tuple)
    """

    p = Tuple(x, y, z, 0)
    return p


def normalize(v: Tuple) -> Tuple:
    """
    Normalizes a vector.

        Parameters:
            v (Tuple): With type=vector.

        Returns:
            normalized (Tuple)
    """

    m = magnitude(v)
    normalized = Tuple(v.x / m, v.y / m, v.z / m, v.w / m)
    return normalized


def magnitude(v: Tuple) -> float:
    """
    Returns the magnitude of a vector.

        Parameters:
            v (Tuple): With type=vector.

        Returns:
            magnitude (float)
    """

    magnitude = math.sqrt(v.x**2 + v.y**2 + v.z**2 + v.w**2)
    return magnitude


def dot(a: Tuple, b: Tuple) -> float:
    """
    Returns the dot product of two vectors.

        Parameters:
            a (Tuple)
            b (Tuple)

        Returns:
            product (float)
    """

    product = a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w
    return product


def cross(a: Tuple, b: Tuple) -> float:
    """
    Returns the cross product of two vectors.

        Parameters:
            a (Tuple)
            b (Tuple)

        Returns:
            product (Tuple)
    """

    product = vector(
        a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x
    )
    return product
