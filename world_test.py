from canvas import Color
from lights import PointLight
from material import Material
from ray import Ray, Intersection
from sphere import Sphere
from transformations import scaling
from tuple import point, vector
from world import World, default_world, prepare_computations
import unittest


class Tests(unittest.TestCase):
    def test_scenario1(self):
        """
        Scenario: The default world
            Given light ← point_light(point(-10, 10, -10), color(1, 1, 1))
            And s1 ← sphere() with:
              | material.color    | (0.8, 1.0, 0.6) |
              | material.diffuse  | 0.7             |
              | material.specular | 0.2             |
            And s2 ← sphere() with:
              | transform | scaling(0.5, 0.5, 0.5) |
            When w ← default_world()
            Then w.light = light
            And w contains s1
            And w contains s2
        """

        light = PointLight(point(-10, 10, -10), Color(1, 1, 1))
        s1 = Sphere()
        s1.material.color = Color(0.8, 1, 0.6)
        s1.material.diffuse = 0.7
        s1.material.specular = 0.2
        s2 = Sphere(point(0, 0, 0), 1, Material())
        s2.set_transform(scaling(0.5, 0.5, 0.5))
        w = default_world()
        self.assertEqual(w.light_source, light)
        self.assertTrue(w.includes(s1))
        self.assertTrue(w.includes(s2))

    def test_scenario2(self):
        """
        Scenario: Intersect a world with a ray
            Given w ← default_world()
            And r ← ray(point(0, 0, -5), vector(0, 0, 1))
            When xs ← intersect_world(w, r)
            Then xs.count = 4
            And xs[0].t = 4
            And xs[1].t = 4.5
            And xs[2].t = 5.5
            And xs[3].t = 6
        """

        w = default_world()
        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        xs = w.intersect(r)
        self.assertEqual(xs.count, 4)
        self.assertEqual(xs[0].t, 4)
        self.assertEqual(xs[1].t, 4.5)
        self.assertEqual(xs[2].t, 5.5)
        self.assertEqual(xs[3].t, 6)

    def test_scenario3(self):
        """
        Scenario: Precomputing the state of an intersection
            Given r ← ray(point(0, 0, -5), vector(0, 0, 1))
            And shape ← sphere()
            And i ← intersection(4, shape)
            When comps ← prepare_computations(i, r)
            Then comps.t = i.t
            And comps.object = i.object
            And comps.point = point(0, 0, -1)
            And comps.eyev = vector(0, 0, -1)
            And comps.normalv = vector(0, 0, -1)
        """

        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        shape = Sphere()
        i = Intersection(4, shape)
        comps = prepare_computations(i, r)
        self.assertEqual(comps.t, i.t)
        self.assertEqual(comps.object, i.object)
        self.assertEqual(comps.point, point(0, 0, -1))
        self.assertEqual(comps.eyev, vector(0, 0, -1))
        self.assertEqual(comps.normalv, vector(0, 0, -1))

    def test_scenario4(self):
        """
        Scenario: The hit, when an intersection occurs on the outside
            Given r ← ray(point(0, 0, -5), vector(0, 0, 1))
            And shape ← sphere()
            And i ← intersection(4, shape)
            When comps ← prepare_computations(i, r)
            Then comps.inside = false
        """

        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        shape = Sphere()
        i = Intersection(4, shape)
        comps = prepare_computations(i, r)
        self.assertFalse(comps.inside)

    def test_scenario5(self):
        """
        Scenario: The hit, when an intersection occurs on the inside
            Given r ← ray(point(0, 0, 0), vector(0, 0, 1))
            And shape ← sphere()
            And i ← intersection(1, shape)
            When comps ← prepare_computations(i, r)
            Then comps.point = point(0, 0, 1)
            And comps.eyev = vector(0, 0, -1)
            And comps.inside = true
            # normal would have been (0, 0, 1), but is inverted!
            And comps.normalv = vector(0, 0, -1)
        """

        r = Ray(point(0, 0, 0), vector(0, 0, 1))
        shape = Sphere()
        i = Intersection(1, shape)
        comps = prepare_computations(i, r)
        self.assertEqual(comps.point, point(0, 0, 1))
        self.assertEqual(comps.eyev, vector(0, 0, -1))
        self.assertTrue(comps.inside)
        self.assertEqual(comps.normalv, vector(0, 0, -1))

    def test_scenario6(self):
        """
        Scenario: Shading an intersection
            Given w ← default_world()
            And r ← ray(point(0, 0, -5), vector(0, 0, 1))
            And shape ← the first object in w
            And i ← intersection(4, shape)
            When comps ← prepare_computations(i, r)
            And c ← shade_hit(w, comps)
            Then c = color(0.38066, 0.47583, 0.2855)
        """

        w = default_world()
        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        shape = w[0]
        i = Intersection(4, shape)
        comps = prepare_computations(i, r)
        c = w.shade_hit(comps)
        self.assertEqual(c, Color(0.38066, 0.47583, 0.2855))

    def test_scenario7(self):
        """
        Scenario: Shading an intersection from the inside
            Given w ← default_world()
            And w.light ← point_light(point(0, 0.25, 0), color(1, 1, 1))
            And r ← ray(point(0, 0, 0), vector(0, 0, 1))
            And shape ← the second object in w
            And i ← intersection(0.5, shape)
            When comps ← prepare_computations(i, r)
            And c ← shade_hit(w, comps)
            Then c = color(0.90498, 0.90498, 0.90498)
        """

        w = default_world()
        w.light_source = PointLight(point(0, 0.25, 0), Color(1, 1, 1))
        r = Ray(point(0, 0, 0), vector(0, 0, 1))
        shape = w[1]
        i = Intersection(0.5, shape)
        comps = prepare_computations(i, r)
        c = w.shade_hit(comps)
        self.assertEqual(c, Color(0.90498, 0.90498, 0.90498))

    def test_scenario8(self):
        """
        Scenario: The color when a ray misses
            Given w ← default_world()
            And r ← ray(point(0, 0, -5), vector(0, 1, 0))
            When c ← color_at(w, r)
            Then c = color(0, 0, 0)
        """

        w = default_world()
        r = Ray(point(0, 0, -5), vector(0, 1, 0))
        c = w.color_at(r)
        self.assertEqual(c, Color(0, 0, 0))

    def test_scenario9(self):
        """
        Scenario: The color when a ray hits
            Given w ← default_world()
            And r ← ray(point(0, 0, -5), vector(0, 0, 1))
            When c ← color_at(w, r)
            Then c = color(0.38066, 0.47583, 0.2855)
        """

        w = default_world()
        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        c = w.color_at(r)
        self.assertEqual(c, Color(0.38066, 0.47583, 0.2855))

    def test_scenario10(self):
        """
        Scenario: The color with an intersection behind the ray
            Given w ← default_world()
            And outer ← the first object in w
            And outer.material.ambient ← 1
            And inner ← the second object in w
            And inner.material.ambient ← 1
            And r ← ray(point(0, 0, 0.75), vector(0, 0, -1))
            When c ← color_at(w, r)
            Then c = inner.material.color
        """

        w = default_world()
        outer = w[0]
        outer.material.ambient = 1
        inner = w[1]
        inner.material.ambient = 1
        r = Ray(point(0, 0, 0.75), vector(0, 0, -1))
        c = w.color_at(r)
        self.assertEqual(c, inner.material.color)


if __name__ == "__main__":
    unittest.main()
