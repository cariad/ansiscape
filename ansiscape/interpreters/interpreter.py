from abc import ABC, abstractmethod
from typing import Dict, Generic, List, TypeVar

from ansiscape.interpreters.interpretation_dict import InterpretationDict

TInterpretable = TypeVar("TInterpretable")


class Interpreter(ABC, Generic[TInterpretable]):
    """
    Base implementation for a class that can recognise and interpret specific
    ANSI escape codes.
    """

    def __init__(self, attributes: Dict[int, TInterpretable]) -> None:
        super().__init__()
        self.attributes = attributes

    @abstractmethod
    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        If the attribute at the start of the list isn't recognised then it's
        acceptable to make no changes at all.

        The function may read more than one attribute, but must read from the
        start and may not skip.

        Returns the count of attributes that were interpreted.
        """
