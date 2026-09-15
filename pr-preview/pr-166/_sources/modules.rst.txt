.. A 7-character "=" underline (the length of "Modules") is treated as a
   merge-conflict separator by ``git diff --check`` / ``check-merge-conflict``;
   keep this underline longer than the title to avoid the false positive.

Modules
=========

The API reference below is generated automatically from the source docstrings.

Package (``chrome_version``)
----------------------------

The public interface. :func:`~chrome_version.get_chrome_version` is re-exported
here for convenient access.

.. automodule:: chrome_version

Core (``chrome_version.core``)
------------------------------

Platform-specific Chrome-detection logic.

.. automodule:: chrome_version.core

CLI (``chrome_version.cli``)
----------------------------

The ``chrome-version`` console-script entrypoint.

.. automodule:: chrome_version.cli
