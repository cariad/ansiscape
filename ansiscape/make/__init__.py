from typing import Union

from ansiscape.enums import SelectGraphicRendition


def sequence(code: SelectGraphicRendition) -> str:
    return f"\033[{code.value}m"


def wrap(
    text: str,
    prefix: SelectGraphicRendition,
    suffix: SelectGraphicRendition,
) -> str:
    return f"{sequence(prefix)}{text}{sequence(suffix)}"


def bold(text: str) -> str:
    return wrap(
        text,
        SelectGraphicRendition.WEIGHT_HEAVY,
        SelectGraphicRendition.WEIGHT_NORMAL,
    )


def red(*text: str) -> str:
    return wrap(
        "".join(text),
        SelectGraphicRendition.FOREGROUND_RED,
        SelectGraphicRendition.FOREGROUND_DEFAULT,
    )


def yellow(*text: str) -> str:
    return wrap(
        "".join(text),
        SelectGraphicRendition.FOREGROUND_YELLOW,
        SelectGraphicRendition.FOREGROUND_DEFAULT,
    )


def green(*text: str) -> str:
    return wrap(
        "".join(text),
        SelectGraphicRendition.FOREGROUND_GREEN,
        SelectGraphicRendition.FOREGROUND_DEFAULT,
    )


class WithCodes:
    def __init__(self, *args: Union[str, "WithCodes"]) -> None:
        self.args = args

    def __str__(self) -> str:
        return "".join([str(arg) for arg in self.args])
