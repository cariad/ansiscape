from typing import Any, Dict, List

from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.types import Color, Interpreter

interpreters: Dict[InterpretationKey, Interpreter[Any]] = {}
for_sgr: Dict[SelectGraphicRendition, List[Interpreter[Any]]] = {}


def register_interpreter(interpreter: Interpreter[Any]) -> None:
    print(f"Registering interpreter: {interpreter}")
    interpreters[interpreter.key] = interpreter
    for sgr in interpreter.supported_codes:
        if sgr not in for_sgr:
            for_sgr[sgr] = []
        for_sgr[sgr].append(interpreter)


def get_interpreter(key: InterpretationKey) -> Interpreter[Any]:
    return interpreters[key]


def get_color_interpreter(key: InterpretationKey) -> Interpreter[Color]:
    return interpreters[key]


def get_interpreter_for_sgr(sgr: SelectGraphicRendition) -> Interpreter[Any]:
    if sgr not in for_sgr:
        raise ValueError(f"no interpreter for {sgr.name}")
    if len(for_sgr[sgr]) != 1:
        raise ValueError(
            f"expected one interpreter for {sgr.name} but found {len(for_sgr[sgr])}"
        )
    return for_sgr[sgr][0]
