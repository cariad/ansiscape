from pathlib import Path
from tempfile import NamedTemporaryFile
from time import sleep
from webbrowser import open as open_browser

from ansiscape.types import RGB


def get_8_bit_rgb(code: int) -> RGB:
    """
    Converts an ANSI escape code to an 8-bit colour.

    `code` is taken from the third attribute in, for example, "38;5;<code>m".
    """

    if not 16 <= code <= 231:
        raise ValueError(f'"code" ({code}) must be 16 - 231 inclusive')

    for r in range(0, 6):
        for g in range(0, 6):
            for b in range(0, 6):
                if 16 + 36 * r + 6 * g + b == code:
                    return ((r * 51) / 255, (g * 51) / 255, (b * 51) / 255)

    raise ValueError(f'failed to get 8_bit RGH for code "{code}"')


def make_8_bit_rgb_visualization_html() -> str:
    css = (
        ".colors { font-family: monospace; }"
        ".colors div { width: 1.6rem; height: 1.6rem; display: inline-block; }"
    )
    html = f'<html><style>{css}</style><body class="colors">'
    for code in range(16, 232):
        r, g, b = get_8_bit_rgb(code)
        style = f"background: rgb(calc({r}*255), calc({g}*255), calc({b}*255));"
        html = f'{html}<div style="{style}">{code}</div>'
        if (code - 15) % 36 == 0 and code < 231:
            html = f"{html}<br />"
    return f"{html}</body></html>"


def visualize_8_bit_rgb() -> None:
    """
    Creates a HTML table visualising the 216 non-grey 8-bit colours, and opens
    it directly in the default browser.
    """

    with NamedTemporaryFile() as t:
        path = Path(t.name).resolve().absolute()
        with open(path, "w") as f:
            f.write(make_8_bit_rgb_visualization_html())
        open_browser(f"file://{path.as_posix()}")
        # Give the browser a chance to open the file before we delete it:
        sleep(1)
