from abc import ABC, abstractmethod
from typing import List

from ansiscape.interpreters.interpretation_dict import InterpretationDict


class Interpreter(ABC):
    """
    Base implementation for a class that can recognise and interpret specific
    ANSI escape codes.
    """

    @abstractmethod
    def claim(self, code: List[int]) -> int:
        """
        Returns the quantity of attributes at the start of the code that this
        interpreter wishes to claim.
        """

    @abstractmethod
    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the claimed ANSI escape code."""
