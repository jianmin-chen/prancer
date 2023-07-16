from canvas import Color
from lights import PointLight
from tuple import point
import unittest


class Tests(unittest.TestCase):
    def test_scenario1(self):
        """
        Scenario: A point light has a position and intensity
          Given intensity ← color(1, 1, 1)
            And position ← point(0, 0, 0)
          When light ← point_light(position, intensity)
          Then light.position = position
            And light.intensity = intensity
        """

        intensity = Color(1, 1, 1)
        position = point(0, 0, 0)
        light = PointLight(position, intensity)
        self.assertEqual(light.position, position)
        self.assertEqual(light.intensity, intensity)


if __name__ == "__main__":
    unittest.main()
