try:
    import typer
except ImportError:
    # First Way: Raise the error if Typer is not installed.
    # raise ImportError(
    #     "Typer is not installed, please install it using `pip install typer` and try again."
    # )
    # Second Way: Exit with a non-zero exit code to indicate a failure
    assert (
        False
    ), "Typer is not installed, please install it using `pip install typer` and try again."
from chrome_version.resolver import get_chrome_version


app = typer.Typer()


@app.command(
    name="Get Chrome Version",
    help="Get the version of Chrome.",
    short_help="Get the version of Chrome.",
)
def main():
    """
    Get the version of Chrome.
    """
    version = get_chrome_version()
    typer.echo(version)


if __name__ == "__main__":
    app()
