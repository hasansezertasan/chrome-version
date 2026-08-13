"""Tests for the ``chrome-version`` console-script entrypoint."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chrome_version import cli

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


def test_main_prints_detected_version(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    mocker: MockerFixture,
) -> None:
    """A detected version is printed to stdout and the process exits ``0``."""
    monkeypatch.setattr("sys.argv", ["chrome-version"])
    mocker.patch("chrome_version.cli.get_chrome_version", return_value="103.0.5060.114")

    with pytest.raises(SystemExit) as exc:
        cli.main()

    assert exc.value.code == 0
    assert "103.0.5060.114" in capsys.readouterr().out


def test_main_reports_missing_chrome(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    mocker: MockerFixture,
) -> None:
    """When Chrome is undetectable, an error is written and the exit code is ``1``."""
    monkeypatch.setattr("sys.argv", ["chrome-version"])
    mocker.patch("chrome_version.cli.get_chrome_version", return_value=None)

    with pytest.raises(SystemExit) as exc:
        cli.main()

    assert exc.value.code == 1
    assert "not installed" in capsys.readouterr().err


def test_main_version_flag(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """``--version`` prints the package version and exits ``0``."""
    monkeypatch.setattr("sys.argv", ["chrome-version", "--version"])

    with pytest.raises(SystemExit) as exc:
        cli.main()

    assert exc.value.code == 0
    assert capsys.readouterr().out.strip()


def test_main_info_flag(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """``--info`` prints application, Python, and platform details and exits ``0``."""
    monkeypatch.setattr("sys.argv", ["chrome-version", "--info"])

    with pytest.raises(SystemExit) as exc:
        cli.main()

    assert exc.value.code == 0
    out = capsys.readouterr().out
    assert "Application Version:" in out
    assert "Python Version:" in out
    assert "Platform:" in out
