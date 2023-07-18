from copy import copy
from canvas import Canvas
from math import tan
from matrix import identity_matrix, inverse
from ray import Ray
from tuple import point, normalize
from world import World


class Camera:
    def __init__(self, hsize: int, vsize: int, field_of_view: float):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = copy(identity_matrix)

        half_view = tan(self.field_of_view / 2)
        aspect = self.hsize / self.vsize
        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view

        self.pixel_size = (self.half_width * 2) / self.hsize

    def ray_for_pixel(self, x: int, y: int) -> Ray:
        """
        Returns a new ray that starts at the camera and passes through the indicated (x, y) pixel on the canvas.

            Parameters:
                x (int)
                y (int)

            Returns:
                ray (Ray)
        """

        xoffset = (x + 0.5) * self.pixel_size
        yoffset = (y + 0.5) * self.pixel_size

        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset

        pixel = inverse(self.transform) * point(world_x, world_y, -1)
        origin = inverse(self.transform) * point(0, 0, 0)
        direction = normalize(pixel - origin)

        return Ray(origin, direction)

    def render(self, world: World) -> Canvas:
        """
        Render an image of the given world.

            Parameters:
                world (World)

            Returns:
                image (Canvas)
        """

        image = Canvas(self.hsize, self.vsize)

        for y in range(self.vsize):
            for x in range(self.hsize):
                ray = self.ray_for_pixel(x, y)
                color = world.color_at(ray)
                image.write_pixel(x, y, color)

        return image
