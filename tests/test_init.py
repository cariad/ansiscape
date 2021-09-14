from pytest import mark

import ansiscape as a


@mark.parametrize(
    "sequence, expect",
    [
        (a.alternative_font_0("foo"), "\033[11mfoo\033[10m"),
        (a.alternative_font_1("foo"), "\033[12mfoo\033[10m"),
        (a.alternative_font_2("foo"), "\033[13mfoo\033[10m"),
        (a.alternative_font_3("foo"), "\033[14mfoo\033[10m"),
        (a.alternative_font_4("foo"), "\033[15mfoo\033[10m"),
        (a.alternative_font_5("foo"), "\033[16mfoo\033[10m"),
        (a.alternative_font_6("foo"), "\033[17mfoo\033[10m"),
        (a.alternative_font_7("foo"), "\033[18mfoo\033[10m"),
        (a.alternative_font_8("foo"), "\033[19mfoo\033[10m"),
        (a.black("foo"), "\033[30mfoo\033[39m"),
        (a.black_background("foo"), "\033[40mfoo\033[49m"),
        (a.blackletter("foo"), "\033[20mfoo\033[23m"),
        (a.blue("foo"), "\033[34mfoo\033[39m"),
        (a.blue_background("foo"), "\033[44mfoo\033[49m"),
        (a.bright_black("foo"), "\033[38;5;8mfoo\033[39m"),
        (a.bright_black_background("foo"), "\033[48;5;8mfoo\033[49m"),
        (a.bright_blue("foo"), "\033[38;5;12mfoo\033[39m"),
        (a.bright_blue_background("foo"), "\033[48;5;12mfoo\033[49m"),
        (a.bright_cyan("foo"), "\033[38;5;14mfoo\033[39m"),
        (a.bright_cyan_background("foo"), "\033[48;5;14mfoo\033[49m"),
        (a.bright_green("foo"), "\033[38;5;10mfoo\033[39m"),
        (a.bright_green_background("foo"), "\033[48;5;10mfoo\033[49m"),
        (a.bright_magenta("foo"), "\033[38;5;13mfoo\033[39m"),
        (a.bright_magenta_background("foo"), "\033[48;5;13mfoo\033[49m"),
        (a.bright_red("foo"), "\033[38;5;9mfoo\033[39m"),
        (a.bright_red_background("foo"), "\033[48;5;9mfoo\033[49m"),
        (a.bright_white("foo"), "\033[38;5;15mfoo\033[39m"),
        (a.bright_white_background("foo"), "\033[48;5;15mfoo\033[49m"),
        (a.bright_yellow("foo"), "\033[38;5;11mfoo\033[39m"),
        (a.bright_yellow_background("foo"), "\033[48;5;11mfoo\033[49m"),
        (a.circle("foo"), "\033[52mfoo\033[54m"),
        (a.conceal("foo"), "\033[8mfoo\033[28m"),
        (a.cyan("foo"), "\033[36mfoo\033[39m"),
        (a.cyan_background("foo"), "\033[46mfoo\033[49m"),
        (a.double_line_over_or_left("foo"), "\033[63mfoo\033[65m"),
        (a.double_line_under_or_right("foo"), "\033[61mfoo\033[65m"),
        (a.double_underline("foo"), "\033[21mfoo\033[24m"),
        (a.fast_blink("foo"), "\033[6mfoo\033[25m"),
        (a.frame("foo"), "\033[51mfoo\033[54m"),
        (a.green("foo"), "\033[32mfoo\033[39m"),
        (a.green_background("foo"), "\033[42mfoo\033[49m"),
        (a.heavy("foo"), "\033[1mfoo\033[22m"),
        (a.invert("foo"), "\033[7mfoo\033[27m"),
        (a.italic("foo"), "\033[3mfoo\033[23m"),
        (a.light("foo"), "\033[2mfoo\033[22m"),
        (a.magenta("foo"), "\033[35mfoo\033[39m"),
        (a.magenta_background("foo"), "\033[45mfoo\033[49m"),
        (a.overline("foo"), "\033[53mfoo\033[55m"),
        (a.proportional_spacing("foo"), "\033[26mfoo\033[50m"),
        (a.red("foo"), "\033[31mfoo\033[39m"),
        (a.red_background("foo"), "\033[41mfoo\033[49m"),
        (a.single_line_over_or_left("foo"), "\033[62mfoo\033[65m"),
        (a.single_line_under_or_right("foo"), "\033[60mfoo\033[65m"),
        (a.single_underline("foo"), "\033[4mfoo\033[24m"),
        (a.slow_blink("foo"), "\033[5mfoo\033[25m"),
        (a.strike("foo"), "\033[9mfoo\033[29m"),
        (a.stress("foo"), "\033[64mfoo\033[65m"),
        (a.white("foo"), "\033[37mfoo\033[39m"),
        (a.white_background("foo"), "\033[47mfoo\033[49m"),
        (a.yellow("foo"), "\033[33mfoo\033[39m"),
        (a.yellow_background("foo"), "\033[43mfoo\033[49m"),
    ],
)
def test_sequence(sequence: a.Sequence, expect: str) -> None:
    assert str(sequence) == expect


@mark.parametrize(
    "sequence, expect",
    [
        (
            a.Sequence("Here's some ", a.red("red"), "!"),
            "Here's some \033[31mred\033[39m!",
        ),
        (
            a.Sequence(
                "Here's some ", a.red("red and ", a.yellow("yellow"), " too"), "!"
            ),
            "Here's some \033[31mred and \033[33myellow\033[31m too\033[39m!",
        ),
    ],
)
def test_compound_sequences(sequence: a.Sequence, expect: str) -> None:
    assert str(sequence) == expect
