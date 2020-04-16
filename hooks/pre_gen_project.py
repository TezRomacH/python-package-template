import re
import sys
from typing import Callable, List

MODULE_REGEX = r"^[a-z][a-z0-9\-]+[a-z0-9]$"
module_name = "{{ cookiecutter.project_name }}"


def validate_project_name():
    """This validator is used to ensure that `project_name` is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or underscores.

    Raises:
        ValueError: If module_name is not a valid Python module name
    """
    if not re.match(MODULE_REGEX, module_name):
        message = (
            f"ERROR: The project name `{module_name}` is not a valid Python module name."
        )

        raise ValueError(message)


validators: List[Callable] = [validate_project_name]

for validator in validators:
    try:
        validator()
    except ValueError as ex:
        print(ex)
        sys.exit(1)
