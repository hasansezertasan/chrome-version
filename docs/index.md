<h1 align="center">
    <strong>Chrome Version</strong>
</h1>
<p align="center">
    <em>Get the version of Chrome installed on Windows, Linux, Mac. Cross-platform using Python, native OS detection, does not require Selenium.</em>
</p>
<p align="center">
    <a href="https://github.com/hasansezertasan/chrome-version" target="_blank">
        <img src="https://img.shields.io/github/last-commit/hasansezertasan/chrome-version" alt="Latest Commit">
    </a>
        <img src="https://img.shields.io/github/workflow/status/hasansezertasan/chrome-version/Test">
        <img src="https://img.shields.io/codecov/c/github/hasansezertasan/chrome-version">
    <br />
    <a href="https://pypi.org/project/chrome-version" target="_blank">
        <img src="https://img.shields.io/pypi/v/chrome-version" alt="Package version">
    </a>
    <a href="https://pypi.org/project/chrome-version" target="_blank">
        <img src="https://img.shields.io/pypi/pyversions/chrome-version">
    </a>
    <img src="https://img.shields.io/github/license/hasansezertasan/chrome-version">
</p>

## Installation

- To use it as a module:

``` bash
pip install chrome-version
```

- To use it as a CLI:

``` bash
pip install chrome-version[console]
```

## Usage

Module:

```python
>>> import chrome_version
>>> print(chrome_version.get_chrome_version())
>>> '103.0.5060.114'
```

CLI:

```bash
chrome-version
103.0.5060.114
```

## Why?

At first,

I needed to get the Chrome version for a project I was working on, which was using [Undetected Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver). I found the gist below.

When I used it in a variaty of projects, I decided to turn it into a module so I'll be free of copy/paste. It only have one functionality: getting the chrome version.

Then,

I decided to use it to learn more about:

- Using [Poetry](https://python-poetry.org/) for packaging and dependency management.
- Using typer for CLI.
- Versioning.
- License management.
- Documentation.
- Publishing a module on PyPI.
- Using GitHub Actions to automate the publishing process.
- ...

Finally,

Now it's kind of a playground for me to learn more...

## Motivation

- It might be useful for someone.
- It's easier to pip install a module than copy/paste a gist.
- Educational Purposes: A simple module is a good practice for me to learn how to build modules and publish them on PyPI and show others how easy it is.

## Disclaimer

This module based on [Detect the version of Chrome installed on Windows, Linux, Mac. Cross-platform using Python, native OS detection, does not require Selenium.](https://gist.github.com/primaryobjects/d5346bf7a173dbded1a70375ff7461b4) gist. I'm not the author of the gist, I just made it into a module and coded a CLI wrapping it. All credits to the author of the gist.
