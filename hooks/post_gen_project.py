"""This module is called after project is created."""

import textwrap
from pathlib import Path
from shutil import move, rmtree

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"

# Values to generate correct license
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.organization }}"

# Values to generate github repository
GITHUB_USER = "{{ cookiecutter.github_name }}"

licenses = {
    "MIT": "mit",
    "BSD-3": "bsd3",
    "GNU GPL v3.0": "gpl3",
    "Apache Software License 2.0": "apache",
}


def generate_license() -> None:
    """Generate license file for the project."""
    move(f"{PROJECT_DIRECTORY}/_licences/{licenses[LICENSE]}.txt", f"{PROJECT_DIRECTORY}/LICENSE")
    rmtree(f"{PROJECT_DIRECTORY}/_licences/")


def print_futher_instuctions() -> None:
    """Show user what to do next after project creation."""
    message = f"""
    Your project {PROJECT_NAME} is created.

    1) Now you can start working on it:

        $ cd {PROJECT_NAME} && git init

    2) If you don't have Poetry installed run:

        $ make poetry-download

    3) Initialize poetry and install pre-commit hooks:

        $ make install
        $ make pre-commit-install

    4) Run codestyle:

        $ make codestyle

    5) Upload initial code to GitHub:

        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git branch -M main
        $ git remote add origin https://github.com/{GITHUB_USER}/{PROJECT_NAME}.git
        $ git push -u origin main
    """
    print(textwrap.dedent(message))


generate_license()
print_futher_instuctions()
