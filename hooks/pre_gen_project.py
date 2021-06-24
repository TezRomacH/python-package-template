"""This module is called before project is created."""

from typing import Callable, List

import re
import sys

MODULE_REGEX = re.compile(r"^[a-z][a-z0-9\-\_]+[a-z0-9]$")
SEMVER_REGEX = re.compile(
    r"""
        ^
        (?P<major>0|[1-9]\d*)
        \.
        (?P<minor>0|[1-9]\d*)
        \.
        (?P<patch>0|[1-9]\d*)
        (?:-(?P<prerelease>
            (?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
            (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*
        ))?
        (?:\+(?P<build>
            [0-9a-zA-Z-]+
            (?:\.[0-9a-zA-Z-]+)*
        ))?
        $
    """,
    re.VERBOSE,
)

module_name = "{{ cookiecutter.project_name }}"
version = "{{ cookiecutter.version }}"
line_length = "{{ cookiecutter.line_length }}"


def validate_project_name() -> None:
    """Ensure that `project_name` parameter is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or underscores.

    Raises:
        ValueError: If module_name is not a valid Python module name
    """
    if MODULE_REGEX.fullmatch(module_name) is None:
        message = f"ERROR: The project name `{module_name}` is not a valid Python module name."
        raise ValueError(message)


def validate_semver() -> None:
    """Ensure version in semver notation.

    Raises:
        ValueError: If version is not in semver notation
    """
    if SEMVER_REGEX.fullmatch(version) is None:
        message = f"ERROR: The `{version}` is not in semver notation (https://semver.org/)"
        raise ValueError(message)


def validate_line_length() -> None:
    """Validate line_length parameter. Length should be between 50 and 300.

    Raises:
        ValueError: If line_length isn't between 50 and 300
    """
    if not (50 <= int(line_length) <= 300):
        message = f"ERROR: line_length must be between 50 and 300. Got `{line_length}`."
        raise ValueError(message)


validators: List[Callable[[], None]] = [
    validate_project_name,
    validate_semver,
    validate_line_length,
]

for validator in validators:
    try:
        validator()
    except ValueError as ex:
        print(ex)
        sys.exit(1)
