from typing import List

from pytest import mark

from ansiscape.enums import Intensity
from ansiscape.interpreters import IntensityInterpreter, InterpretationDict


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([1], 1),
        ([2], 1),
        ([3], 0),
        ([21], 0),
        ([22], 1),
        ([23], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert IntensityInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], InterpretationDict(intensity=Intensity.NORMAL, vertical_position=None)),
        ([1], InterpretationDict(intensity=Intensity.BOLD, vertical_position=None)),
        ([2], InterpretationDict(intensity=Intensity.DIM, vertical_position=None)),
        ([22], InterpretationDict(intensity=Intensity.NORMAL, vertical_position=None)),
    ],
)
def test_update(
    code: List[int],
    expect: InterpretationDict,
    interpretation: InterpretationDict,
) -> None:
    IntensityInterpreter().update(code, interpretation)
    assert interpretation == expect
