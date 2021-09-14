from typing import Any, Dict, List

from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.types import Color, InterpreterProtocol

interpreters: Dict[str, InterpreterProtocol[Any]] = {}
for_sgr: Dict[SelectGraphicRendition, List[InterpreterProtocol[Any]]] = {}


def register_interpreter(interpreter: InterpreterProtocol[Any]) -> None:
    interpreters[interpreter.key] = interpreter
    for sgr in interpreter.supported_codes:
        if sgr not in for_sgr:
            for_sgr[sgr] = []
        for_sgr[sgr].append(interpreter)


def get_interpreter(key: str) -> InterpreterProtocol[Any]:
    return interpreters[key]


def get_color_interpreter(key: InterpretationKey) -> InterpreterProtocol[Color]:
    return interpreters[key.value]


def get_interpreters_for_sgr(
    sgr: SelectGraphicRendition,
) -> List[InterpreterProtocol[Any]]:
    if sgr not in for_sgr:
        raise ValueError(f"no interpreter for {sgr.name}: {for_sgr}")
    return for_sgr[sgr]


def get_interpreter_for_sgr(sgr: SelectGraphicRendition) -> InterpreterProtocol[Any]:
    if sgr not in for_sgr:
        raise ValueError(f"no interpreter for {sgr.name}: {for_sgr}")
    if len(for_sgr[sgr]) != 1:
        raise ValueError(
            f"expected one interpreter for {sgr.name} but found {len(for_sgr[sgr])}"
        )
    return for_sgr[sgr][0]
