from pathlib import Path

from setuptools import setup  # pyright: reportMissingTypeStubs=false

from ansiscape import get_version

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Utilities",
    "Typing :: Typed",
]

version = get_version()

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.io",
    classifiers=classifiers,
    description="Python package for interpreting ANSI escape codes",
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="ansiscape",
    packages=[
        "ansiscape",
        "ansiscape.enums",
        "ansiscape.interpreters",
        "ansiscape.strings",
        "ansiscape.strings.colors",
        "ansiscape.strings.colors.background",
        "ansiscape.strings.colors.background.named",
        "ansiscape.strings.colors.background.named_bright",
        "ansiscape.strings.colors.foreground",
        "ansiscape.strings.colors.foreground.named",
        "ansiscape.strings.colors.foreground.named_bright",
        "ansiscape.version",
    ],
    package_data={
        "ansiscape": ["py.typed"],
        "ansiscape.enums": ["py.typed"],
        "ansiscape.interpreters": ["py.typed"],
        "ansiscape.version": ["py.typed"],
        "ansiscape.strings": ["py.typed"],
        "ansiscape.strings.colors": ["py.typed"],
        "ansiscape.strings.colors.background": ["py.typed"],
        "ansiscape.strings.colors.background.named": ["py.typed"],
        "ansiscape.strings.colors.background.named_bright": ["py.typed"],
        "ansiscape.strings.colors.foreground": ["py.typed"],
        "ansiscape.strings.colors.foreground.named": ["py.typed"],
        "ansiscape.strings.colors.foreground.named_bright": ["py.typed"],
    },
    python_requires=">=3.8",
    url="https://github.com/cariad/ansiscape",
    version=version,
)
