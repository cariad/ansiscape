from pytest import fixture

from ansiscape import InterpretationDict


@fixture
def interpretation() -> InterpretationDict:
    return InterpretationDict(intensity=None, vertical_position=None)
