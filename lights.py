from canvas import Color
from tuple import Tuple


class PointLight:
    def __init__(self, position: Tuple, intensity: Color):
        self.position = position
        self.intensity = intensity
