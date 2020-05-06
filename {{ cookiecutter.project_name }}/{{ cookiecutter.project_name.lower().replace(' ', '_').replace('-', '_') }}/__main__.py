# type: ignore[attr-defined]

import random
from enum import Enum
from typing import Optional

import typer
from rich.console import Console

from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.example import hello


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    help="{{ cookiecutter.project_description }}"
)
console = Console()


@app.command(name="")
def main(
    name: str = typer.Option(..., help="Name of person to greet."),
    color: Optional[Color] = typer.Option(
        None,
        case_sensitive=False,
        help="Color for name. If not specified then color will be random.",
    ),
):
    """Greetings for giving name."""
    if color is None:
        # If no color specified use random value from `Color` class
        color = random.choice(list(Color.__members__.values()))

    greeting: str = hello(name)
    console.print(f"[bold {color}]{greeting}[/]")
