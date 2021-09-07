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
