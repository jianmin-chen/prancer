from material import Material
from matrix import Matrix, identity_matrix, inverse, transpose
from tuple import Tuple, point, normalize


class Sphere:
    def __init__(
        self,
        origin: Tuple = point(0, 0, 0),
        radius: float = 1,
        material: Material = Material(),
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

    def __repr__(self):
        return f"Sphere with origin at {self.origin} and radius {self.radius}"
