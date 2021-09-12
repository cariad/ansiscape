from abc import ABC, abstractmethod, abstractproperty
from typing import Generic, List, Union

from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.types.attributes import Attributes
from ansiscape.types.color import Color
from ansiscape.types.interpretation_dict import InterpretationDict
from ansiscape.types.interpretation_value import TInterpretationValue
from ansiscape.types.rgb import RGB
from ansiscape.types.rgba import RGBA
from ansiscape.types.sequencer_result import SequencerResult


class BaseSequence(ABC):
    @abstractproperty
    def args(self) -> List[Union[str, InterpretationDict]]:
        ...


class Interpreter(ABC, Generic[TInterpretationValue]):
    @abstractproperty
    def key(self) -> InterpretationKey:
        ...

    @abstractproperty
    def supported_codes(self) -> List[SelectGraphicRendition]:
        ...

    @abstractmethod
    def sequence(self, stack: List[InterpretationDict]) -> SequencerResult:
        ...

    @abstractmethod
    def to_code(self, value: TInterpretationValue) -> SequencerResult:
        ...

    def make_sequence(
        self,
        value: TInterpretationValue,
        *parts: Union[str, BaseSequence],
    ) -> BaseSequence:
        ...

    def make_sequence_from_attributes(
        self,
        attrs: Attributes,
        *parts: Union[str, BaseSequence],
    ) -> BaseSequence:
        ...


# Generic[TInterpretationValue]

# EncoderGetter = Callable[[InterpretationKey], Encoder[Any]]


__all__ = [
    "Attributes",
    "Color",
    "InterpretationDict",
    "RGB",
    "RGBA",
    "SequencerResult",
    "TInterpretationValue",
]
