from typing import NamedTuple

# Represents the red, green, blue and alpha aspects of a colour. Each component
# is described by a float from 0.0 to 1.0.
class RGBA(NamedTuple):
    red: float
    green: float
    blue: float
    alpha: float
