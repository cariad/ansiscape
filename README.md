# ansiscape

[![CircleCI](https://circleci.com/gh/cariad/ansiscape/tree/main.svg?style=shield)](https://circleci.com/gh/cariad/ansiscape/tree/main) [![codecov](https://codecov.io/gh/cariad/ansiscape/branch/main/graph/badge.svg?token=cn6UnSvD8u)](https://codecov.io/gh/cariad/ansiscape) [![Documentation Status](https://readthedocs.org/projects/ansiscape/badge/?version=latest)](https://ansiscape.readthedocs.io/en/latest/?badge=latest)

`ansiscape` is a Python package and CLI tool for creating and interpreting ANSI escape codes.

- Support for **named**, **8-bit** and **24-bit colours**.
- Create formatted strings with **nested sequences** and **property reversions**.
- Convert embedded escape codes into **explanatory dictionaries**.
- Write sequences as **fully resolved strings** and **explanatory JSON**.

Full documentation is published at [ansiscape.readthedocs.io](https://ansiscape.readthedocs.io).

## Installation

`ansiscape` requires **Python 3.8 or later**.

```bash
pip install ansiscape
```

## Basic CLI usage

```bash
APP | ansiscape
```

For example:

```bash
ls --color | ansiscape
```

```json
[
  {
    "background": -1,
    "foreground": 4,
    "weight": 1
  },
  "ansiscape",
  {
    "background": -1
  },
  "\n",
  {
    "foreground": 4,
    "weight": 1
  },
  "ansiscape.egg-info",
  {
    "background": -1
  },
  "\n",
  {
    "foreground": 2,
    "weight": 1
  },
  "build.sh",
  ...
]
```

Full documentation is published at [ansiscape.readthedocs.io](https://ansiscape.readthedocs.io).

```python
from ansiscape import Interpretation, Sequence, heavy
from ansiscape.enums import MetaInterpretation, Weight

sequence = Sequence(
    Interpretation(weight=Weight.HEAVY),
    "Hello, world!",
    Interpretation(weight=MetaInterpretation.REVERT),
)

# or:

sequence = heavy("Hello, world!")

print(sequence)
```

```text
\033[1mHello, world!\033[22m
```

Full documentation is published at [ansiscape.readthedocs.io](https://ansiscape.readthedocs.io).

## 👋 Hello!

**Hello!** I'm [Cariad Eccleston](https://cariad.io) and I'm an independent/freelance software engineer. If my work has value to you, please consider [sponsoring](https://github.com/sponsors/cariad/).

If you ever raise a bug, request a feature or ask a question then mention that you're a sponsor and I'll respond as a priority. Thank you!
