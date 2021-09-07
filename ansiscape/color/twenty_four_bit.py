from typing import List, Optional

from ansiscape.exceptions import AttributeError
from ansiscape.types import RGB


def interpret_24_bit_rgb(attrs: List[int]) -> Optional[RGB]:
    """
    Attempts to interpret a 24-bit RGB colour from a sequence of attributes.

    The attributes are typically the source sequence from the third attribute
    onwards. For example, for the sequence `"38;2;1;2;3..."`, pass
    `[ 1, 2, 3, ... ]`.
    """

    if not attrs:
        # Weirdly, all the attributes for a 24-bit colour are optional. This is
        # a valid non-colour.
        return None

    if len(attrs) == 1:
        # Assumption: "...;<colour-space>"
        # Looks like this prescribes a colour space without the optional red,
        # green and blue components. We don't support colour spaces.
        raise AttributeError("color spaces are not supported", attrs)

    if len(attrs) == 2:
        # Assumption: ?
        # This doesn't look like any valid sequence.
        raise AttributeError("unexpected sequence", attrs)

    if len(attrs) == 3:
        # Assumption: "...;<r>;<g>;<b>"
        return (attrs[0] / 255, attrs[1] / 255, attrs[2] / 255)

    # Assumption: "...;<colour-space>;<r>;<g>;<b>;<more-unsupported>;..."
    # We don't support colour spaces.
    raise AttributeError("color spaces are not supported", attrs)
