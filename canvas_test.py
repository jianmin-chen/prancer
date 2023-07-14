from canvas import Canvas
from tuple import Color
import unittest


class Tests(unittest.TestCase):
    def test_scenario1(self):
        """
        Scenario: Creating a canvas
          Given c ← canvas(10, 20)
          Then c.width = 10
            And c.height = 20
            And every pixel of c is color(0, 0, 0)
        """

        c = Canvas(10, 20)
        self.assertEqual(c.width, 10)
        self.assertEqual(c.height, 20)
        for pixel in c.canvas:
            self.assertEqual(pixel, Color(0, 0, 0))

    def test_scenario2(self):
        """
        Scenario: Writing pixels to a canvas
          Given c ← canvas(10, 20)
            And red ← color(1, 0, 0)
          When write_pixel(c, 2, 3, red)
          Then pixel_at(c, 2, 3) = red
        """

        c = Canvas(10, 20)
        red = Color(1, 0, 0)
        c.write_pixel(2, 3, red)
        self.assertEqual(c.pixel_at(2, 3), red)

    def test_scenario3(self):
        """
        Scenario: Constructing the PPM header
            Given c ← canvas(5, 3)
            When ppm ← canvas_to_ppm(c)
            Then lines 1-3 of ppm are
              \"\"\"
              P3
              5 3
              255
              \"\"\"
        """

        c = Canvas(5, 3)
        ppm = c.to_ppm(False)
        self.assertTrue(ppm[:3], ["P3", "5 3", "255"])

    def test_scenario4(self):
        """
        Scenario: Constructing the PPM pixel data
            Given c ← canvas(5, 3)
            And c1 ← color(1.5, 0, 0)
            And c2 ← color(0, 0.5, 0)
            And c3 ← color(-0.5, 0, 1)
            When write_pixel(c, 0, 0, c1)
            And write_pixel(c, 2, 1, c2)
            And write_pixel(c, 4, 2, c3)
            And ppm ← canvas_to_ppm(c)
            Then lines 4-6 of ppm are
              \"\"\"
              255 0 0 0 0 0 0 0 0 0 0 0 0 0 0
              0 0 0 0 0 0 0 128 0 0 0 0 0 0 0
              0 0 0 0 0 0 0 0 0 0 0 0 0 0 255
              \"\"\"
        """

        c = Canvas(5, 3)
        c1 = Color(1.5, 0, 0)
        c2 = Color(0, 0.5, 0)
        c3 = Color(-0.5, 0, 1)
        c.write_pixel(0, 0, c1)
        c.write_pixel(2, 1, c2)
        c.write_pixel(4, 2, c3)
        ppm = c.to_ppm(False)
        self.assertEqual(
            ppm[3:6],
            [
                "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
                "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0",
                "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255",
            ],
        )

    def test_scenario5(self):
        """
        Scenario: Splitting long lines in PPM files
            Given c ← canvas(10, 2)
            When every pixel of c is set to color(1, 0.8, 0.6)
            And ppm ← canvas_to_ppm(c)
            Then lines 4-7 of ppm are
              \"\"\"
              255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
              153 255 204 153 255 204 153 255 204 153 255 204 153
              255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
              153 255 204 153 255 204 153 255 204 153 255 204 153
              \"\"\"
        """

        c = Canvas(10, 2)
        for y in range(c.height):
            for x in range(c.width):
                c.write_pixel(x, y, Color(1, 0.8, 0.6))
        ppm = c.to_ppm(False)
        self.assertEqual(
            ppm[3:7],
            [
                "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
                "153 255 204 153 255 204 153 255 204 153 255 204 153",
                "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
                "153 255 204 153 255 204 153 255 204 153 255 204 153",
            ],
        )

    def test_scenario6(self):
        """
        Scenario: PPM files are terminated by a newline character
            Given c ← canvas(5, 3)
            When ppm ← canvas_to_ppm(c)
            Then ppm ends with a newline character
        """

        c = Canvas(5, 3)
        ppm = c.to_ppm()
        self.assertEqual(ppm[-1], "\n")


if __name__ == "__main__":
    unittest.main()
