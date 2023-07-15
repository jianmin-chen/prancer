from math import pi
from canvas import Canvas, Color
from transformations import rotation_y
from tuple import point

# Choose an axis to orient the clock. If, for example, it's oriented along the y axis and you're looking at it face-on, then you're looking toward the negative end of the y axis. This means twelve o' clock is on the z axis at point(0, 0, 1) and three o' clock is on the x axis at point(1, 0, 0).
twelve = point(0, 0, 1)
points = [twelve]

# Now, rotate the twelve o' clock point around the y axis to find the other hour positions. There are 2 * pi radians in a circle, so each hour is rotated pi / 8 radians.
for tick in range(12):
    rotation_matrix = rotation_y(pi / 6)
    points.append(rotation_matrix * points[-1])

# Decide how large the clock is to be drawn on your canvas. For example, if your canvas is square, you might let the clock's radius be 3/8 of the canvas's width.
# For each point that you computer, multiple the x and z components by this radius, and then move them to the center of your canvas by adding the coordinates of the center point.
size = 400
c = Canvas(size, size)

radius = (3 / 8) * size

for p in points:
    x = radius * p.x + size / 2
    z = radius * p.z + size / 2
    c.write_pixel(round(x), round(z), Color(0, 1, 0))

with open("test.ppm", "w") as f:
    f.write(c.to_ppm(True))
