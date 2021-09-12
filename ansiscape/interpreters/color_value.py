from typing import Dict, List, Tuple

from ansiscape.enums import (
    ColorScheme,
    InterpretationKey,
    SelectGraphicRendition,
    StandardColor,
)
from ansiscape.exceptions import AttributeError
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.types import RGB, Attributes, Color, SequencerResult


class ColorValue(Interpreter[Color]):
    def __init__(
        self,
        key: InterpretationKey,
        lookup: Dict[SelectGraphicRendition, Color],
        rgb: SelectGraphicRendition,
    ) -> None:
        super().__init__(key, lookup)
        self.rgb = rgb

    @property
    def supported_codes(self) -> List[SelectGraphicRendition]:
        return [*super().supported_codes, self.rgb]

    def from_extended_attributes(self, attrs: Attributes) -> Tuple[Color, int]:
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
            tfb = ColorValue.get_24_bit_rgb(attrs[1:])
            return (tfb[0], tfb[1], tfb[2], 1), len(attrs)

        if scheme == ColorScheme.CMY:
            raise AttributeError("Cyan-Magenta-Yellow not supported", attrs)

        if scheme == ColorScheme.CMYB:
            raise AttributeError("Cyan-Magenta-Yellow-Black not supported", attrs)

        if 0 <= attrs[1] <= 15:
            return StandardColor(attrs[1]), 2

        if 16 <= attrs[1] <= 231:
            eight_bit_color = ColorValue.get_8_bit_rgb_color(attrs[1])
        else:
            eight_bit_color = ColorValue.get_8_bit_rgb_grey(attrs[1])

        return (eight_bit_color[0], eight_bit_color[1], eight_bit_color[2], 1), 2

    def get_extended_code(self, value: Color) -> SequencerResult:
        if isinstance(value, StandardColor):
            return SequencerResult(
                sgr=self.rgb,
                additional=[ColorScheme.EIGHT_BIT.value, value.value],
            )
        raise NotImplementedError()

    @staticmethod
    def get_8_bit_rgb_color(attr: int) -> RGB:
        """
        Converts an ANSI escape code to an 8-bit colour.

        `code` is taken from the third attribute in, for example, "38;5;<code>m".
        """

        if not 16 <= attr <= 232:
            raise AttributeError("invalid 8-bit RGB color sequence", attr)

        for r in range(0, 6):
            for g in range(0, 6):
                for b in range(0, 6):
                    if 16 + 36 * r + 6 * g + b == attr:
                        return ((r * 51) / 255, (g * 51) / 255, (b * 51) / 255)

        raise AttributeError("unexpected 8-bit RGB color sequence", attr)

    @staticmethod
    def get_8_bit_rgb_grey(attr: int) -> RGB:
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
