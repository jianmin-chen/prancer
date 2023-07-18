from math import pi
from canvas import Color
from camera import Camera
from lights import PointLight
from material import Material
from sphere import Sphere
from transformations import scaling, translation, rotation_y, rotation_x, view_transform
from tuple import point, vector
from world import World

floor = Sphere()
floor.transform = scaling(10, 0.01, 10)
floor.material = Material()
floor.material.color = Color(1, 0.9, 0.9)
floor.material.specular = 0

left_wall = Sphere()
left_wall.transform = (
    translation(0, 0, 5)
    * rotation_y(-pi / 4)
    * rotation_x(pi / 2)
    * scaling(10, 0.01, 10)
)
left_wall.material = floor.material

right_wall = Sphere()
right_wall.transform = (
    translation(0, 0, 5)
    * rotation_y(pi / 4)
    * rotation_x(pi / 2)
    * scaling(10, 0.01, 10)
)
right_wall.material = floor.material

middle = Sphere()
middle.transform = translation(-0.5, 1, 0.5)
middle.material = Material()
middle.material.color = Color(0.1, 1, 0.5)
middle.material.diffuse = 0.7
middle.material.specular = 0.3

right = Sphere()
right.transform = translation(1.5, 0.5, -0.5) * scaling(0.5, 0.5, 0.5)
right.material = Material(Color(0.5, 1, 0.1), 0.1, 0.7, 0.3)

left = Sphere()
left.transform = translation(-1.5, 0.33, -0.75) * scaling(0.33, 0.33, 0.33)
left.material = Material(Color(1, 0.8, 0.1), 0.1, 0.7, 0.3)

world = World(
    [floor, left_wall, right_wall, left, middle, right],
    PointLight(point(-10, 10, -10), Color(1, 1, 1)),
)

# 2:1 ratio
camera = Camera(2560, 1600, pi / 3)
camera.transform = view_transform(point(0, 1.5, -5), point(0, 1, 0), vector(0, 1, 0))

canvas = camera.render(world)

with open("test.ppm", "w") as f:
    f.write(canvas.to_ppm())
