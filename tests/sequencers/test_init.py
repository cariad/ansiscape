from typing import List, Union

from pytest import mark

from ansiscape.enums import InterpretationSpecial, StandardColor, Weight
from ansiscape.enums.blink import Blink
from ansiscape.enums.calligraphy import Calligraphy
from ansiscape.enums.font import Font
from ansiscape.enums.frame import Frame
from ansiscape.enums.ideogram import Ideogram
from ansiscape.enums.underline import Underline
from ansiscape.sequencers import to_string
from ansiscape.types import InterpretationDict


@mark.parametrize(
    "args, expect",
    [
        (
            [
                "This is ",
                InterpretationDict(background=StandardColor.RED),
                "red",
                InterpretationDict(background=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[48;5;1mred\033[49m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(blink=Blink.SLOW),
                "blinking",
                InterpretationDict(blink=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[5mblinking\033[25m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(calligraphy=Calligraphy.ITALIC),
                "italic",
                InterpretationDict(calligraphy=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[3mitalic\033[23m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(conceal=True),
                "concealed",
                InterpretationDict(conceal=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[8mconcealed\033[28m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(font=Font.ALT_0),
                "alternate font 0",
                InterpretationDict(font=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[11malternate font 0\033[10m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(foreground=StandardColor.CYAN),
                "cyan",
                InterpretationDict(foreground=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[38;5;6mcyan\033[39m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(frame=Frame.FRAMED),
                "framed",
                InterpretationDict(frame=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[51mframed\033[54m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(ideogram=Ideogram.STRESS),
                "stressed",
                InterpretationDict(ideogram=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[64mstressed\033[65m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(invert=True),
                "inverted",
                InterpretationDict(invert=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[7minverted\033[27m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(overline=True),
                "overlined",
                InterpretationDict(overline=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[53moverlined\033[55m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(proportional_spacing=True),
                "spaced proportionally",
                InterpretationDict(proportional_spacing=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[26mspaced proportionally\033[50m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(strike=True),
                "struck",
                InterpretationDict(strike=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[9mstruck\033[29m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(underline=Underline.SINGLE),
                "underlined",
                InterpretationDict(underline=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[4munderlined\033[24m.",
        ),
        (
            [
                "This is ",
                InterpretationDict(weight=Weight.HEAVY),
                "heavy",
                InterpretationDict(weight=InterpretationSpecial.REVERT),
                ".",
            ],
            "This is \033[1mheavy\033[22m.",
        ),
        (
            [
                "Here's some ",
                InterpretationDict(foreground=StandardColor.GREEN),
                "green text with a ",
                InterpretationDict(foreground=StandardColor.YELLOW),
                "yellow highlight",
                InterpretationDict(foreground=InterpretationSpecial.REVERT),
                " inside",
                InterpretationDict(foreground=InterpretationSpecial.REVERT),
                "!",
            ],
            "Here's some \033[38;5;2mgreen text with a \033[38;5;3myellow highlight\033[38;5;2m inside\033[39m!",
        ),
        (
            [
                "It's ",
                InterpretationDict(foreground=StandardColor.GREEN),
                "green now and ",
                InterpretationDict(weight=Weight.HEAVY),
                "heavy now and ",
                InterpretationDict(foreground=StandardColor.YELLOW),
                "yellow now and ",
                InterpretationDict(foreground=InterpretationSpecial.REVERT),
                "no longer yellow and ",
                InterpretationDict(weight=InterpretationSpecial.REVERT),
                "no longer bold and ",
                InterpretationDict(foreground=InterpretationSpecial.REVERT),
                "no longer green.",
            ],
            "It's \033[38;5;2mgreen now and \033[1mheavy now and \033[38;5;3myellow now and \033[38;5;2mno longer yellow and \033[22mno longer bold and \033[39mno longer green.",
        ),
        (
            [
                "It's ",
                InterpretationDict(foreground=StandardColor.GREEN),
                "green now and ",
                InterpretationDict(weight=Weight.HEAVY),
                "heavy now and ",
                InterpretationDict(foreground=StandardColor.YELLOW),
                "yellow now and ",
                InterpretationDict(weight=InterpretationSpecial.REVERT),
                "no longer bold and ",
                InterpretationDict(foreground=InterpretationSpecial.REVERT),
                "no longer yellow and ",
                InterpretationDict(foreground=InterpretationSpecial.REVERT),
                "no longer green.",
            ],
            "It's \033[38;5;2mgreen now and \033[1mheavy now and \033[38;5;3myellow now and \033[22mno longer bold and \033[38;5;2mno longer yellow and \033[39mno longer green.",
        ),
    ],
)
def test_to_string(args: List[Union[str, InterpretationDict]], expect: str) -> None:
    assert to_string(*args) == expect
