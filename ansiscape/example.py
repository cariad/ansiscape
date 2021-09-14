from math import floor

import ansiscape as a
from ansiscape.types import SequenceProtocol


def make_example() -> SequenceProtocol:

    foreground_rgb = a.sequence()
    background_rgb = a.sequence()

    square = 10

    for row in range(0, square):
        for column in range(0, (square * square)):
            block = floor(column / square)
            r = (1 / square) * row
            g = (1 / square) * block
            b = (1 / square) * (column - (square * block))
            foreground_rgb.extend(a.foreground((r, g, b, 1), "X"))
            background_rgb.extend(a.background((r, g, b, 1), " "))

        foreground_rgb.extend("\n")
        background_rgb.extend("\n")

    return a.sequence(
        a.heavy(a.double_underline("ansiscape")),
        "\n\n",
        "Welcome to the ",
        a.heavy("ansiscape"),
        " example!\n\n",
        "These are ",
        a.heavy("heavy"),
        " and ",
        a.light("light"),
        ".\n\nThese are ",
        a.italic("italic"),
        " and ",
        a.blackletter("blackletter"),
        ".\n\nThese are ",
        a.single_underline("single underlined"),
        ", ",
        a.double_underline("double underlined"),
        " and ",
        a.overline("overlined"),
        ".\n\nThese are ",
        a.slow_blink("blinking slowly"),
        " and ",
        a.fast_blink("blinking fast"),
        ".\n\nThese are ",
        a.invert("inverted"),
        ", ",
        a.conceal("concealed"),
        " (that's ",
        a.italic("concealed"),
        ") and ",
        a.strike("struck"),
        ".\n\nThese are the ",
        a.alternative_font_0("first alternative font"),
        ", the ",
        a.alternative_font_1("second alternative font"),
        ", the ",
        a.alternative_font_2("third alternative font"),
        ", the ",
        a.alternative_font_3("fourth alternative font"),
        ", the ",
        a.alternative_font_4("fifth alternative font"),
        ", the ",
        a.alternative_font_5("sixth alternative font"),
        ", the ",
        a.alternative_font_6("seventh alternative font"),
        ", the ",
        a.alternative_font_7("eighth alternative font"),
        " and the ",
        a.alternative_font_8("ninth alternative font"),
        ".\n\n",
        a.proportional_spacing("This entire line uses proportional spacing."),
        "\n\nThese are ",
        a.black("black"),
        ", ",
        a.red("red"),
        ", ",
        a.green("green"),
        ", ",
        a.yellow("yellow"),
        ", ",
        a.blue("blue"),
        ", ",
        a.magenta("magenta"),
        ", ",
        a.cyan("cyan"),
        ", ",
        a.white("white"),
        ", ",
        a.bright_black("bright black"),
        ", ",
        a.bright_red("bright red"),
        ", ",
        a.bright_green("bright green"),
        ", ",
        a.bright_yellow("bright yellow"),
        ", ",
        a.bright_blue("bright blue"),
        ", ",
        a.bright_magenta("bright magenta"),
        ", ",
        a.bright_cyan("bright cyan"),
        " and ",
        a.bright_white("bright white"),
        " foreground.\n\nThese are ",
        a.black_background("black"),
        ", ",
        a.red_background("red"),
        ", ",
        a.green_background("green"),
        ", ",
        a.yellow_background("yellow"),
        ", ",
        a.blue_background("blue"),
        ", ",
        a.magenta_background("magenta"),
        ", ",
        a.cyan_background("cyan"),
        ", ",
        a.white_background("white"),
        ", ",
        a.bright_black_background("bright black"),
        ", ",
        a.bright_red_background("bright red"),
        ", ",
        a.bright_green_background("bright green"),
        ", ",
        a.bright_yellow_background("bright yellow"),
        ", ",
        a.bright_blue_background("bright blue"),
        ", ",
        a.bright_magenta_background("bright magenta"),
        ", ",
        a.bright_cyan_background("bright cyan"),
        " and ",
        a.bright_white_background("bright white"),
        " background.\n\nHere's some foreground RGB:\n\n",
        foreground_rgb,
        "\nAnd some background RGB:\n\n",
        background_rgb,
        "\nThese are ",
        a.frame("framed"),
        " and ",
        a.circle("encircled"),
        ".\n\nThese are the ",
        a.single_line_under_or_right("single line under/right"),
        ", ",
        a.double_line_under_or_right("double line under/right"),
        ", ",
        a.single_line_over_or_left("single line over/left"),
        ", ",
        a.double_line_over_or_left("double line over/left"),
        " and ",
        a.stress("stress"),
        " ideograms.\n\nNot all terminals support all codes, so please don't ",
        "be too sad if some of the examples didn't work for you.",
    )
