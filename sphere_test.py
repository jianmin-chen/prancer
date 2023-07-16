from math import sqrt, pi
from material import Material
from matrix import identity_matrix
from ray import Ray, Intersection, Intersections, hit
from sphere import Sphere
from transformations import translation, scaling, rotation_z
from tuple import point, vector, normalize
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

    def test_scenario10(self):
        """
        Scenario: The normal on a sphere at a point on the x axis
            Given s ← sphere()
            When n ← normal_at(s, point(1, 0, 0))
            Then n = vector(1, 0, 0)
        """

        s = Sphere()
        n = s.normal_at(point(1, 0, 0))
        self.assertEqual(n, vector(1, 0, 0))

    def test_scenario11(self):
        """
        Scenario: The normal on a sphere at a point on the y axis
            Given s ← sphere()
            When n ← normal_at(s, point(0, 1, 0))
            Then n = vector(0, 1, 0)
        """

        s = Sphere()
        n = s.normal_at(point(0, 1, 0))
        self.assertEqual(n, vector(0, 1, 0))

    def test_scenario12(self):
        """
        Scenario: The normal on a sphere at a point on the z axis
            Given s ← sphere()
            When n ← normal_at(s, point(0, 0, 1))
            Then n = vector(0, 0, 1)
        """

        s = Sphere()
        n = s.normal_at(point(0, 0, 1))
        self.assertEqual(n, vector(0, 0, 1))

    def test_scenario13(self):
        """
        Scenario: The normal on a sphere at a nonaxial point
            Given s ← sphere()
            When n ← normal_at(s, point(√3/3, √3/3, √3/3))
            Then n = vector(√3/3, √3/3, √3/3)
        """

        s = Sphere()
        n = s.normal_at(point(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))
        self.assertEqual(n, vector(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))

    def test_scenario14(self):
        """
        Scenario: The normal is a normalized vector
            Given s ← sphere()
            When n ← normal_at(s, point(√3/3, √3/3, √3/3))
            Then n = normalize(n)
        """

        s = Sphere()
        n = s.normal_at(point(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))
        self.assertEqual(n, normalize(n))

    def test_scenario15(self):
        """
        Scenario: Computing the normal on a translated sphere
            Given s ← sphere()
            And set_transform(s, translation(0, 1, 0))
            When n ← normal_at(s, point(0, 1.70711, -0.70711))
            Then n = vector(0, 0.70711, -0.70711)
        """

        s = Sphere()
        s.set_transform(translation(0, 1, 0))
        n = s.normal_at(point(0, 1.70711, -0.70711))
        self.assertEqual(n, vector(0, 0.70711, -0.70711))

    def test_scenario16(self):
        """
        Scenario: Computing the normal on a transformed sphere
            Given s ← sphere()
            And m ← scaling(1, 0.5, 1) * rotation_z(π/5)
            And set_transform(s, m)
            When n ← normal_at(s, point(0, √2/2, -√2/2))
            Then n = vector(0, 0.97014, -0.24254)
        """

        s = Sphere()
        m = scaling(1, 0.5, 1) * rotation_z(pi / 5)
        s.set_transform(m)
        n = s.normal_at(point(0, sqrt(2) / 2, -(sqrt(2) / 2)))
        self.assertEqual(n, vector(0, 0.97014, -0.24254))

    def test_scenario17(self):
        """
        Scenario: A sphere has a default material
            Given s ← sphere()
            When m ← s.material
            Then m = material()
        """

        s = Sphere()
        m = s.material
        self.assertEqual(m, Material())

    def test_scenario18(self):
        """
        Scenario: A sphere may be assigned a material
            Given s ← sphere()
            And m ← material()
            And m.ambient ← 1
            When s.material ← m
            Then s.material = m
        """

        s = Sphere()
        m = Material()
        m.ambient = 1
        s.material = m
        self.assertEqual(s.material, m)


if __name__ == "__main__":
    unittest.main()
