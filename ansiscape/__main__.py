from argparse import ArgumentParser
from sys import argv, stdin, stdout
from typing import List, TextIO

from ansiscape import Sequence, get_version
from ansiscape.checks import should_emit_codes
from ansiscape.example import make_example


def cli_entry(
    cli_args: List[str] = argv,
    in_pipe: TextIO = stdin,
    out_pipe: TextIO = stdout,
) -> None:
    """
    CLI entrypoint.

    Arguments:
        args:     Command line arguments
        in_pipe:  "stdin" or other pipe to read from
        out_pipe: "stdout" or other pipe to write to
    """

    parser = ArgumentParser(
        description="Describes ANSI escape codes read from stdin.",
        epilog="Made with love by Cariad Eccleston: https://github.com/cariad/ansiscape",
    )

    parser.add_argument(
        "--check",
        action="store_true",
        help="checks if codes should be emitted",
    )

    parser.add_argument("--example", action="store_true", help="print an example")
    parser.add_argument("--version", action="store_true", help="print the version")

    args = parser.parse_args(cli_args[1:])

    if args.check:
        if should_emit_codes():
            out_pipe.write("yes\n")
        else:
            out_pipe.write("no\n")
        return

    if args.example:
        out_pipe.write(str(make_example()))
        return

    if args.version:
        out_pipe.write(str(get_version()) + "\n")
        return

    Sequence(in_pipe.read().strip()).write_json(out_pipe)
    out_pipe.flush()


if __name__ == "__main__":
    cli_entry()
