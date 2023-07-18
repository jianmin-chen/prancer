from math import pi, sqrt
from camera import Camera
from canvas import Color
from matrix import identity_matrix
from transformations import rotation_y, translation, view_transform
from tuple import point, vector
from utils import equal
from world import default_world
import unittest


class Tests(unittest.TestCase):
    def test_scenario1(self):
        """
        Scenario: Constructing a camera
          Given hsize ← 160
            And vsize ← 120
            And field_of_view ← π/2
          When c ← camera(hsize, vsize, field_of_view)
          Then c.hsize = 160
            And c.vsize = 120
            And c.field_of_view = π/2
            And c.transform = identity_matrix
        """

        hsize = 160
        vsize = 120
        field_of_view = pi / 2
        c = Camera(hsize, vsize, field_of_view)
        self.assertEqual(c.hsize, 160)
        self.assertEqual(c.vsize, 120)
        self.assertEqual(c.field_of_view, pi / 2)
        self.assertEqual(c.transform, identity_matrix)

    def test_scenario2(self):
        """
        Scenario: The pixel size for a horizontal canvas
          Given c ← camera(200, 125, π/2)
          Then c.pixel_size = 0.01
        """

        c = Camera(200, 125, pi / 2)
        self.assertTrue(equal(c.pixel_size, 0.01))

    def test_scenario3(self):
        """
        Scenario: The pixel size for a vertical canvas
          Given c ← camera(125, 200, π/2)
          Then c.pixel_size = 0.01
        """

        c = Camera(125, 200, pi / 2)
        self.assertTrue(equal(c.pixel_size, 0.01))

    def test_scenario4(self):
        """
        Scenario: Constructing a ray through the center of the canvas
          Given c ← camera(201, 101, π/2)
          When r ← ray_for_pixel(c, 100, 50)
          Then r.origin = point(0, 0, 0)
            And r.direction = vector(0, 0, -1)
        """

        c = Camera(201, 101, pi / 2)
        r = c.ray_for_pixel(100, 50)
        self.assertEqual(r.origin, point(0, 0, 0))
        self.assertEqual(r.direction, vector(0, 0, -1))

    def test_scenario5(self):
        """
        Scenario: Constructing a ray through a corner of the canvas
          Given c ← camera(201, 101, π/2)
          When r ← ray_for_pixel(c, 0, 0)
          Then r.origin = point(0, 0, 0)
            And r.direction = vector(0.66519, 0.33259, -0.66851)
        """

        c = Camera(201, 101, pi / 2)
        r = c.ray_for_pixel(0, 0)
        self.assertEqual(r.origin, point(0, 0, 0))
        self.assertEqual(r.direction, vector(0.66519, 0.33259, -0.66851))

    def test_scenario6(self):
        """
        Scenario: Constructing a ray when the camera is transformed
          Given c ← camera(201, 101, π/2)
          When c.transform ← rotation_y(π/4) * translation(0, -2, 5)
            And r ← ray_for_pixel(c, 100, 50)
          Then r.origin = point(0, 2, -5)
            And r.direction = vector(√2/2, 0, -√2/2)
        """

        c = Camera(201, 101, pi / 2)
        c.transform = rotation_y(pi / 4) * translation(0, -2, 5)
        r = c.ray_for_pixel(100, 50)
        self.assertEqual(r.origin, point(0, 2, -5))
        self.assertEqual(r.direction, vector(sqrt(2) / 2, 0, -(sqrt(2) / 2)))

    def test_scenario7(self):
        """
        Scenario: Rendering a world with a camera
          Given w ← default_world()
            And c ← camera(11, 11, π/2)
            And from ← point(0, 0, -5)
            And to ← point(0, 0, 0)
            And up ← vector(0, 1, 0)
            And c.transform ← view_transform(from, to, up)
          When image ← render(c, w)
          Then pixel_at(image, 5, 5) = color(0.38066, 0.47583, 0.2855)
        """

        w = default_world()
        c = Camera(11, 11, pi / 2)
        start = point(0, 0, -5)
        to = point(0, 0, 0)
        up = vector(0, 1, 0)
        c.transform = view_transform(start, to, up)
        image = c.render(w)
        self.assertEqual(image.pixel_at(5, 5), Color(0.38066, 0.47583, 0.2855))


if __name__ == "__main__":
    unittest.main()
