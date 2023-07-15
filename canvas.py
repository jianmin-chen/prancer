from tuple import Color
from utils import interpolate


class Canvas:
    def __init__(self, width: int, height: int, fill: Color = Color(0, 0, 0)):
        self.width = width
        self.height = height
        self.canvas = [fill for pixel in range(width * height)]

    def write_pixel(self, x: int, y: int, color: Color) -> None:
        """
        Writes pixels to canvas.

            Parameters:
                x (int)
                y (int)

            Returns:
                None
        """

        self.canvas[y * self.width + x] = color

    def pixel_at(self, x: int, y: int) -> Color:
        """
        Returns pixel at (x, y).

            Parameters:
                x (int)
                y (int)

            Returns:
                pixel (Color)
        """

        pixel = self.canvas[y * self.width + x]
        return pixel

    def to_ppm(self, as_str: bool = True) -> str:
        """
        Converts canvas to PPM file format.

            Parameters:
                as_str (bool): True if returning as string, False if returning as array

            Returns:
                ppm (list)
        """

        ppm = ["P3", f"{self.width} {self.height}", "255"]
        for y in range(self.height):
            row = []
            for x in range(self.width):
                pixel = self.pixel_at(x, y)
                row.extend(
                    [
                        str(round(interpolate(pixel.red, 0, 255))),
                        str(round(interpolate(pixel.green, 0, 255))),
                        str(round(interpolate(pixel.blue, 0, 255))),
                    ]
                )
            rrepr = " ".join(row)
            if len(rrepr) > 70:
                # Trim and add two lines
                trim = 69
                while rrepr[trim] != " ":
                    trim -= 1
                ppm.extend([rrepr[:trim].strip(), rrepr[trim:].strip()])
            else:
                ppm.append(rrepr)
        ppm.append("\n")
        if as_str:
            return "\n".join(ppm)
        return ppm

    def __repr__(self):
        return f"{str(self.canvas)}"
