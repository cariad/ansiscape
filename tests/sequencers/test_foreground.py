from typing import Optional

from pytest import mark

from ansiscape.enums import (
    ColorSpecial,
    InterpretationKey,
    SelectGraphicRendition,
    StandardColor,
)
from ansiscape.sequencers import ForegroundSequencer
from ansiscape.types.color import Color
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert ForegroundSequencer().key == InterpretationKey.FOREGROUND


@mark.parametrize(
    "color, expect",
    [
        (
            None,
            SequencerResult(sgr=SelectGraphicRendition.FOREGROUND_DEFAULT),
        ),
        (
            ColorSpecial.DEFAULT,
            SequencerResult(sgr=SelectGraphicRendition.FOREGROUND_DEFAULT),
        ),
        (
            StandardColor.BLACK,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 0],
            ),
        ),
        (
            StandardColor.RED,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 1],
            ),
        ),
        (
            StandardColor.GREEN,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 2],
            ),
        ),
        (
            StandardColor.YELLOW,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 3],
            ),
        ),
        (
            StandardColor.BLUE,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 4],
            ),
        ),
        (
            StandardColor.MAGENTA,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 5],
            ),
        ),
        (
            StandardColor.CYAN,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 6],
            ),
        ),
        (
            StandardColor.WHITE,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 7],
            ),
        ),
        (
            StandardColor.BRIGHT_BLACK,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 8],
            ),
        ),
        (
            StandardColor.BRIGHT_RED,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 9],
            ),
        ),
        (
            StandardColor.BRIGHT_GREEN,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 10],
            ),
        ),
        (
            StandardColor.BRIGHT_YELLOW,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 11],
            ),
        ),
        (
            StandardColor.BRIGHT_BLUE,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 12],
            ),
        ),
        (
            StandardColor.BRIGHT_MAGENTA,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 13],
            ),
        ),
        (
            StandardColor.BRIGHT_CYAN,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 14],
            ),
        ),
        (
            StandardColor.BRIGHT_WHITE,
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[5, 15],
            ),
        ),
        # Transparent:
        (
            (0.0, 0.0, 0.0, 0),
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[1],
            ),
        ),
        (
            (1.0, 1.0, 1.0, 0),
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[1],
            ),
        ),
        # RGB:
        (
            (0.0, 0.0, 0.0, 1),
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[2, 0, 0, 0],
                must_isolate=True,
            ),
        ),
        (
            (1.0, 0.0, 0.0, 1),
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[2, 255, 0, 0],
                must_isolate=True,
            ),
        ),
        (
            (0.0, 1.0, 0.0, 1),
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[2, 0, 255, 0],
                must_isolate=True,
            ),
        ),
        (
            (0.0, 0.0, 1.0, 1),
            SequencerResult(
                sgr=SelectGraphicRendition.FOREGROUND_RGB,
                additional=[2, 0, 0, 255],
                must_isolate=True,
            ),
        ),
    ],
)
def test_resolve(color: Optional[Color], expect: SequencerResult) -> None:
    assert ForegroundSequencer().resolve(color) == expect
