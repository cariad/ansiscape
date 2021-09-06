from pytest import mark

from ansiscape import InterpretationDict, interpret
from ansiscape.enums import (
    BlinkSpeed,
    Color,
    FontFace,
    Frame,
    Ideogram,
    Intensity,
    Underline,
    VerticalPosition,
)


@mark.parametrize(
    "code, expect",
    [
        (
            "",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "-1",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "-1;73",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "0",
            InterpretationDict(
                blackletter=False,
                blink_speed=BlinkSpeed.NONE,
                conceal=False,
                font_face=FontFace.DEFAULT,
                foreground_color=Color.DEFAULT,
                frame=Frame.NONE,
                ideogram=Ideogram.NONE,
                intensity=Intensity.NORMAL,
                invert=False,
                italic=False,
                overline=False,
                proportional_spacing=False,
                strike=False,
                underline=Underline.NONE,
                vertical_position=VerticalPosition.NONE,
            ),
        ),
        (
            "1",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=Intensity.BOLD,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "2",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=Intensity.DIM,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "3",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=True,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "4",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=Underline.SINGLE,
                vertical_position=None,
            ),
        ),
        (
            "5",
            InterpretationDict(
                blackletter=None,
                blink_speed=BlinkSpeed.SLOW,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "6",
            InterpretationDict(
                blackletter=None,
                blink_speed=BlinkSpeed.FAST,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "7",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=True,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "8",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=True,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "9",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=True,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "10",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=FontFace.DEFAULT,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "11",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=FontFace.ALTERNATIVE_0,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "12",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=FontFace.ALTERNATIVE_1,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "13",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=FontFace.ALTERNATIVE_2,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "14",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=FontFace.ALTERNATIVE_3,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "15",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=FontFace.ALTERNATIVE_4,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "16",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=FontFace.ALTERNATIVE_5,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "17",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=FontFace.ALTERNATIVE_6,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "18",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=FontFace.ALTERNATIVE_7,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "19",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=FontFace.ALTERNATIVE_8,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "20",
            InterpretationDict(
                blackletter=True,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "21",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=Underline.DOUBLE,
                vertical_position=None,
            ),
        ),
        (
            "23",
            InterpretationDict(
                blackletter=False,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=False,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "24",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=Underline.NONE,
                vertical_position=None,
            ),
        ),
        (
            "25",
            InterpretationDict(
                blackletter=None,
                blink_speed=BlinkSpeed.NONE,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "26",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=True,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "27",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=False,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "28",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=False,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "29",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=False,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "30",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.BLACK,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "31",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.RED,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "32",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.GREEN,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "33",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.YELLOW,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "34",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.BLUE,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "35",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.MAGENTA,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "36",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.CYAN,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "37",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.WHITE,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "38;5;0",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.BLACK,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "38;5;1",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.RED,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "38;5;2",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.GREEN,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "38;5;3",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.YELLOW,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "38;5;4",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.BLUE,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "38;5;5",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.MAGENTA,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "38;5;6",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.CYAN,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "38;5;7",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=Color.WHITE,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "50",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=False,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "51",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=Frame.FRAMED,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "52",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=Frame.ENCIRCLED,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "53",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=True,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "54",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=Frame.NONE,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "55",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=False,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "60",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=Ideogram.LINE_UNDER_OR_RIGHT,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "61",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "62",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=Ideogram.LINE_OVER_OR_LEFT,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "63",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=Ideogram.DOUBLE_LINE_OVER_OR_LEFT,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "64",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=Ideogram.STRESS,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=None,
            ),
        ),
        (
            "73",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=VerticalPosition.SUPERSCRIPT,
            ),
        ),
        (
            "74",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=VerticalPosition.SUBSCRIPT,
            ),
        ),
        (
            "75",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=VerticalPosition.NONE,
            ),
        ),
        (
            "73;1",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=Intensity.BOLD,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=VerticalPosition.SUPERSCRIPT,
            ),
        ),
        (
            "0;73",
            InterpretationDict(
                blackletter=False,
                blink_speed=BlinkSpeed.NONE,
                conceal=False,
                font_face=FontFace.DEFAULT,
                foreground_color=Color.DEFAULT,
                frame=Frame.NONE,
                ideogram=Ideogram.NONE,
                intensity=Intensity.NORMAL,
                invert=False,
                italic=False,
                overline=False,
                proportional_spacing=False,
                strike=False,
                underline=Underline.NONE,
                vertical_position=VerticalPosition.SUPERSCRIPT,
            ),
        ),
        (
            "73;74",
            InterpretationDict(
                blackletter=None,
                blink_speed=None,
                conceal=None,
                font_face=None,
                foreground_color=None,
                frame=None,
                ideogram=None,
                intensity=None,
                invert=None,
                italic=None,
                overline=None,
                proportional_spacing=None,
                strike=None,
                underline=None,
                vertical_position=VerticalPosition.SUBSCRIPT,
            ),
        ),
    ],
)
def test_interpret(code: str, expect: InterpretationDict) -> None:
    assert interpret(code) == expect
