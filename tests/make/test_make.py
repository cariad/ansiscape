from ansiscape.make import WithCodes, bold


def test_foo() -> None:
    s = WithCodes("Here's some ", bold("bold"), "!")
    assert str(s) == "Here's some \033[1mbold\033[22m!"
