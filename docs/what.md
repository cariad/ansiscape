# What are ANSI escape codes?

## Introduction

ANSI escape codes are commands embedded in text. These commands can control aspects of a terminal session, like changing the text colour.

They're called _escape_ codes because they're preceded by the ASCII `ESC` character; octal `33`, represented by `\033` in Python.

An escape sequence begins when a terminal encounters `ESC[` and ends when it encounters `m`. Everything between the `[` and `m` is the _escape code_.

## Example

In Python, the string `\033[31;1mHello, world!\033[0m` contains two escape sequences and two escape codes:

```text
       |||escape sequences|||
       vvvvvvvvvv     vvvvvvv
Hello, \033[31;1mworld\033[0m!
            ^^^^           ^
            |||escape codes|
```

Specifically, the code `31;1` turns text red and bold, while the code `0` returns all the formatting back to the default.

<!--
## How `ansiscape` helps

If you're building software that needs to recognise ANSI escape codes, how could you know what `31:1` means?

`ansiscape` can tell you.

```python
from ansiscape import render

interpretation = render("31;1")

print(interpretation)
```
-->
