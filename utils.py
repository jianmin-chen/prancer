EPSILON = 0.00001


def equal(a: float, b: float) -> bool:
    """
    Determines if two values are roughly equal.

        Parameters:
            a (float)
            b (float)

        Returns:
            is_equal (bool): True if roughly equal, False otherwise.
    """

    if abs(a - b) < EPSILON:
        return True
    return False


def interpolate(value: float, minimum: float, maximum: float) -> float:
    """
    Scales and clamps a value between a new range.

    Parameters:
        value (float)
        minimum (float)
        maximum (float)

    Returns:
        interpolated (float)
    """

    interpolated = max(minimum, min(maximum, (1 - value) * minimum + value * maximum))
    return interpolated


def rgb_scaled(red, green, blue):
    return (red / 255, green / 255, blue / 255)
