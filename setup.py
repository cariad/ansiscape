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
    "Programming Language :: Python :: 3.10",
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
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Create and interpret ANSI escape codes",
    entry_points={
        "console_scripts": [
            "ansiscape=ansiscape.__main__:cli_entry",
        ],
    },
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="ansiscape",
    packages=[
        "ansiscape",
        "ansiscape.enums",
        "ansiscape.exceptions",
        "ansiscape.interpreters",
        "ansiscape.types",
        "ansiscape.version",
    ],
    package_data={
        "ansiscape": ["py.typed"],
        "ansiscape.enums": ["py.typed"],
        "ansiscape.exceptions": ["py.typed"],
        "ansiscape.interpreters": ["py.typed"],
        "ansiscape.types": ["py.typed"],
        "ansiscape.version": ["py.typed"],
    },
    python_requires=">=3.8",
    url="https://github.com/cariad/ansiscape",
    version=version,
)
