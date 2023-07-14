from tuple import Color, point, vector, normalize
from canvas import Canvas
from playground_tick import Projectile, Environment

start = point(0, 1, 0)
velocity = normalize(vector(1, 1.8, 0)) * 11.25
p = Projectile(start, velocity)

gravity = vector(0, -0.1, 0)
wind = vector(-0.01, 0, 0)
e = Environment(gravity, wind)

c = Canvas(900, 550)


def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)


while p.position.y > 0:
    p = tick(e, p)
    # -> Write to PPM file!
    if p.position.y >= 0:
        x = p.position.x
        y = 550 - p.position.y
        c.write_pixel(round(x), round(y), Color(0.75, 1, 0.75))


with open("test.ppm", "w") as f:
    f.write(c.to_ppm(True))
