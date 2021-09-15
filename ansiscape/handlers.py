from typing import Any, Dict, List

from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.types import Color, InterpreterType

interpreters: Dict[str, InterpreterType[Any]] = {}

# key: Select Graphic Rendition code
for_sgr: Dict[int, List[InterpreterType[Any]]] = {}


def register_interpreter(interpreter: InterpreterType[Any]) -> None:
    interpreters[interpreter.key] = interpreter
    for sgr in interpreter.supported_codes:
        if sgr not in for_sgr:
            for_sgr[sgr] = []
        for_sgr[sgr].append(interpreter)


def get_interpreter(key: str) -> InterpreterType[Any]:
    return interpreters[key]


def get_color_interpreter(key: InterpretationKey) -> InterpreterType[Color]:
    return interpreters[key.value]


def get_interpreter_for_sgr_int(sgr: int) -> InterpreterType[Any]:
    return for_sgr[sgr][0]


def get_interpreter_for_sgr(sgr: SelectGraphicRendition) -> InterpreterType[Any]:
    return get_interpreter_for_sgr_int(sgr.value)
