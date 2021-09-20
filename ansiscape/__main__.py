from sys import argv, stdin, stdout
from typing import List, TextIO

from ansiscape import Sequence
from ansiscape.example import make_example


def cli_entry(
    args: List[str] = argv,
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

    if len(args) > 1:
        out_pipe.write(str(make_example()))
        return

    Sequence(in_pipe.read().strip()).write_json(out_pipe)
    out_pipe.flush()


if __name__ == "__main__":
    cli_entry()
