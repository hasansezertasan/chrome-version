"""Tests for the platform-specific Chrome-detection logic in ``core``."""

from __future__ import annotations

import subprocess
from typing import TYPE_CHECKING, cast

from chrome_version import core

if TYPE_CHECKING:
    from pytest_mock import MockerFixture

_APP_DIR = r"C:\Program Files\Google\Chrome\Application"


class _FakeEntry:
    """Minimal stand-in for :class:`os.DirEntry` used by ``os.scandir`` mocks."""

    def __init__(self, path: str, *, is_dir: bool) -> None:
        self.path = path
        self._is_dir = is_dir

    def is_dir(self) -> bool:
        """Report whether this fake entry represents a directory."""
        return self._is_dir


def test_extract_version_registry_found() -> None:
    """A registry query containing ``DisplayVersion`` yields the version."""
    output = "    DisplayVersion    REG_SZ    123.0.6312.86\r\n"

    assert core.extract_version_registry(output) == "123.0.6312.86"


def test_extract_version_registry_no_match() -> None:
    """Output without a ``DisplayVersion`` line returns ``None``."""
    assert core.extract_version_registry("nothing useful here") is None


def test_extract_version_registry_invalid_input() -> None:
    """Non-string input is handled gracefully and returns ``None``."""
    # None is passed at runtime (to exercise the TypeError guard) but typed as
    # str via cast so every type checker sees a valid call.
    assert core.extract_version_registry(cast("str", None)) is None


def test_extract_version_folder_found(mocker: MockerFixture) -> None:
    """A versioned ``Application`` subdirectory yields its version name."""
    mocker.patch("chrome_version.core.pathlib.Path.is_dir", return_value=True)
    mocker.patch(
        "chrome_version.core.os.scandir",
        return_value=[_FakeEntry(rf"{_APP_DIR}\123.0.6312.86", is_dir=True)],
    )

    assert core.extract_version_folder() == "123.0.6312.86"


def test_extract_version_folder_no_versioned_dir(mocker: MockerFixture) -> None:
    """Only non-versioned or non-directory entries yield ``None``."""
    mocker.patch("chrome_version.core.pathlib.Path.is_dir", return_value=True)
    mocker.patch(
        "chrome_version.core.os.scandir",
        return_value=[
            _FakeEntry(rf"{_APP_DIR}\Dictionaries", is_dir=True),
            _FakeEntry(rf"{_APP_DIR}\chrome.exe", is_dir=False),
        ],
    )

    assert core.extract_version_folder() is None


def test_extract_version_folder_not_installed(mocker: MockerFixture) -> None:
    """A missing ``Application`` directory yields ``None``."""
    mocker.patch("chrome_version.core.pathlib.Path.is_dir", return_value=False)

    assert core.extract_version_folder() is None


def test_get_chrome_version_linux(mocker: MockerFixture) -> None:
    """On Linux the Chrome binary is invoked with ``--version``."""
    mocker.patch("chrome_version.core.platform", "linux")
    mocker.patch(
        "chrome_version.core.subprocess.check_output",
        return_value="Google Chrome 103.0.5060.114 \n",
    )

    assert core.get_chrome_version() == "103.0.5060.114"


def test_get_chrome_version_darwin(mocker: MockerFixture) -> None:
    """On macOS the Chrome binary is invoked with ``--version``."""
    mocker.patch("chrome_version.core.platform", "darwin")
    mocker.patch(
        "chrome_version.core.subprocess.check_output",
        return_value="Google Chrome 103.0.5060.114\n",
    )

    assert core.get_chrome_version() == "103.0.5060.114"


def test_get_chrome_version_binary_unparsable(mocker: MockerFixture) -> None:
    """Unparsable ``--version`` output yields ``None``."""
    mocker.patch("chrome_version.core.platform", "linux")
    mocker.patch(
        "chrome_version.core.subprocess.check_output",
        return_value="not a version string\n",
    )

    assert core.get_chrome_version() is None


def test_get_chrome_version_windows_registry(mocker: MockerFixture) -> None:
    """On Windows the version is read from the registry when available."""
    mocker.patch("chrome_version.core.platform", "win32")
    mocker.patch(
        "chrome_version.core.subprocess.check_output",
        return_value="    DisplayVersion    REG_SZ    124.0.6367.60\r\n",
    )

    assert core.get_chrome_version() == "124.0.6367.60"


def test_get_chrome_version_windows_folder_fallback(mocker: MockerFixture) -> None:
    """A failed registry query falls back to folder-name parsing."""
    mocker.patch("chrome_version.core.platform", "win32")
    mocker.patch(
        "chrome_version.core.subprocess.check_output",
        side_effect=subprocess.CalledProcessError(1, ["reg", "query"]),
    )
    mocker.patch(
        "chrome_version.core.extract_version_folder", return_value="124.0.6367.60"
    )

    assert core.get_chrome_version() == "124.0.6367.60"


def test_get_chrome_version_unknown_platform(mocker: MockerFixture) -> None:
    """An unrecognized platform yields ``None`` without shelling out."""
    mocker.patch("chrome_version.core.platform", "cygwin")

    assert core.get_chrome_version() is None
