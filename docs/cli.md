# CLI usage

## Discovering terminal support

To see examples of the formatting supported by your terminal, run:

```bash
ansiscape --example
```

## Converting encoded text to explanatory JSON

The `ansiscape` CLI will read from `stdin` and write to `stdout` a JSON document describing the input.

For example, to interpret a simple string:

```bash
echo -e "\033[1mhello world\033[22m" | ansiscape
```

```json
[
  {
    "weight": 1
  },
  "hello world",
  {
    "weight": 0
  }
]
```

!!! info
    The `-e` is needed with `echo` to prevent `echo` escaping the escape codes.

You can pipe the output of any command into `ansiscape` to generate explanatory JSON:

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
  {
    "background": -1
  },
  "\ncoverage.xml\n",
  {
    "foreground": 4,
    "weight": 1
  },
  "dist",
  {
    "background": -1
  },
  "\n",
  {
    "foreground": 4,
    "weight": 1
  },
  "docs",
  {
    "background": -1
  },
  "\nfoo.json\n",
  {
    "foreground": 4,
    "weight": 1
  },
  "htmlcov",
  {
    "background": -1
  },
  "\nLICENSE\n",
  {
    "foreground": 2,
    "weight": 1
  },
  "lint.sh",
  {
    "background": -1
  },
  "\nMANIFEST.in\nmkdocs.yml\nmypy.ini\nPipfile\nPipfile.lock\npyproject.toml\nREADME.md\nsetup.py\n",
  {
    "foreground": 4,
    "weight": 1
  },
  "tests",
  {
    "background": -1
  }
]
```

See the [enum documentation](interpretation.md) to translate the integer values to meaningful interpretations.

## If your application doesn't emit escape codes through pipes

Some applications omit escape codes from their output if they detect they're running in a non-interactive shell (i.e. their output is being redirected or piped).

Tools like [NaughTTY](https://github.com/cariad/naughtty/) can fool these applications into emitting their codes by wrapping them in a pseudo-terminal.

To use **NaughTTY** with **ansiscape**:

```bash
naughtty APP | ansiscape
```
