from typing import Dict, Tuple

from ansiscape.color import get_8_bit_color, get_color_scheme, interpret_24_bit_rgb
from ansiscape.enums import (
    ColorScheme,
    InterpretationKey,
    SelectGraphicRendition,
    StandardColor,
)
from ansiscape.exceptions import AttributeError
from ansiscape.interpreters.dict_value import DictValue
from ansiscape.types import Attributes, Color
from ansiscape.types.sequencer_result import SequencerResult


class ColorValue(DictValue[Color]):
    def __init__(
        self,
        key: InterpretationKey,
        lookup: Dict[SelectGraphicRendition, Color],
        rgb: SelectGraphicRendition,
    ) -> None:
        super().__init__(key, lookup)
        self.rgb = rgb

    def from_extended_attributes(
        self,
        attrs: Attributes,
    ) -> Tuple[Color, int]:
        scheme = get_color_scheme(attrs[0])

        if scheme == ColorScheme.IMPLEMENTATION_DEFINED:
            raise AttributeError("ansiscape has no custom color scheme", attrs)

        if scheme == ColorScheme.TRANSPARENT:
            return (0.0, 0.0, 0.0, 0), 1

        if scheme == ColorScheme.RGB:
            # 24-bit RGB descriptors can contain attributes that we don't
            # support. We'll play cautious and assume that the entire sequence
            # is ours for the plucking, and no other interpreters will get a
            # look-in after us.
            if interpreted_rbg := interpret_24_bit_rgb(attrs[1:]):
                return (
                    interpreted_rbg[0],
                    interpreted_rbg[1],
                    interpreted_rbg[2],
                    1,
                ), len(attrs)
            raise ValueError()

        if scheme == ColorScheme.CMY:
            raise AttributeError("Cyan-Magenta-Yellow not supported", attrs)

        if scheme == ColorScheme.CMYB:
            raise AttributeError("Cyan-Magenta-Yellow-Black not supported", attrs)

        eight_bit_color = get_8_bit_color(attrs[1])
        if isinstance(eight_bit_color, StandardColor):
            return eight_bit_color, 2
        return (eight_bit_color[0], eight_bit_color[1], eight_bit_color[2], 1), 2

    def get_extended_code(self, value: Color) -> SequencerResult:
        if isinstance(value, StandardColor):
            return SequencerResult(
                sgr=self.rgb,
                additional=[ColorScheme.EIGHT_BIT.value, value.value],
            )
        raise NotImplementedError()
