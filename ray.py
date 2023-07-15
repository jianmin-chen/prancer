from copy import copy
from math import sqrt
from matrix import Matrix, inverse
from sphere import Sphere
from tuple import Tuple, point, dot


class Intersection:
    def __init__(self, t: float, object):
        self.t = t
        self.object = object

    def __repr__(self):
        return f"{self.object} at {self.t}"


class Intersections:
    def __init__(self, *intersections: Intersection):
        self.intersections = intersections or []

    @property
    def count(self):
        return len(self.intersections)

    def __getitem__(self, index: int) -> float:
        return self.intersections[index]

    def __repr__(self) -> str:
        pass


def hit(intersections: Intersections) -> Intersection:
    """
    Identify which intersection is actually visible from a ray's origin.

        Parameters:
            intersections (Intersections)

        Returns:
            visible (Intersection)
    """

    filtered = list(
        filter(lambda intersection: intersection.t >= 0, intersections.intersections)
    )
    visible = None
    for intersection in filtered:
        if visible is not None:
            if visible.t > intersection.t:
                visible = intersection
        else:
            visible = intersection
    return visible


class Ray:
    def __init__(self, origin: Tuple, direction: Tuple):
        self.origin = origin
        self.direction = direction

    def position(self, t: float) -> Tuple:
        """
        Finds the point at a given distance along ray.

            Parameters:
                t (float): time

            Returns:
                point (Tuple)
        """

        point = self.origin + self.direction * t
        return point

    def intersect(self, obj) -> Intersection:
        """
        Determine where ray intersects object.

            Parameters:
                obj (Any)

            Returns:
                intersection (Intersection)
        """

        if isinstance(obj, Sphere):
            # Calculate intersection with sphere
            ray2 = transform(self, inverse(obj.transform))
            sphere_to_ray = ray2.origin - point(0, 0, 0)
            a = dot(ray2.direction, ray2.direction)
            b = 2 * dot(ray2.direction, sphere_to_ray)
            c = dot(sphere_to_ray, sphere_to_ray) - 1

            discriminant = b**2 - 4 * a * c

            if discriminant < 0:
                return Intersections()

            t1 = (-b - sqrt(discriminant)) / (2 * a)
            t2 = (-b + sqrt(discriminant)) / (2 * a)
            return Intersections(Intersection(t1, obj), Intersection(t2, obj))

    def __copy__(self):
        return Ray(self.origin, self.direction)


def transform(ray: Ray, transformation: Matrix) -> Ray:
    """
    Apply transformations to a ray.

        Parameters:
            ray (Ray)
            transformation (Matrix)

        Returns:
            transformed (Ray)
    """

    transformed = Ray(transformation * ray.origin, transformation * ray.direction)
    return transformed
