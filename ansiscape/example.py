from math import floor

import ansiscape as s


def make_example() -> str:

    foreground_rgb = s.sequence()
    background_rgb = s.sequence()

    square = 10

    for row in range(0, square):
        for column in range(0, (square * square)):
            block = floor(column / square)
            r = (1 / square) * row
            g = (1 / square) * block
            b = (1 / square) * (column - (square * block))
            foreground_rgb += s.foreground((r, g, b, 1), "X")
            background_rgb += s.background((r, g, b, 1), " ")
        foreground_rgb += "\n"
        background_rgb += "\n"

    example = s.sequence(
        s.heavy(s.double_underline("ansiscape")),
        "\n\n",
        "Welcome to the ",
        s.heavy("ansiscape"),
        " example!\n\n",
        "These are ",
        s.heavy("heavy"),
        " and ",
        s.light("light"),
        ".\n\nThese are ",
        s.italic("italic"),
        " and ",
        s.blackletter("blackletter"),
        ".\n\nThese are ",
        s.single_underline("single underlined"),
        ", ",
        s.double_underline("double underlined"),
        " and ",
        s.overline("overlined"),
        ".\n\nThese are ",
        s.slow_blink("blinking slowly"),
        " and ",
        s.fast_blink("blinking fast"),
        ".\n\nThese are ",
        s.invert("inverted"),
        ", ",
        s.conceal("concealed"),
        " (that's ",
        s.italic("concealed"),
        ") and ",
        s.strike("struck"),
        ".\n\nThese are the ",
        s.alternative_font_0("first alternative font"),
        ", the ",
        s.alternative_font_1("second alternative font"),
        ", the ",
        s.alternative_font_2("third alternative font"),
        ", the ",
        s.alternative_font_3("fourth alternative font"),
        ", the ",
        s.alternative_font_4("fifth alternative font"),
        ", the ",
        s.alternative_font_5("sixth alternative font"),
        ", the ",
        s.alternative_font_6("seventh alternative font"),
        ", the ",
        s.alternative_font_7("eighth alternative font"),
        " and the ",
        s.alternative_font_8("ninth alternative font"),
        ".\n\n",
        s.proportional_spacing("This entire line uses proportional spacing."),
        "\n\nThese are ",
        s.black("black"),
        ", ",
        s.red("red"),
        ", ",
        s.green("green"),
        ", ",
        s.yellow("yellow"),
        ", ",
        s.blue("blue"),
        ", ",
        s.magenta("magenta"),
        ", ",
        s.cyan("cyan"),
        ", ",
        s.white("white"),
        ", ",
        s.bright_black("bright black"),
        ", ",
        s.bright_red("bright red"),
        ", ",
        s.bright_green("bright green"),
        ", ",
        s.bright_yellow("bright yellow"),
        ", ",
        s.bright_blue("bright blue"),
        ", ",
        s.bright_magenta("bright magenta"),
        ", ",
        s.bright_cyan("bright cyan"),
        " and ",
        s.bright_white("bright white"),
        " foreground.\n\nThese are ",
        s.black_background("black"),
        ", ",
        s.red_background("red"),
        ", ",
        s.green_background("green"),
        ", ",
        s.yellow_background("yellow"),
        ", ",
        s.blue_background("blue"),
        ", ",
        s.magenta_background("magenta"),
        ", ",
        s.cyan_background("cyan"),
        ", ",
        s.white_background("white"),
        ", ",
        s.bright_black_background("bright black"),
        ", ",
        s.bright_red_background("bright red"),
        ", ",
        s.bright_green_background("bright green"),
        ", ",
        s.bright_yellow_background("bright yellow"),
        ", ",
        s.bright_blue_background("bright blue"),
        ", ",
        s.bright_magenta_background("bright magenta"),
        ", ",
        s.bright_cyan_background("bright cyan"),
        " and ",
        s.bright_white_background("bright white"),
        " background.\n\nHere's some foreground RGB:\n\n",
        foreground_rgb,
        "\nAnd some background RGB:\n\n",
        background_rgb,
        "\nThese are ",
        s.frame("framed"),
        " and ",
        s.circle("encircled"),
        ".\n\nThese are the ",
        s.single_line_under_or_right("single line under/right"),
        ", ",
        s.double_line_under_or_right("double line under/right"),
        ", ",
        s.single_line_over_or_left("single line over/left"),
        ", ",
        s.double_line_over_or_left("double line over/left"),
        " and ",
        s.stress("stress"),
        " ideograms.",
    )
    return (
        str(example)
        + "\n\nNot all terminals support all codes, so please don't be too sad "
        + "if some of the examples didn't work for you."
    )
