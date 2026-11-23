Usage
=====

As a library
------------

Import the package and call :func:`chrome_version.get_chrome_version`:

.. code-block:: python

   import chrome_version

   print(chrome_version.get_chrome_version())
   # '103.0.5060.114'

The function returns the detected version string, or ``None`` if Chrome is
not installed or its version cannot be determined.

From the command line
---------------------

Installing the package also provides the ``chrome-version`` console script:

.. code-block:: sh

   chrome-version
   # 103.0.5060.114

It prints the detected version and exits ``0``; if Chrome cannot be found it
writes an error to ``stderr`` and exits ``1``. Additional flags:

.. code-block:: sh

   chrome-version --version   # print the installed chrome-version package version
   chrome-version --info      # print package, Python, and platform details

The module is also runnable directly:

.. code-block:: sh

   python -m chrome_version
