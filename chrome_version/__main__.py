import typer

app = typer.Typer(
    name="Chrome Version",
)


@app.callback(
    name="Hello World",
    help="Hello World.",
    short_help="Hello World.",
)
def main():
    """
    Get the version of Chrome.
    """
    typer.echo("Hello World.")


if __name__ == "__main__":
    app()
