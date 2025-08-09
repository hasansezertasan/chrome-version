"""CLI entrypoint for retrieving the installed Chrome version."""
# ruff: noqa: T201

from chrome_version.core import get_chrome_version


def main() -> None:
    """Print the detected Chrome version to stdout.

    This function is used by the ``chrome-version`` console script.
    """
    version = get_chrome_version()
    print(version)
