from __future__ import annotations
from utils import equal
import math


class Tuple:
    def __init__(self, x: float, y: float, z: float, w: float = 1) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.type = "point" if w == 1 else "vector"

    def __getitem__(self, index):
        indexed = [self.x, self.y, self.z, self.w]
        return indexed[index]

    def __eq__(self, other: Tuple) -> bool:
        return (
            equal(self.x, other.x)
            and equal(self.y, other.y)
            and equal(self.z, other.z)
            and equal(self.w, other.w)
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


class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __eq__(self, other: Color) -> bool:
        return (
            equal(self.red, other.red)
            and equal(self.green, other.green)
            and equal(self.blue, other.blue)
        )

    def __add__(self, other: Color) -> Color:
        return Color(
            self.red + other.red, self.green + other.green, self.blue + other.blue
        )

    def __sub__(self, other: Color) -> Color:
        return Color(
            self.red - other.red, self.green - other.green, self.blue - other.blue
        )

    def __mul__(self, other) -> Color:
        if isinstance(other, Color):
            # Multiplying two colors
            return Color(
                self.red * other.red, self.green * other.green, self.blue * other.blue
            )
        return Color(self.red * other, self.green * other, self.blue * other)

    def __repr__(self) -> str:
        return f"({self.red}, {self.green}, {self.blue})"


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


def reflect(initial: Tuple, normal: Tuple) -> Tuple:
    """
    Reflects a vector.

        Parameters:
            initial (Tuple)
            normal (Tuple)

        Returns:
            reflected (Tuple)
    """

    reflected = initial - normal * 2 * dot(initial, normal)
    return reflected
