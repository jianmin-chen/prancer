from __future__ import annotations
from copy import copy
from canvas import Color
from lights import PointLight
from material import lighting, Material
from ray import Ray, Intersection, Intersections, hit
from sphere import Sphere
from tuple import point, dot
from transformations import scaling
from utils import equal


class Computations:
    def __init__(self):
        self.t = None
        self.object = None
        self.point = None
        self.eyev = None
        self.normalv = None
        self.inside = None


class World:
    def __init__(self, objects: list = [], light_source: PointLight = None):
        self.objects = objects
        self.light_source = light_source

    def includes(self, obj) -> bool:
        for object in self.objects:
            if obj == object:
                return True
        return False

    def intersect(self, ray: Ray) -> Intersections:
        """
        Determine where ray intersects objects, in world context.

            Parameters:
                ray (Ray)

            Returns:
                intersections (Intersections)
        """

        intersections = Intersections()
        for obj in self.objects:
            intersections.intersections.extend(ray.intersect(obj))
        intersections.intersections = sorted(
            intersections.intersections, key=lambda intersection: intersection.t
        )
        return intersections

    def shade_hit(self, comps: Computations) -> Color:
        """
        Returns the color at the intersection encapsulated by a computation.

            Parameters:
                comps (Computations)

            Returns:
                color (Color)
        """

        color = lighting(
            comps.object.material,
            self.light_source,
            comps.point,
            comps.eyev,
            comps.normalv,
        )
        return color

    def color_at(self, ray: Ray) -> Color:
        """
        Returns the color at the given intersection.

            Parameters:
                ray (Ray)

            Returns:
                color (Color)
        """

        intersections = self.intersect(ray)
        reach = hit(intersections)
        if not reach:
            return Color(0, 0, 0)
        comps = prepare_computations(reach, ray)
        return self.shade_hit(comps)

    def __copy__(self) -> World:
        return World(copy(self.objects), copy(self.light_source))

    def __getitem__(self, index: int):
        return self.objects[index]


def default_world():
    """
    Generates a default world with two spheres.
    """

    s1 = Sphere()
    s1.material.color = Color(0.8, 1, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    s2 = Sphere(point(0, 0, 0), 1, Material())
    s2.set_transform(scaling(0.5, 0.5, 0.5))
    return World([copy(s1), copy(s2)], PointLight(point(-10, 10, -10), Color(1, 1, 1)))


def prepare_computations(intersection: Intersection, ray: Ray):
    comps = Computations()
    comps.t = intersection.t
    comps.object = intersection.object
    comps.point = ray.position(comps.t)
    comps.eyev = -ray.direction
    comps.normalv = comps.object.normal_at(comps.point)
    if dot(comps.normalv, comps.eyev) < 0:
        comps.inside = True
        comps.normalv = -comps.normalv
    else:
        comps.inside = False
    return comps
