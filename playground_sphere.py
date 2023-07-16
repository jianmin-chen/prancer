from canvas import Canvas, Color
from lights import PointLight
from material import Material, lighting
from ray import Ray, hit
from sphere import Sphere
from tuple import point, normalize
from utils import rgb_scaled

# Start the ray at z = -5
ray_origin = point(0, 0, -5)

# Put the wall at z = 10
wall_z = 10
wall_size = 7

canvas_pixels = 900

pixel_size = wall_size / canvas_pixels

half = wall_size / 2

canvas = Canvas(canvas_pixels, canvas_pixels, Color(*rgb_scaled(255, 127, 80)))

sphere = Sphere()
sphere.material = Material()
sphere.material.color = Color(*rgb_scaled(255, 99, 71))

light_position = point(-10, 10, -10)
light_color = Color(1, 1, 1)
light = PointLight(light_position, light_color)

# For each row of pixels in the canvas
for y in range(canvas_pixels):
    # Compute the world y coordinate(top=+half, bottom=-half)
    world_y = half - pixel_size * y

    # For each pixel in the row
    for x in range(canvas_pixels):
        # Compute the world x coordinate (left=-half, right=half)
        world_x = -half + pixel_size * x

        # Describe the point on the wall that the ray will target
        position = point(world_x, world_y, wall_z)

        ray = Ray(ray_origin, normalize(position - ray_origin))
        xs = ray.intersect(sphere)

        h = hit(xs)
        if h:
            p = ray.position(h.t)
            normal = sphere.normal_at(p)
            eye = -ray.direction

            color = lighting(h.object.material, light, p, eye, normal)

            canvas.write_pixel(x, y, color)

with open("test.ppm", "w") as f:
    f.write(canvas.to_ppm())
