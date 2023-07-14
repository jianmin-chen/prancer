from tuple import Tuple, point, vector, normalize


class Projectile:
    def __init__(self, position: Tuple, velocity: Tuple):
        self.position = position
        self.velocity = velocity

    def __repr__(self) -> str:
        return f"({self.position.x}, {self.position.y}, {self.position.z})"


class Environment:
    def __init__(self, gravity: Tuple, wind: Tuple):
        self.gravity = gravity
        self.wind = wind


def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)


proj = Projectile(point(0, 1, 0), normalize(vector(1, 1, 0)))
env = Environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))

while proj.position.y > 0:
    print(f"Position of projectile: {proj}")
    proj = tick(env, proj)
