from typing import Dict, Generic, List, TypeVar

from ansiscape.interpreters.interpreter import Interpreter

TInterpretable = TypeVar("TInterpretable")


class GenericLookupInterpreter(Interpreter, Generic[TInterpretable]):
    """
    Recognises and interprets ANSI escape codes from a simple generic lookup.
    """

    def __init__(self, attributes: Dict[int, TInterpretable]) -> None:
        super().__init__()
        self.attributes = attributes

    def claim(self, code: List[int]) -> int:
        """
        Returns the quantity of attributes at the start of the code that this
        interpreter wishes to claim.
        """

        return 1 if code[0] in self.attributes else 0
