import typer

from {{ cookiecutter.project_name.lower().replace('-', '_') }}.example import hello


def hello(name: str = typer.Option(..., help="Name of person to greet.")):
    """Greetings for giving name"""
    typer.echo(hello(name))


if __name__ == "__main__":
    typer.run(main)
