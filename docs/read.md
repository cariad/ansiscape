# Reading Sequences

Regardless of how you [create a `Sequence`](make.md), you can consume it in a number of ways.

## Reading the entire Sequence as a string

Simply `print()` a `Sequence` to print its entire stack as an encoded string.

You can also cast a `Sequence` to `str` or read its `encoded` property to get the string value.

## Iterating through strings and Interpretation dictionaries

To iterate part-by-part through a `Sequence`, use the `resolved` generator.

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

Note that strings with embedded escape codes can be passed into the `Sequence` initialiser, but these will be converted to sub-sequences of plain strings and [`Interpretation`](interpretation.md) dictionaries. The `resolved` property will never return strings with embedded escape codes.

## Writing a JSON stream

To interpret a `Sequence` to JSON, pass a `TextIO` instance to the `json_write()` function.

```python
from ansiscape import Sequence
from sys import stdout

sequence = Sequence("Hello world, and \033[3myou\033[23m in particular!")
sequence.write_json(stdout)
```

```json
[
    "Hello world, and ",
    {
        "calligraphy": 2
    },
    "you",
    {
        "calligraphy": 0
    },
    " in particular!"
]
```

!!! question
    **Why not just provide the JSON as a plain string property?** Because it can be _huge_. Chances are, if you want JSON then you want to write it somewhere, and using TextIO can fulfil that while minimising memory usage.
