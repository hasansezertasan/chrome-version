"""Advanced example: gate a script on a minimum Chrome major version.

Exits non-zero when Chrome is missing or older than the required major version,
so it can be used as a preflight check before launching browser-based tooling
(for example in CI).
"""

import sys

from chrome_version import get_chrome_version

REQUIRED_MAJOR = 120


def main() -> int:
    """Check the installed Chrome against the required minimum major version.

    Returns:
        ``0`` when a new-enough Chrome is present, ``1`` when Chrome is missing
        or older than the required major version.
    """
    version = get_chrome_version()
    if version is None:
        print("Google Chrome was not detected.", file=sys.stderr)
        return 1

    major = int(version.split(".")[0])
    if major < REQUIRED_MAJOR:
        print(
            f"Chrome {version} is older than the required major {REQUIRED_MAJOR}.",
            file=sys.stderr,
        )
        return 1

    print(f"Chrome {version} satisfies the minimum major {REQUIRED_MAJOR}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
