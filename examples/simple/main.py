"""Minimal example: detect and print the installed Google Chrome version."""

from chrome_version import get_chrome_version


def main() -> None:
    """Detect the installed Chrome version and print it to stdout."""
    version = get_chrome_version()
    if version is None:
        print("Google Chrome was not detected on this system.")
    else:
        print(f"Detected Google Chrome {version}")


if __name__ == "__main__":
    main()
