# type: ignore[attr-defined]

import random
from enum import Enum
from typing import Optional

import typer
from rich.console import Console

from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} import __version__
from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.example import hello


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="{{ cookiecutter.project_name }}",
    help="{{ cookiecutter.project_description }}",
    add_completion=False,
)
console = Console()


def version_callback(value: bool):
    """Prints the version of the package."""
    if value:
        console.print(
            f"[yellow]{{ cookiecutter.project_name }}[/] version: [bold blue]{__version__}[/]"
        )
        raise typer.Exit()


@app.command(name="")
def main(
    name: str = typer.Option(..., help="Name of person to greet."),
    color: Optional[Color] = typer.Option(
        None,
        case_sensitive=False,
        help="Color for name. If not specified then choice will be random.",
    ),
    version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the {{ cookiecutter.project_name }} package.",
    ),
):
    """Prints a greeting for a giving name."""
    if color is None:
        # If no color specified use random value from `Color` class
        color = random.choice(list(Color.__members__.values()))

    greeting: str = hello(name)
    console.print(f"[bold {color}]{greeting}[/]")
