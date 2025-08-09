"""Core utilities for detecting the installed Google Chrome version.

The functions in this module provide platform-specific strategies to
determine the locally installed Google Chrome version.
"""

# Copyright (c) 2023 Hasan Sezer Taşan
# Licensed under the MIT License
# ruff: noqa: S404, S603, S605, C901
from __future__ import annotations

import os
import pathlib
import re
import subprocess
from sys import platform
from typing import Optional


def extract_version_registry(output: str) -> Optional[str]:
    """Extract Chrome version from a Windows registry query output string.

    Parameters
    ----------
    output: str
        Raw text captured from a ``reg query`` command targeting the Google Chrome
        uninstall key.

    Returns:
    -------
    Optional[str]
        Chrome version string (e.g., ``"123.0.6312.86"``) if found; otherwise ``None``.

    Examples:
    --------
    ```python
    extract_version_registry()
    "123.0.6312.86"
    ```

    """
    try:
        # Use a regular expression to extract the version string after
        # "DisplayVersion    REG_SZ"
        match = re.search(r"DisplayVersion\s+REG_SZ\s+([^\r\n]+)", output)
        if match:
            return match.group(1).strip()
    except (TypeError, ValueError):
        # Gracefully handle unexpected input types or missing key
        return None
    else:
        return None


def extract_version_folder() -> Optional[str]:
    """Extract Chrome version by inspecting Windows installation folders.

    Checks both 32-bit and 64-bit ``Program Files`` directories for a Chrome
    ``Application`` folder whose subdirectory name matches a version pattern.

    Returns:
    -------
    Optional[str]
        Chrome version string if a matching directory name is found; otherwise ``None``.

    Examples:
    --------
    ```python
    extract_version_folder()
    "123.0.6312.86"
    ```

    """
    for program_files_variant_index in range(2):
        path = (
            "C:\\Program Files"
            + (" (x86)" if program_files_variant_index else "")
            + "\\Google\\Chrome\\Application"
        )
        if pathlib.Path(path).is_dir():
            candidate_paths = [
                entry.path for entry in os.scandir(path) if entry.is_dir()
            ]
            for candidate_path in candidate_paths:
                directory_name = pathlib.Path(candidate_path).name
                pattern = r"\d+\.\d+\.\d+\.\d+"
                match = re.search(pattern, directory_name)
                if match and match.group():
                    # Found a Chrome version.
                    return match[0]

    return None


def get_chrome_version() -> Optional[str]:
    """Get the installed Google Chrome version for the current platform.

    On Linux and macOS, the function invokes the Chrome binary with the
    ``--version`` flag. On Windows, it first attempts to read the version
    from the registry; if unavailable, it falls back to parsing the
    installation directory name.

    Returns:
    -------
    Optional[str]
        Chrome version string if detected; otherwise ``None``.

    Examples:
    --------
    ```python
    get_chrome_version()
    "123.0.6312.86"
    ```
    """
    version: Optional[str] = None
    install_path: Optional[str] = None

    if platform.startswith("linux"):
        # Linux
        install_path = "/usr/bin/google-chrome"
    elif platform == "darwin":
        # macOS
        install_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    elif platform == "win32":
        # Windows
        # Try registry key first, fall back to folder name parsing
        query = (
            "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\"
            "Uninstall\\Google Chrome"
        )
        command = ["reg", "query", query]
        try:
            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, text=True
            )
        except subprocess.CalledProcessError:
            output = ""
        version = extract_version_registry(output) or extract_version_folder()

    # When calling the binary with spaces in the path (macOS), wrap in quotes
    if install_path:
        command = f'"{install_path}" --version'
        output = os.popen(command).read()
        match = re.search(r"Google Chrome ([\d\.]+)", output)
        version = match.group(1) if match else None

    return version
