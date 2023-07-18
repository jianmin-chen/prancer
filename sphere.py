from __future__ import annotations
from copy import copy
from canvas import Color
from material import Material
from matrix import Matrix, identity_matrix, inverse, transpose
from tuple import Tuple, point, normalize


class Sphere(object):
    def __init__(
        self,
        origin: Tuple = point(0, 0, 0),
        radius: float = 1,
        material: Material = Material(Color(1, 1, 1), 0.1, 0.9, 0.9, 200),
    ):
        self.origin = origin
        self.radius = radius
        self.transform = identity_matrix
        self.material = material

    def set_transform(self, transformation: Matrix) -> None:
        """
        Set a sphere's transformation matrix to a given one.

            Parameters:
                transformation (Matrix)
        """

        self.transform = transformation

    def normal_at(self, p: Tuple) -> Tuple:
        """
        Computes the normal at a given point on a sphere.

            Parameters:
                p (Tuple)

            Returns:
                normal (Tuple)
        """

        object_point = inverse(self.transform) * p
        object_normal = object_point - point(0, 0, 0)
        world_normal = transpose(inverse(self.transform)) * object_normal
        world_normal.w = 0
        normal = normalize(world_normal)
        return normal

    def __copy__(self) -> Sphere:
        s = Sphere(copy(self.origin), self.radius, copy(self.material))
        s.transform = copy(self.transform)
        return s

    def __eq__(self, other: Sphere) -> bool:
        return (
            self.origin == other.origin
            and self.radius == other.radius
            and self.transform == other.transform
            and self.material == other.material
        )

    def __repr__(self):
        return f"Sphere with origin at {self.origin} and radius {self.radius}"
