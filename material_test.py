from math import sqrt
from canvas import Color
from lights import PointLight
from material import Material, lighting
from tuple import point, vector
import unittest


class Tests(unittest.TestCase):
    def test_scenario1(self):
        """
        Scenario: The default material
          Given m ← material()
          Then m.color = color(1, 1, 1)
            And m.ambient = 0.1
            And m.diffuse = 0.9
            And m.specular = 0.9
            And m.shininess = 200.0
        """

        m = Material()
        self.assertEqual(m.color, Color(1, 1, 1))
        self.assertEqual(m.ambient, 0.1)
        self.assertEqual(m.diffuse, 0.9)
        self.assertEqual(m.specular, 0.9)
        self.assertEqual(m.shininess, 200)

    def test_scenario2(self):
        """
        Background:
            Given m ← material()
            And position ← point(0, 0, 0)
        Scenario: Lighting with the eye between the light and the surface
          Given eyev ← vector(0, 0, -1)
            And normalv ← vector(0, 0, -1)
            And light ← point_light(point(0, 0, -10), color(1, 1, 1))
          When result ← lighting(m, light, position, eyev, normalv)
          Then result = color(1.9, 1.9, 1.9)
        """

        m = Material()
        position = point(0, 0, 0)
        eyev = vector(0, 0, -1)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 0, -10), Color(1, 1, 1))
        result = lighting(m, light, position, eyev, normalv)
        self.assertEqual(result, Color(1.9, 1.9, 1.9))

    def test_scenario3(self):
        """
        Background:
          Given m ← material()
            And position ← point(0, 0, 0)
        Scenario: Lighting with the eye between light and surface, eye offset 45°
          Given eyev ← vector(0, √2/2, -√2/2)
            And normalv ← vector(0, 0, -1)
            And light ← point_light(point(0, 0, -10), color(1, 1, 1))
          When result ← lighting(m, light, position, eyev, normalv)
          Then result = color(1.0, 1.0, 1.0)
        """

        m = Material()
        position = point(0, 0, 0)
        eyev = vector(0, sqrt(2) / 2, -(sqrt(2) / 2))
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 0, -10), Color(1, 1, 1))
        result = lighting(m, light, position, eyev, normalv)
        self.assertEqual(result, Color(1, 1, 1))

    def test_scenario4(self):
        """
        Background:
          Given m ← material()
            And position ← point(0, 0, 0)
        Scenario: Lighting with eye opposite surface, light offset 45°
          Given eyev ← vector(0, 0, -1)
            And normalv ← vector(0, 0, -1)
            And light ← point_light(point(0, 10, -10), color(1, 1, 1))
          When result ← lighting(m, light, position, eyev, normalv)
          Then result = color(0.7364, 0.7364, 0.7364)
        """

        m = Material()
        position = point(0, 0, 0)
        eyev = vector(0, 0, -1)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 10, -10), Color(1, 1, 1))
        result = lighting(m, light, position, eyev, normalv)
        self.assertEqual(result, Color(0.7364, 0.7364, 0.7364))

    def test_scenario5(self):
        """
        Background:
          Given m ← material()
            And position ← point(0, 0, 0)
        Scenario: Lighting with eye in the path of the reflection vector
          Given eyev ← vector(0, -√2/2, -√2/2)
            And normalv ← vector(0, 0, -1)
            And light ← point_light(point(0, 10, -10), color(1, 1, 1))
          When result ← lighting(m, light, position, eyev, normalv)
          Then result = color(1.6364, 1.6364, 1.6364)
        """

        m = Material()
        position = point(0, 0, 0)
        eyev = vector(0, -(sqrt(2) / 2), -(sqrt(2) / 2))
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 10, -10), Color(1, 1, 1))
        result = lighting(m, light, position, eyev, normalv)
        self.assertEqual(result, Color(1.6364, 1.6364, 1.6364))


if __name__ == "__main__":
    unittest.main()
