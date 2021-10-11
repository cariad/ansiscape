# Checks

`ansiscape.checks` contains functions to check the state of your application.

`should_emit_codes()` returns `True` if ANSI escape codes should be emitted. It'll return `False`, for example, if the script appears to be running non-interactively.
