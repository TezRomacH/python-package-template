"""This module is called after project is created."""

import os
import textwrap
from pathlib import Path

# Get the root project directory:
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"

# We need these values to generate correct license:
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.organization }}"

# We need these values to generate github repository:
GITHUB_USER = "{{ cookiecutter.github_name }}"

licenses = {
    "MIT": "mit",
    "BSD-3": "bsd3",
    "GNU GPL v3.0": "gpl3",
    "Apache Software License 2.0": "apache",
}


def generate_license() -> None:
    """Generates license file for the project."""
    license_result = os.system(
        f"lice {licenses[LICENSE]} -o '{ORGANIZATION}' -p {PROJECT_NAME} > {PROJECT_DIRECTORY}/LICENSE"
    )
    if license_result:  # it means that return code is not 0, print exception
        print(license_result)


def print_futher_instuctions() -> None:
    """Shows user what to do next after project creation."""
    message = f"""
    Your project {PROJECT_NAME} is created.

    1) Now you can start working on it:

        $ cd {PROJECT_NAME} && git init

    2) If you don't have Poetry installed run:

        $ make download-poetry

    3) Initialize poetry and install pre-commit hooks:

        $ make install

    4) Run codestyle:

        $ git add . && make install

    5) Upload initial code to GitHub (ensure you've run `make install` to use `pre-commit`):

        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git remote add origin https://github.com/{GITHUB_USER}/{PROJECT_NAME}.git
        $ git push -u origin master
    """
    print(textwrap.dedent(message))


generate_license()
print_futher_instuctions()
