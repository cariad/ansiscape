from pytest import fixture

from ansiscape import InterpretationDict, make_interpretation


@fixture
def interpretation() -> InterpretationDict:
    return make_interpretation()
