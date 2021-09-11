from math import floor
from typing import Optional

from ansiscape.encoders.sequencer import Sequencer
from ansiscape.enums import ColorScheme, SelectGraphicRendition, StandardColor
from ansiscape.types import Color, SequencerResult


class ColorSequencer(Sequencer[Color]):
    @property
    def default_code(self) -> SelectGraphicRendition:
        """
        Gets the Select Graphic Rendition code that represets the default state.
        """

    @property
    def rgb_code(self) -> SelectGraphicRendition:
        """
        Gets the Select Graphic Rendition code that represets an RGB colour.
        """

    def resolve(self, value: Optional[Color]) -> SequencerResult:
        """Resolves a value into a sequencer result."""

        if isinstance(value, StandardColor):
            return SequencerResult(
                sgr=self.rgb_code,
                additional=[ColorScheme.EIGHT_BIT.value, value.value],
            )

        if isinstance(value, tuple):
            if value[3] == 0:
                return SequencerResult(
                    sgr=self.rgb_code,
                    additional=[ColorScheme.TRANSPARENT.value],
                )

            return SequencerResult(
                sgr=self.rgb_code,
                additional=[
                    ColorScheme.RGB.value,
                    floor(value[0] * 255),
                    floor(value[1] * 255),
                    floor(value[2] * 255),
                ],
                must_isolate=True,
            )

        return SequencerResult(sgr=self.default_code)
