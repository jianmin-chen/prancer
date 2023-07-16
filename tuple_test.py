import math, unittest
from tuple import Tuple, Color, point, vector, magnitude, normalize, dot, cross, reflect


class Tests(unittest.TestCase):
    def test_scenario1(self):
        """
        Scenario: A tuple with w=1.0 is a point
         Given a ← tuple(4.3, -4.2, 3.1, 1.0)
         Then a.x = 4.3
           And a.y = -4.2
           And a.z = 3.1
           And a.w = 1.0
           And a is a point
           And a is not a vector
        """

        a = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(a.x, 4.3)
        self.assertEqual(a.y, -4.2)
        self.assertEqual(a.z, 3.1)
        self.assertEqual(a.w, 1.0)
        self.assertEqual(a.type, "point")
        self.assertNotEqual(a.type, "vector")

    def test_scenario2(self):
        """
        Scenario: A tuple with w=0 is a vector
          Given a ← tuple(4.3, -4.2, 3.1, 0.0)
          Then a.x = 4.3
            And a.y = -4.2
            And a.z = 3.1
            And a.w = 0.0
            And a is not a point
            And a is a vector
        """

        a = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertEqual(a.x, 4.3)
        self.assertEqual(a.y, -4.2)
        self.assertEqual(a.z, 3.1)
        self.assertEqual(a.w, 0.0)
        self.assertNotEqual(a.type, "point")
        self.assertEqual(a.type, "vector")

    def test_scenario3(self):
        """
        Scenario: point() creates tuples with w=1
            Given p ← point(4, -4, 3)
            Then p = tuple(4, -4, 3, 1)
        """

        p = point(4, -4, 3)
        self.assertEqual(p, Tuple(4, -4, 3, 1))

    def test_scenario4(self):
        """
        Scenario: vector() creates tuples with w=0
          Given v ← vector(4, -4, 3)
          Then v = tuple(4, -4, 3, 0)
        """

        v = vector(4, -4, 3)
        self.assertEqual(v, Tuple(4, -4, 3, 0))

    def test_scenario5(self):
        """
        Scenario: Adding two tuples
            Given a1 ← tuple(3, -2, 5, 1)
            And a2 ← tuple(-2, 3, 1, 0)
            Then a1 + a2 = tuple(1, 1, 6, 1)
        """

        a1 = Tuple(3, -2, 5, 1)
        a2 = Tuple(-2, 3, 1, 0)
        self.assertEqual(a1 + a2, Tuple(1, 1, 6, 1))

    def test_scenario6(self):
        """
        Scenario: Subtracting two points
            Given p1 ← point(3, 2, 1)
            And p2 ← point(5, 6, 7)
            Then p1 - p2 = vector(-2, -4, -6)
        """

        p1 = point(3, 2, 1)
        p2 = point(5, 6, 7)
        self.assertEqual(p1 - p2, vector(-2, -4, -6))

    def test_scenario7(self):
        """
        Scenario: Subtracting a vector from a point
            Given p ← point(3, 2, 1)
            And v ← vector(5, 6, 7)
            Then p - v = point(-2, -4, -6)
        """

        p = point(3, 2, 1)
        v = vector(5, 6, 7)
        self.assertEqual(p - v, point(-2, -4, -6))

    def test_scenario8(self):
        """
        Scenario: Subtracting two vectors
            Given v1 ← vector(3, 2, 1)
            And v2 ← vector(5, 6, 7)
            Then v1 - v2 = vector(-2, -4, -6)
        """

        v1 = vector(3, 2, 1)
        v2 = vector(5, 6, 7)
        self.assertEqual(v1 - v2, vector(-2, -4, -6))

    def test_scenario9(self):
        """
        Scenario: Subtracting a vector from the zero vector
            Given zero ← vector(0, 0, 0)
            And v ← vector(1, -2, 3)
            Then zero - v = vector(-1, 2, -3)
        """

        zero = vector(0, 0, 0)
        v = vector(1, -2, 3)
        self.assertEqual(zero - v, vector(-1, 2, -3))

    def test_scenario10(self):
        """
        Scenario: Negating a tuple
            Given a ← tuple(1, -2, 3, -4)
            Then -a = tuple(-1, 2, -3, 4)
        """

        a = Tuple(1, 2, 3, -4)
        self.assertEqual(-a, Tuple(-1, -2, -3, 4))

    def test_scenario11(self):
        """
        Scenario: Multiplying a tuple by a scalar
            Given a ← tuple(1, -2, 3, -4)
            Then a * 3.5 = tuple(3.5, -7, 10.5, -14)
        """

        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a * 3.5, Tuple(3.5, -7, 10.5, -14))

    def test_scenario12(self):
        """
        Scenario: Multiplying a tuple by a fraction
            Given a ← tuple(1, -2, 3, -4)
            Then a * 0.5 = tuple(0.5, -1, 1.5, -2)
        """

        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a * 0.5, Tuple(0.5, -1, 1.5, -2))

    def test_scenario13(self):
        """
        Scenario: Dividing a tuple by a scalar
            Given a ← tuple(1, -2, 3, -4)
            Then a / 2 = tuple(0.5, -1, 1.5, -2)
        """

        a = Tuple(1, -2, 3, -4)
        self.assertEqual(a / 2, Tuple(0.5, -1, 1.5, -2))

    def test_scenario14(self):
        """
        Scenario: Computing the magnitude of vector(0, 1, 0)
            Given v ← vector(0, 1, 0)
            Then magnitude(v) = 1
        """

        v = vector(0, 1, 0)
        self.assertEqual(magnitude(v), 1)

    def test_scenario15(self):
        """
        Scenario: Computing the magnitude of vector(0, 0, 1)
            Given v ← vector(0, 0, 1)
            Then magnitude(v) = 1
        """

        v = vector(0, 0, 1)
        self.assertEqual(magnitude(v), 1)

    def test_scenario16(self):
        """
        Scenario: Computing the magnitude of vector(1, 2, 3)
            Given v ← vector(1, 2, 3)
            Then magnitude(v) = √14
        """

        v = vector(1, 2, 3)
        self.assertEqual(magnitude(v), math.sqrt(14))

    def test_scenario17(self):
        """
        Scenario: Computing the magnitude of vector(-1, -2, -3)
            Given v ← vector(-1, -2, -3)
            Then magnitude(v) = √14
        """

        v = vector(-1, -2, -3)
        self.assertEqual(magnitude(v), math.sqrt(14))

    def test_scenario18(self):
        """
        Scenario: Normalizing vector(4, 0, 0) gives (1, 0, 0)
            Given v ← vector(4, 0, 0)
            Then normalize(v) = vector(1, 0, 0)
        """

        v = vector(4, 0, 0)
        self.assertEqual(normalize(v), vector(1, 0, 0))

    def test_scenario19(self):
        """
        Scenario: Normalizing vector(1, 2, 3)
            Given v ← vector(1, 2, 3)
            # vector(1/√14,   2/√14,   3/√14)
            Then normalize(v) = approximately vector(0.26726, 0.53452, 0.80178)
        """

        v = vector(1, 2, 3)
        self.assertEqual(
            normalize(v),
            vector(1 / math.sqrt(14), 2 / math.sqrt(14), 3 / math.sqrt(14)),
        )

    def test_scenario20(self):
        """
        Scenario: The magnitude of a normalized vector
            Given v ← vector(1, 2, 3)
            When norm ← normalize(v)
            Then magnitude(norm) = 1
        """

        v = vector(1, 2, 3)
        norm = normalize(v)
        self.assertEqual(magnitude(norm), 1)

    def test_scenario21(self):
        """
        Scenario: The dot product of two tuples
            Given a ← vector(1, 2, 3)
            And b ← vector(2, 3, 4)
            Then dot(a, b) = 20
        """

        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        self.assertEqual(dot(a, b), 20)

    def test_scenario22(self):
        """
        Scenario: The cross product of two vectors
            Given a ← vector(1, 2, 3)
            And b ← vector(2, 3, 4)
            Then cross(a, b) = vector(-1, 2, -1)
            And cross(b, a) = vector(1, -2, 1)
        """

        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        self.assertEqual(cross(a, b), vector(-1, 2, -1))
        self.assertEqual(cross(b, a), vector(1, -2, 1))

    def test_scenario23(self):
        """
        Scenario: Colors are (red, green, blue) tuples
            Given c ← color(-0.5, 0.4, 1.7)
            Then c.red = -0.5
            And c.green = 0.4
            And c.blue = 1.7
        """

        c = Color(-0.5, 0.4, 1.7)
        self.assertEqual(c.red, -0.5)
        self.assertEqual(c.green, 0.4)
        self.assertEqual(c.blue, 1.7)

    def test_scenario24(self):
        """
        Scenario: Adding colors
            Given c1 ← color(0.9, 0.6, 0.75)
            And c2 ← color(0.7, 0.1, 0.25)
            Then c1 + c2 = color(1.6, 0.7, 1.0)
        """

        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertEqual(c1 + c2, Color(1.6, 0.7, 1.0))

    def test_scenario25(self):
        """
        Scenario: Subtracting colors
            Given c1 ← color(0.9, 0.6, 0.75)
            And c2 ← color(0.7, 0.1, 0.25)
            Then c1 - c2 = color(0.2, 0.5, 0.5)
        """

        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertEqual(c1 - c2, Color(0.2, 0.5, 0.5))

    def test_scenario26(self):
        """
        Scenario: Multiplying a color by a scalar
           Given c ← color(0.2, 0.3, 0.4)
           Then c * 2 = color(0.4, 0.6, 0.8)
        """

        c = Color(0.2, 0.3, 0.4)
        self.assertEqual(c * 2, Color(0.4, 0.6, 0.8))

    def test_scenario27(self):
        """
        Scenario: Multiplying colors
            Given c1 ← color(1, 0.2, 0.4)
            And c2 ← color(0.9, 1, 0.1)
            Then c1 * c2 = color(0.9, 0.2, 0.04)
        """

        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        self.assertEqual(c1 * c2, Color(0.9, 0.2, 0.04))

    def test_scenario28(self):
        """
        Scenario: Reflecting a vector approaching at 45°
          Given v ← vector(1, -1, 0)
            And n ← vector(0, 1, 0)
          When r ← reflect(v, n)
          Then r = vector(1, 1, 0)
        """

        v = vector(1, -1, 0)
        n = vector(0, 1, 0)
        r = reflect(v, n)
        self.assertEqual(r, vector(1, 1, 0))

    def test_scenario29(self):
        """
        Scenario: Reflecting a vector off a slanted surface
          Given v ← vector(0, -1, 0)
            And n ← vector(√2/2, √2/2, 0)
          When r ← reflect(v, n)
          Then r = vector(1, 0, 0)
        """

        v = vector(0, -1, 0)
        n = vector(math.sqrt(2) / 2, math.sqrt(2) / 2, 0)
        r = reflect(v, n)
        self.assertEqual(r, vector(1, 0, 0))


if __name__ == "__main__":
    unittest.main()
