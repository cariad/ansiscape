# Interpreting ANSI escape codes

The `ansiscape.Sequence` class expands embedded escape codes into [`Interpretation`](interpretation.md) dictionaries. Read the expanded sequence parts from the `resolved` property.

For example, to interpret `"Hello world, and \033[3myou\033[23m in particular!"`:

```python
from ansiscape import Sequence

sequence = Sequence("Hello world, and \033[3myou\033[23m in particular!")
for part in sequence.resolved:
    print(part)
```

```python
"Hello world, and "
{"calligraphy": Calligraphy.ITALIC}
"you"
{"calligraphy": Calligraphy.NONE}
" in particular!"
```
