import typer

from {{ cookiecutter.project_name.lower().replace('-', '_') }}.example import hello

app = typer.Typer(help="{{ cookiecutter.project_description }}")

@app.command(name="")
def main(name: str = typer.Option(..., help="Name of person to greet.")):
    """Greetings for giving name"""
    typer.echo(hello(name))
