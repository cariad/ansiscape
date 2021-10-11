from ansiscape.checks import should_emit_codes


def test_should_emit_codes() -> None:
    assert not should_emit_codes()
