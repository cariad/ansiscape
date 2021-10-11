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

`ansiscape` on the command line will read from stdin and emit a JSON document describing the text and its escape codes.

For example:

```bash
ls --color | ansiscape
```

<!--dinject as=markdown host=shell range=start-->

```text
[{"background": -1, "foreground": 4, "weight": 1},"ansiscape",{"background": -1},"\n",{"foreground": 4, "weight": 1},"ansiscape.egg-info",{"background": -1},"\n",{"foreground": 2, "weight": 1},"build.sh",{"background": -1},"\ncoverage.xml\n",{"foreground": 4, "weight": 1},"dist",{"background": -1},"\n",{"foreground": 4, "weight": 1},"docs",{"background": -1},"\n",{"foreground": 4, "weight": 1},"htmlcov",{"background": -1},"\nLICENSE\n",{"foreground": 2, "weight": 1},"lint.sh",{"background": -1},"\nMANIFEST.in\nmkdocs.yml\nmypy.ini\nPipfile\nPipfile.lock\npyproject.toml\nREADME.md\nsetup.py\n",{"foreground": 2, "weight": 1},"test-cli.sh",{"background": -1},"\n",{"foreground": 4, "weight": 1},"tests",{"background": -1},"\n",{"foreground": 2, "weight": 1},"test.sh",{"background": -1}]
```

<!--dinject range=end-->

Full documentation is published at [ansiscape.readthedocs.io](https://ansiscape.readthedocs.io).

## Basic Python usage

`ansiscape` provides a library of functions for formatting text.

For example, to make text bold:

```python
from ansiscape import heavy

print(heavy("Hello, world!"))
```

<!--dinject as=markdown host=shell range=start-->

```text
[1mHello, world![22m
```

<!--dinject range=end-->

These functions can be nested to create complex formatted strings. Specific instructions can also be embedded:

```python
from ansiscape import Interpretation, Sequence, heavy
from ansiscape.enums import MetaInterpretation, Weight

sequence = Sequence(
    Interpretation(weight=Weight.HEAVY),
    "Hello, world!",
    Interpretation(weight=MetaInterpretation.REVERT),
)

print(sequence)
```

<!--dinject as=markdown host=shell range=start-->

```text
[1mHello, world![22m
```

<!--dinject range=end-->

Full documentation is published at [ansiscape.readthedocs.io](https://ansiscape.readthedocs.io).

## 👋 Hello!

**Hello!** I'm [Cariad Eccleston](https://cariad.io) and I'm an independent/freelance software engineer. If my work has value to you, please consider [sponsoring](https://github.com/sponsors/cariad/).

If you ever raise a bug, request a feature or ask a question then mention that you're a sponsor and I'll respond as a priority. Thank you!
