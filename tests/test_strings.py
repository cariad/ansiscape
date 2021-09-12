from pytest import mark

from ansiscape import strings as s
from ansiscape.sequence import Sequence


@mark.parametrize(
    "sequence, expect",
    [
        (s.alternative_font_0("foo"), "\033[11mfoo\033[10m"),
        (s.alternative_font_1("foo"), "\033[12mfoo\033[10m"),
        (s.alternative_font_2("foo"), "\033[13mfoo\033[10m"),
        (s.alternative_font_3("foo"), "\033[14mfoo\033[10m"),
        (s.alternative_font_4("foo"), "\033[15mfoo\033[10m"),
        (s.alternative_font_5("foo"), "\033[16mfoo\033[10m"),
        (s.alternative_font_6("foo"), "\033[17mfoo\033[10m"),
        (s.alternative_font_7("foo"), "\033[18mfoo\033[10m"),
        (s.alternative_font_8("foo"), "\033[19mfoo\033[10m"),
        (s.black("foo"), "\033[30mfoo\033[39m"),
        (s.black_background("foo"), "\033[40mfoo\033[49m"),
        (s.blackletter("foo"), "\033[20mfoo\033[23m"),
        (s.blue("foo"), "\033[34mfoo\033[39m"),
        (s.blue_background("foo"), "\033[44mfoo\033[49m"),
        (s.bright_black("foo"), "\033[38;5;8mfoo\033[39m"),
        (s.bright_black_background("foo"), "\033[48;5;8mfoo\033[49m"),
        (s.bright_blue("foo"), "\033[38;5;12mfoo\033[39m"),
        (s.bright_blue_background("foo"), "\033[48;5;12mfoo\033[49m"),
        (s.bright_cyan("foo"), "\033[38;5;14mfoo\033[39m"),
        (s.bright_cyan_background("foo"), "\033[48;5;14mfoo\033[49m"),
        (s.bright_green("foo"), "\033[38;5;10mfoo\033[39m"),
        (s.bright_green_background("foo"), "\033[48;5;10mfoo\033[49m"),
        (s.bright_magenta("foo"), "\033[38;5;13mfoo\033[39m"),
        (s.bright_magenta_background("foo"), "\033[48;5;13mfoo\033[49m"),
        (s.bright_red("foo"), "\033[38;5;9mfoo\033[39m"),
        (s.bright_red_background("foo"), "\033[48;5;9mfoo\033[49m"),
        (s.bright_white("foo"), "\033[38;5;15mfoo\033[39m"),
        (s.bright_white_background("foo"), "\033[48;5;15mfoo\033[49m"),
        (s.bright_yellow("foo"), "\033[38;5;11mfoo\033[39m"),
        (s.bright_yellow_background("foo"), "\033[48;5;11mfoo\033[49m"),
        (s.circle("foo"), "\033[52mfoo\033[54m"),
        (s.conceal("foo"), "\033[8mfoo\033[28m"),
        (s.cyan("foo"), "\033[36mfoo\033[39m"),
        (s.cyan_background("foo"), "\033[46mfoo\033[49m"),
        (s.double_line_over_or_left("foo"), "\033[63mfoo\033[65m"),
        (s.double_line_under_or_right("foo"), "\033[61mfoo\033[65m"),
        (s.double_underline("foo"), "\033[21mfoo\033[24m"),
        (s.fast_blink("foo"), "\033[6mfoo\033[25m"),
        (s.frame("foo"), "\033[51mfoo\033[54m"),
        (s.green("foo"), "\033[32mfoo\033[39m"),
        (s.green_background("foo"), "\033[42mfoo\033[49m"),
        (s.heavy("foo"), "\033[1mfoo\033[22m"),
        (s.invert("foo"), "\033[7mfoo\033[27m"),
        (s.italic("foo"), "\033[3mfoo\033[23m"),
        (s.light("foo"), "\033[2mfoo\033[22m"),
        (s.magenta("foo"), "\033[35mfoo\033[39m"),
        (s.magenta_background("foo"), "\033[45mfoo\033[49m"),
        (s.overline("foo"), "\033[53mfoo\033[55m"),
        (s.proportional_spacing("foo"), "\033[26mfoo\033[50m"),
        (s.red("foo"), "\033[31mfoo\033[39m"),
        (s.red_background("foo"), "\033[41mfoo\033[49m"),
        (s.single_line_over_or_left("foo"), "\033[62mfoo\033[65m"),
        (s.single_line_under_or_right("foo"), "\033[60mfoo\033[65m"),
        (s.single_underline("foo"), "\033[4mfoo\033[24m"),
        (s.slow_blink("foo"), "\033[5mfoo\033[25m"),
        (s.strike("foo"), "\033[9mfoo\033[29m"),
        (s.stress("foo"), "\033[64mfoo\033[65m"),
        (s.white("foo"), "\033[37mfoo\033[39m"),
        (s.white_background("foo"), "\033[47mfoo\033[49m"),
        (s.yellow("foo"), "\033[33mfoo\033[39m"),
        (s.yellow_background("foo"), "\033[43mfoo\033[49m"),
    ],
)
def test_sequence(sequence: Sequence, expect: str) -> None:
    assert str(sequence) == expect


@mark.parametrize(
    "sequence, expect",
    [
        (
            Sequence("Here's some ", s.red("red"), "!"),
            "Here's some \033[31mred\033[39m!",
        ),
        (
            Sequence(
                "Here's some ", s.red("red and ", s.yellow("yellow"), " too"), "!"
            ),
            "Here's some \033[31mred and \033[33myellow\033[31m too\033[39m!",
        ),
    ],
)
def test_compound_sequences(sequence: Sequence, expect: str) -> None:
    assert str(sequence) == expect
