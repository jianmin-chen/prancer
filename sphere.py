from matrix import Matrix, identity_matrix
from tuple import Tuple, point


class Sphere:
    def __init__(self, origin: Tuple = point(0, 0, 0), radius: float = 1):
        self.origin = origin
        self.radius = radius
        self.transform = identity_matrix

    def set_transform(self, transformation: Matrix) -> None:
        """
        Set a sphere's transformation matrix to a given one.

            Parameters:
                transformation (Matrix)
        """

        self.transform = transformation

    def __repr__(self):
        return f"Sphere with origin at {self.origin} and radius {self.radius}"
