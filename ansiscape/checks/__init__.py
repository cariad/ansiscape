from os import fstat


def should_emit_codes() -> bool:
    """Returns `True` if ANSI escape codes should be emitted."""

    return fstat(0) == fstat(1)
