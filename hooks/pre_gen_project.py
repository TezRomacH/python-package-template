"""This module is called before project is created."""

from typing import Callable, List

import re
import sys

MODULE_REGEX = r"^[a-z][a-z0-9\-\_]+[a-z0-9]$"
module_name = "{{ cookiecutter.project_name }}"
line_length = "{{ cookiecutter.line_length }}"


def validate_project_name() -> None:
    """Ensure that `project_name` parameter is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or underscores.

    Raises:
        ValueError: If module_name is not a valid Python module name
    """
    if not re.match(MODULE_REGEX, module_name):
        message = f"ERROR: The project name `{module_name}` is not a valid Python module name."
        raise ValueError(message)


def validate_line_length() -> None:
    """Validate line_length parameter. Length should be between 50 and 300.

    Raises:
        ValueError: If line_length isn't between 50 and 300
    """
    if not (50 <= int(line_length) <= 300):
        message = f"ERROR: line_length must be between 50 and 300. Got `{line_length}`."
        raise ValueError(message)


validators: List[Callable[[], None]] = [validate_project_name, validate_line_length]

for validator in validators:
    try:
        validator()
    except ValueError as ex:
        print(ex)
        sys.exit(1)
