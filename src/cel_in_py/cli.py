"""Console script for cel_in_py."""
import cel_in_py

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for cel_in_py."""
    console.print("Replace this message by putting your code into "
               "cel_in_py.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
