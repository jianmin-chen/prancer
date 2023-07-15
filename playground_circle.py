# Think as if you're trying to cast the shadow of your object onto some wall behind it.
# You cast each ray from some starting point toward some point on the wall that corresponds to a position on your canvas. If the ray intersects the sphere, a shadow is cast, which you'll mark with a colored pixel.
from canvas import Canvas, Color
from ray import Ray, hit
from sphere import Sphere
from tuple import point, normalize
import threading

# Figure out how far your ray's origin is from the sphere. Also, decide where your wall will be. Moving the ray origin closer to the sphere will make the sphere in the drawing larger. Moving it further away will make the sphere smaller. Moving the wall will do similarly.

# Start the ray at z = -5
ray_origin = point(0, 0, -5)

# Put the wall at z = 10
wall_z = 10

# Then decide how large your wall needs to be. Because you're using unit spheres, the maximum y value for the sphere is going to be 1. With that, you can extrapolate between the ray origin and the wall to see how large the wall should be.
# So, with the wall at z = 10, it needs to be at least 6 units across in order to capture the sphere's entire shadow. Give yourself a bit of margin, and call it 7. (Just assume the wall is a square.)
wall_size = 7

size = 400

# Once you know how many pixels fit along each side of the wall, you can divide the wall size by the number of pixels to get the size of a single pixel (in world space units).
pixel_size = wall_size / size

# Then, assuming you're looking directly at the center of the sphere, half of the wall will be to the left of that, and half to the right. Compute that size.
half = wall_size / 2

c = Canvas(size, size)
color = Color(0, 1, 0)
shape = Sphere()


def at_point(x, y):
    world_y = half - pixel_size * y
    world_x = -half + pixel_size * x
    position = point(world_x, world_y, wall_z)
    r = Ray(ray_origin, normalize(position - ray_origin))
    xs = r.intersect(shape)

    if hit(xs):
        c.write_pixel(x, y, color)


for y in range(size):
    for x in range(size):
        print(f"{x}, {y}")
        thread = threading.Thread(target=at_point, args=(x, y), daemon=True)
        thread.start()

with open("test.ppm", "w") as f:
    f.write(c.to_ppm())
