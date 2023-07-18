from __future__ import annotations
from copy import copy
from canvas import Color
from tuple import Tuple


class PointLight:
    def __init__(self, position: Tuple, intensity: Color):
        self.position = position
        self.intensity = intensity

    def __eq__(self, other: PointLight) -> bool:
        return self.position == other.position and self.intensity == other.intensity

    def __copy__(self) -> PointLight:
        return PointLight(copy(self.position), copy(self.intensity))
