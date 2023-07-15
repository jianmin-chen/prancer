from tuple import Color
from canvas import Canvas

width = 2560
height = 1664

c = Canvas(width, height)


def pattern_at(gradient, point):
    pass


for y in range(height):
    for x in range(width):
        c.write_pixel(x, y, Color(0, 0, 0))

with open("test.ppm", "w") as f:
    f.write(c.to_ppm(True))
