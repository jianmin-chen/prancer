from ray import Ray, Intersections, Intersection, hit, transform
from sphere import Sphere
from tuple import point, vector
from transformations import translation, scaling
import unittest


class Tests(unittest.TestCase):
    def test_scenario1(self):
        """
        Scenario: Creating and querying a ray
          Given origin ← point(1, 2, 3)
            And direction ← vector(4, 5, 6)
          When r ← ray(origin, direction)
          Then r.origin = origin
            And r.direction = direction
        """

        origin = point(1, 2, 3)
        direction = vector(4, 5, 6)
        r = Ray(origin, direction)
        self.assertEqual(r.origin, origin)
        self.assertEqual(r.direction, direction)

    def test_scenario2(self):
        """
        Scenario: Computing a point from a distance
          Given r ← ray(point(2, 3, 4), vector(1, 0, 0))
          Then position(r, 0) = point(2, 3, 4)
            And position(r, 1) = point(3, 3, 4)
            And position(r, -1) = point(1, 3, 4)
            And position(r, 2.5) = point(4.5, 3, 4)
        """

        r = Ray(point(2, 3, 4), vector(1, 0, 0))
        self.assertEqual(r.position(0), point(2, 3, 4))

    def test_scenario3(self):
        """
        Scenario: An intersection encapsulates t and object
          Given s ← sphere()
          When i ← intersection(3.5, s)
          Then i.t = 3.5
            And i.object = s
        """

        s = Sphere()
        i = Intersection(3.5, s)
        self.assertEqual(i.t, 3.5)
        self.assertEqual(i.object, s)

    def test_scenario4(self):
        """
        Scenario: Aggregating intersections
          Given: s ← sphere()
            And i1 ← intersection(1, s)
            And i2 ← intersection(2, s)
          When xs ← intersections(i1, i2)
          Then xs.count = 2
            And xs[0].t = 1
            And xs[1].t = 2
        """

        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections(i1, i2)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].t, 1)
        self.assertEqual(xs[1].t, 2)

    def test_scenario5(self):
        """
        Scenario: Intersect sets the object on the intersection
            Given r ← ray(point(0, 0, -5), vector(0, 0, 1))
            And s ← sphere()
            When xs ← intersect(s, r)
            Then xs.count = 2
            And xs[0].object = s
            And xs[1].object = s
        """

        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].object, s)
        self.assertEqual(xs[1].object, s)

    def test_scenario6(self):
        """
        Scenario: The hit, when all intersections have positive t
            Given s ← sphere()
            And i1 ← intersection(1, s)
            And i2 ← intersection(2, s)
            And xs ← intersections(i2, i1)
            When i ← hit(xs)
            Then i = i1
        """

        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections(i2, i1)
        i = hit(xs)
        self.assertEqual(i, i1)

    def test_scenario7(self):
        """
        Scenario: The hit, when some intersections have negative t
            Given s ← sphere()
            And i1 ← intersection(-1, s)
            And i2 ← intersection(1, s)
            And xs ← intersections(i2, i1)
            When i ← hit(xs)
            Then i = i2
        """

        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(1, s)
        xs = Intersections(i2, i1)
        i = hit(xs)
        self.assertEqual(i, i2)

    def test_scenario8(self):
        """
        Scenario: The hit, when all intersections have negative t
            Given s ← sphere()
            And i1 ← intersection(-2, s)
            And i2 ← intersection(-1, s)
            And xs ← intersections(i2, i1)
            When i ← hit(xs)
            Then i is nothing
        """

        s = Sphere()
        i1 = Intersection(-2, s)
        i2 = Intersection(-1, s)
        xs = Intersections(i2, i1)
        i = hit(xs)
        self.assertIsNone(i)

    def test_scenario9(self):
        """
        Scenario: The hit is always the lowest nonnegative intersection
            Given s ← sphere()
            And i1 ← intersection(5, s)
            And i2 ← intersection(7, s)
            And i3 ← intersection(-3, s)
            And i4 ← intersection(2, s)
            And xs ← intersections(i1, i2, i3, i4)
            When i ← hit(xs)
            Then i = i4
        """

        s = Sphere()
        i1 = Intersection(5, s)
        i2 = Intersection(7, s)
        i3 = Intersection(-3, s)
        i4 = Intersection(2, s)
        xs = Intersections(i1, i2, i3, i4)
        i = hit(xs)
        self.assertEqual(i, i4)

    def test_scenario10(self):
        """
        Scenario: Translating a ray
            Given r ← ray(point(1, 2, 3), vector(0, 1, 0))
            And m ← translation(3, 4, 5)
            When r2 ← transform(r, m)
            Then r2.origin = point(4, 6, 8)
            And r2.direction = vector(0, 1, 0)
        """

        r = Ray(point(1, 2, 3), vector(0, 1, 0))
        m = translation(3, 4, 5)
        r2 = transform(r, m)
        self.assertEqual(r2.origin, point(4, 6, 8))
        self.assertEqual(r2.direction, vector(0, 1, 0))

    def test_scenario11(self):
        """
        Scenario: Scaling a ray
            Given r ← ray(point(1, 2, 3), vector(0, 1, 0))
            And m ← scaling(2, 3, 4)
            When r2 ← transform(r, m)
            Then r2.origin = point(2, 6, 12)
            And r2.direction = vector(0, 3, 0)
        """

        r = Ray(point(1, 2, 3), vector(0, 1, 0))
        m = scaling(2, 3, 4)
        r2 = transform(r, m)
        self.assertEqual(r2.origin, point(2, 6, 12))
        self.assertEqual(r2.direction, vector(0, 3, 0))


if __name__ == "__main__":
    unittest.main()
