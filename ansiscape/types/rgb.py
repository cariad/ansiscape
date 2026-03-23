from typing import NamedTuple

# Represents the red, green and blue (RGB) aspects of a colour. Each component
# is described by a float from 0.0 to 1.0.
class RGB(NamedTuple):
    red: float
    green: float
    blue: float
