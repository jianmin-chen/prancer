from __future__ import annotations
from canvas import Color
from lights import PointLight
from tuple import Tuple, dot, normalize, reflect


class Material:
    def __init__(
        self,
        color: Color = Color(1, 1, 1),
        ambient: float = 0.1,
        diffuse: float = 0.9,
        specular: float = 0.9,
        shininess: float = 200,
    ):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def __eq__(self, other: Material) -> bool:
        return (
            self.color == other.color
            and self.ambient == other.ambient
            and self.diffuse == other.diffuse
            and self.specular == other.specular
            and self.shininess == other.shininess
        )


def lighting(
    material: Material, light: PointLight, point: Tuple, eyev: Tuple, normalv: Tuple
) -> Tuple:
    """
    Shading for objects.

        Parameters:
            material (Material)
            light (Color)
            point (Tuple): Tuple with type=point
            eyev (Tuple): Tuple with type=vector
            normalv (Tuple): Tuple with type=vector

        Returns:
            intensity (float)
    """

    # Combine the surface color with the light's color/intensity
    effective_color = material.color * light.intensity

    # Find the direction to the light source
    lightv = normalize(light.position - point)

    # Compute the ambient contribution
    ambient = effective_color * material.ambient

    # light_dot_normal represents the cosine of the angle between the light vector and the normal vector. A negative number means the light is on the other side of the surface.
    light_dot_normal = dot(lightv, normalv)
    if light_dot_normal < 0:
        diffuse = Color(0, 0, 0)
        specular = Color(0, 0, 0)
    else:
        # Compute the diffuse contribution
        diffuse = effective_color * material.diffuse * light_dot_normal

        # reflect_dot_eye represents the cosine of the angle between the reflection vector and the eye vector. A negative number means the light reflects away from the eye.
        reflectv = reflect(-lightv, normalv)
        reflect_dot_eye = dot(reflectv, eyev)

        if reflect_dot_eye <= 0:
            specular = Color(0, 0, 0)
        else:
            # Compute the specular contribution
            factor = reflect_dot_eye**material.shininess
            specular = light.intensity * material.specular * factor

    # Add the three contributions together to get the final shading
    return ambient + diffuse + specular
