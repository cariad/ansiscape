from io import StringIO

from ansiscape.__main__ import cli_entry


def test_cli_entry__example() -> None:
    stdout = StringIO()
    cli_entry(args=["ansiscape", "--example"], out_pipe=stdout)
    assert stdout.getvalue().startswith("\x1b[21;1mansiscape\x1b[24;22m")
    assert stdout.getvalue().endswith("work for you.\n\n")


def test_cli_entry__stdin() -> None:
    stdin = StringIO("\033[31mfoo\033[39m")
    stdout = StringIO()
    cli_entry(args=["ansiscape"], in_pipe=stdin, out_pipe=stdout)
    assert stdout.getvalue() == '[{"foreground": 1},"foo",{"foreground": -1}]\n'
