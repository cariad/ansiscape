from functools import cached_property
from math import floor
from typing import Dict, List, Tuple

from ansiscape.enums import (
    ColorScheme,
    InterpretationKey,
    NamedColor,
    SelectGraphicRendition,
)
from ansiscape.exceptions import AttributeError
from ansiscape.interpreter import Interpreter
from ansiscape.types import RGB, Attributes, Color, SequencerResult


class ColorInterpreter(Interpreter[Color]):
    """
    Handles interpreration and translation of colour values.

    Arguments:
        key:    Key of `InterpretationDict` that this interpreter handles

        lookup: Dictionary of Select Graphic Rendition codes and known colours
                to return for each

        rgb:    Select Graphic Rendition code that represents RGB colour
    """

    def __init__(
        self,
        key: InterpretationKey,
        lookup: Dict[SelectGraphicRendition, Color],
        rgb: SelectGraphicRendition,
    ) -> None:
        super().__init__(key=key, lookup=lookup)
        self.rgb = rgb

    def from_extended_attributes(self, attrs: Attributes) -> Tuple[Color, int]:
        """
        Interprets a complex sequence of attributes.

        Returns the interpreted value and the count of attributes claimed.
        """

        scheme = ColorScheme(attrs[0])

        if scheme == ColorScheme.IMPLEMENTATION_DEFINED:
            raise AttributeError("ansiscape has no custom color scheme", attrs)

        if scheme == ColorScheme.TRANSPARENT:
            return (0.0, 0.0, 0.0, 0), 1

        if scheme == ColorScheme.RGB:
            # 24-bit RGB descriptors can contain attributes that we don't
            # support. We'll play cautious and assume that the entire sequence
            # is ours for the plucking, and no other interpreters will get a
            # look-in after us.
            tfb = ColorInterpreter.get_24_bit_rgb(attrs[1:])
            return (tfb[0], tfb[1], tfb[2], 1), len(attrs)

        if scheme == ColorScheme.CMY:
            raise AttributeError("Cyan-Magenta-Yellow not supported", attrs)

        if scheme == ColorScheme.CMYB:
            raise AttributeError("Cyan-Magenta-Yellow-Black not supported", attrs)

        if 0 <= attrs[1] <= 15:
            return NamedColor(attrs[1]), 2

        if 16 <= attrs[1] <= 231:
            eight_bit_color = ColorInterpreter.get_8_bit_rgb_color(attrs[1])
        else:
            eight_bit_color = ColorInterpreter.get_8_bit_rgb_grey(attrs[1])

        return (eight_bit_color[0], eight_bit_color[1], eight_bit_color[2], 1), 2

    @staticmethod
    def get_8_bit_rgb_color(attr: int) -> RGB:
        """
        Converts attribute to an 8-bit colour.

        `attr` is taken from the third attribute in, for example, "38;5;<code>m".
        """

        for r in range(0, 6):
            for g in range(0, 6):
                for b in range(0, 6):
                    if 16 + 36 * r + 6 * g + b == attr:
                        return ((r * 51) / 255, (g * 51) / 255, (b * 51) / 255)

        raise AttributeError("unexpected 8-bit RGB color sequence", attr)

    @staticmethod
    def get_8_bit_rgb_grey(attr: int) -> RGB:
        """
        Converts an attribute to a shade of grey.

        Note that 232 is intentionally not black (use "?;5;16" instead) and 255
        is intentionally not white (use "?;5;231" instead). Duplicating the
        ability to generate those colours reduces the variety of grays that can
        fit between 232-255.
        """

        if not 232 <= attr <= 255:
            raise AttributeError("invalid 8-bit RGB grey sequence", attr)
        grey = (attr - 231) * (1 / 25)
        return (grey, grey, grey)

    @staticmethod
    def get_24_bit_rgb(attrs: Attributes) -> RGB:
        """
        Attempts to interpret a 24-bit RGB colour from a sequence of attributes.

        The attributes are typically the source sequence from the third attribute
        onwards. For example, for the sequence `"38;2;1;2;3..."`, pass
        `[ 1, 2, 3, ... ]`.
        """

        if not attrs:
            # Weirdly, all the attributes for a 24-bit colour are optional. This
            # is a valid non-colour but we're not going to handle it, only for
            # the simplicity of passing None around.
            raise AttributeError("non-colors are not supported", attrs)

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

    @cached_property
    def supported_codes(self) -> List[int]:
        """
        Gets the Select Graphic Rendition codes that this interpreter handles.
        """
        return [*super().supported_codes, self.rgb.value]

    def to_extended_attributes(self, value: Color) -> SequencerResult:
        """Interprets a colour to a complex sequence of attributes."""

        if isinstance(value, NamedColor):
            return SequencerResult(
                attributes=[
                    self.rgb.value,
                    ColorScheme.EIGHT_BIT.value,
                    value.value,
                ],
            )

        if isinstance(value, tuple):
            return SequencerResult(
                attributes=[
                    self.rgb.value,
                    ColorScheme.RGB.value,
                    floor(value[0] * 255),
                    floor(value[1] * 255),
                    floor(value[2] * 255),
                ],
                must_isolate=True,
            )

        # This shouldn't be possible. Only NamedColors and tuples (RGBA) are
        # expected down here.
        raise NotImplementedError()
