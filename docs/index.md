# Introduction

`ansiscape` is a Python package for interpreting and creating ANSI escape codes.

## Highlights

Create formatted text, with **support for nested colours** and **custom RGB**:

```python
from ansiscape import Sequence, green, foreground

text = Sequence(
    green("This is ", foreground((1.0, 0.5, 0.0, 1.0), "heavy"), ", Doc,"),
    " said Marty.",
)
print(text)
```

Convert a string with embedded escape codes into a list of strings and **explanatory dictionaries**:

```python
from ansiscape import Sequence

Sequence("Hello world, and \033[3myou\033[23m in particular!").resolved
```

```python
[
  "Hello world, and ",
  {"calligraphy": Calligraphy.ITALIC},
  "you",
  {"calligraphy": Calligraphy.NONE},
  " in particular!",
]
```

## Installation

`ansiscape` requires Python 3.8 or later.

```bash
pip install ansiscape
```

## Discovering terminal support

To see examples of the formatting supported by your terminal, run:

```bash
ansiscape
```

## The project

The source for `ansiscape` is available at [github.com/cariad/ansiscape](https://github.com/cariad/ansiscape) under the MIT licence.

And, **hello!** I'm [Cariad Eccleston](https://cariad.io) and I'm an independent/freelance software engineer. If my work has value to you, please consider [sponsoring](https://github.com/sponsors/cariad/).
