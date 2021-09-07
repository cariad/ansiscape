from ansiscape.enums import ColorScheme


def get_color_scheme(attribute: int) -> ColorScheme:
    """
    Gets the colour scheme described by the given attribute.

    This is typically the second attribute in a colour code. For example, pass
    `2` for the code `"38;2"`.
    """
    return ColorScheme(attribute)
