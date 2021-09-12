from typing import List, Optional, Union

from ansiscape.enums import (
    Calligraphy,
    Font,
    Frame,
    Ideogram,
    InterpretationKey,
    InterpretationSpecial,
    Underline,
    Weight,
)
from ansiscape.handlers import get_interpreter
from ansiscape.types import Attributes, Color, InterpretationDict, SequenceProtocol


class Sequence(SequenceProtocol):
    def __init__(
        self,
        *parts: Union[str, SequenceProtocol],
        prefix: Optional[InterpretationDict] = None,
        suffix: Optional[InterpretationDict] = None,
    ) -> None:
        self.prefix = prefix or InterpretationDict()
        self.suffix = suffix or InterpretationDict()
        self.parts = parts

    @property
    def args(self) -> List[Union[str, InterpretationDict]]:
        args: List[Union[str, InterpretationDict]] = [self.prefix]

        for part in self.parts:
            if isinstance(part, str):
                args.append(part)
            else:
                args.extend(part.args)

        args.append(self.suffix)
        return args

    def __str__(self) -> str:
        return self.encode(*self.args)

    def encode(self, *parts: Union[str, InterpretationDict]) -> str:
        """
        Encodes a series of strings and formatting interpretations into a single
        string with embedded escape codes.
        """

        wip = ""
        stack: List[InterpretationDict] = []
        for arg in parts:
            if isinstance(arg, str):
                wip += arg
                continue

            if not arg:
                # Don't add empty dictionaries.
                continue

            stack.append(arg)
            wip += self.encode_escape_sequence(stack)

        return wip

    def encode_escape_sequence(self, stack: List[InterpretationDict]) -> str:
        """
        Encodes the interpretation at the top of the stack into an embeddable escape
        code.

        The lower stack will be read only if the interpration at the top prescribes
        a reversion.
        """

        print("encoding:", stack)

        sequences: List[Attributes] = [[]]
        interpretation = stack[-1]

        for key in InterpretationKey:
            if interpretation.get(key.value, None) is None:
                continue

            # Intentionally send a copy of the stack because inner reversion
            # resolution will pop:
            result = get_interpreter(key).sequence([*stack])

            sequence = [result["sgr"].value]
            if additional := result.get("additional", None):
                sequence.extend(additional)

            if result.get("must_isolate", False):
                sequences.append(sequence)
            else:
                sequences[0].extend(sequence)
        code = "".join([f"\033[{';'.join([str(a) for a in s])}m" for s in sequences])
        print("encode_escape_sequence():", code[1:])
        return code


class ForegroundSequence(Sequence):
    def __init__(self, color: Color, *parts: Union[str, "Sequence"]) -> None:
        super().__init__(
            *parts,
            prefix=InterpretationDict(foreground=color),
            suffix=InterpretationDict(foreground=InterpretationSpecial.REVERT),
        )


class BackgroundSequence(Sequence):
    def __init__(self, color: Color, *parts: Union[str, "Sequence"]) -> None:
        super().__init__(
            *parts,
            prefix=InterpretationDict(background=color),
            suffix=InterpretationDict(background=InterpretationSpecial.REVERT),
        )


class AlternativeFontSequence(Sequence):
    def __init__(self, font: Font, *parts: Union[str, "Sequence"]) -> None:
        super().__init__(
            *parts,
            prefix=InterpretationDict(font=font),
            suffix=InterpretationDict(font=InterpretationSpecial.REVERT),
        )


class CalligraphySequence(Sequence):
    def __init__(
        self, calligraphy: Calligraphy, *parts: Union[str, "Sequence"]
    ) -> None:
        super().__init__(
            *parts,
            prefix=InterpretationDict(calligraphy=calligraphy),
            suffix=InterpretationDict(calligraphy=InterpretationSpecial.REVERT),
        )


class WeightSequence(Sequence):
    def __init__(self, weight: Weight, *parts: Union[str, "Sequence"]) -> None:
        super().__init__(
            *parts,
            prefix=InterpretationDict(weight=weight),
            suffix=InterpretationDict(weight=InterpretationSpecial.REVERT),
        )


class IdeogramSequence(Sequence):
    def __init__(self, ideogram: Ideogram, *parts: Union[str, "Sequence"]) -> None:
        super().__init__(
            *parts,
            prefix=InterpretationDict(ideogram=ideogram),
            suffix=InterpretationDict(ideogram=InterpretationSpecial.REVERT),
        )


class FrameSequence(Sequence):
    def __init__(self, frame: Frame, *parts: Union[str, "Sequence"]) -> None:
        super().__init__(
            *parts,
            prefix=InterpretationDict(frame=frame),
            suffix=InterpretationDict(frame=InterpretationSpecial.REVERT),
        )


class UnderlineSequence(Sequence):
    def __init__(self, underline: Underline, *parts: Union[str, "Sequence"]) -> None:
        super().__init__(
            *parts,
            prefix=InterpretationDict(underline=underline),
            suffix=InterpretationDict(underline=InterpretationSpecial.REVERT),
        )
