from .core import get_chrome_version


def app():
    """
    Get the version of Chrome.
    """
    version = get_chrome_version()
    print(f"Chrome version: {version}")
