from ansiscape.interpreters import register
from ansiscape.types import InterpretationDict
from ansiscape.version import get_version

register()


__all__ = ["get_version", "InterpretationDict"]
