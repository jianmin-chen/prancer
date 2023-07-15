from matrix import identity_matrix
from ray import Ray, Intersection, Intersections, hit
from sphere import Sphere
from transformations import translation, scaling
from tuple import point, vector
import unittest


class Tests(unittest.TestCase):
    def test_scenario1(self):
        """
        Scenario: A ray intersects a sphere at two points
          Given r ← ray(point(0, 0, -5), vector(0, 0, 1))
            And s ← sphere()
          When xs ← intersect(s, r)
          Then xs.count = 2
            And xs[0] = 4.0
            And xs[1] = 6.0
        """

        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].t, 4)
        self.assertEqual(xs[1].t, 6)

    def test_scenario2(self):
        """
        Scenario: A ray intersects a sphere at a tangent
          Given r ← ray(point(0, 1, -5), vector(0, 0, 1))
            And s ← sphere()
          When xs ← intersect(s, r)
          Then xs.count = 2
            And xs[0] = 5.0
            And xs[1] = 5.0
        """

        r = Ray(point(0, 1, -5), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].t, 5)
        self.assertEqual(xs[1].t, 5)

    def test_scenario3(self):
        """
        Scenario: A ray misses a sphere
          Given r ← ray(point(0, 2, -5), vector(0, 0, 1))
            And s ← sphere()
          When xs ← intersect(s, r)
          Then xs.count = 0
        """

        r = Ray(point(0, 2, -5), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertEqual(xs.count, 0)

    def test_scenario4(self):
        """
        Scenario: A ray originates inside a sphere
          Given r ← ray(point(0, 0, 0), vector(0, 0, 1))
            And s ← sphere()
          When xs ← intersect(s, r)
          Then xs.count = 2
            And xs[0] = -1.0
            And xs[1] = 1.0
        """

        r = Ray(point(0, 0, 0), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertEqual(xs[0].t, -1)
        self.assertEqual(xs[1].t, 1)

    def test_scenario5(self):
        """
        Scenario: A sphere is behind a ray
          Given r ← ray(point(0, 0, 5), vector(0, 0, 1))
            And s ← sphere()
          When xs ← intersect(s, r)
          Then xs.count = 2
            And xs[0] = -6.0
            And xs[1] = -4.0
        """

        r = Ray(point(0, 0, 5), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].t, -6)
        self.assertEqual(xs[1].t, -4)

    def test_scenario6(self):
        """
        Scenario: A sphere's default transformation
            Given s ← sphere()
            Then s.transform = identity_matrix
        """

        s = Sphere()
        self.assertEqual(s.transform, identity_matrix)

    def test_scenario7(self):
        """
        Scenario: Changing a sphere's transformation
            Given s ← sphere()
            And t ← translation(2, 3, 4)
            When set_transform(s, t)
            Then s.transform = t
        """

        s = Sphere()
        t = translation(2, 3, 4)
        s.set_transform(t)
        self.assertEqual(s.transform, t)

    def test_scenario8(self):
        """
        Scenario: Intersecting a scaled sphere with a ray
            Given r ← ray(point(0, 0, -5), vector(0, 0, 1))
            And s ← sphere()
            When set_transform(s, scaling(2, 2, 2))
            And xs ← intersect(s, r)
            Then xs.count = 2
            And xs[0].t = 3
            And xs[1].t = 7
        """

        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        s = Sphere()
        s.set_transform(scaling(2, 2, 2))
        xs = r.intersect(s)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].t, 3)
        self.assertEqual(xs[1].t, 7)

    def test_scenario9(self):
        """
        Scenario: Intersecting a translated sphere with a ray
            Given r ← ray(point(0, 0, -5), vector(0, 0, 1))
            And s ← sphere()
            When set_transform(s, translation(5, 0, 0))
            And xs ← intersect(s, r)
            Then xs.count = 0
        """

        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        s = Sphere()
        s.set_transform(translation(5, 0, 0))
        xs = r.intersect(s)
        self.assertEqual(xs.count, 0)


if __name__ == "__main__":
    unittest.main()
