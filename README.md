# Chrome Version

[![Coverage](https://img.shields.io/codecov/c/github/hasansezertasan/chrome-version)](https://codecov.io/gh/hasansezertasan/chrome-version)
[![PyPI - Version](https://img.shields.io/pypi/v/chrome-version.svg)](https://pypi.org/project/chrome-version)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/chrome-version.svg)](https://pypi.org/project/chrome-version)
[![License](https://img.shields.io/github/license/hasansezertasan/chrome-version.svg)](https://github.com/hasansezertasan/chrome-version/blob/main/LICENSE)
[![Latest Commit](https://img.shields.io/github/last-commit/hasansezertasan/chrome-version)](https://github.com/hasansezertasan/chrome-version)

[![Downloads](https://pepy.tech/badge/chrome-version)](https://pepy.tech/project/chrome-version)
[![Downloads/Month](https://pepy.tech/badge/chrome-version/month)](https://pepy.tech/project/chrome-version)
[![Downloads/Week](https://pepy.tech/badge/chrome-version/week)](https://pepy.tech/project/chrome-version)

Get the version of Chrome installed on Windows, Linux, Mac. Cross-platform using Python, native OS detection, does not require Selenium.

---

## Table of Contents

- [Chrome Version](#chrome-version)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Motivation](#motivation)
  - [Features](#features)
  - [Author](#author)
  - [Disclaimer](#disclaimer)
  - [License](#license)

## Installation

``` bash
pip install chrome-version
```

## Usage

Module:

```python
import chrome_version
print(chrome_version.get_chrome_version())
# '103.0.5060.114'
```

CLI:

```bash
chrome-version
103.0.5060.114
```

## Motivation

TL;DR I don't want to copy and paste it again...

At first,

I needed to get the Chrome version for a project I was working on, which was using [Undetected Chromedriver][untedected-chromedriver]. I found the gist below.

When I used it in a variaty of projects, I decided to turn it into a module so I'll be free of copy/paste. It only have one functionality: getting the chrome version.

Then,

I decided to use it to learn more about:

- Using [Poetry](https://python-poetry.org/) for packaging and dependency management.
- Using scripts for CLI.
- Versioning.
- License management.
- Documentation.
- Publishing a module on PyPI.
- Using GitHub Actions to automate the publishing process.
- ...

Finally,

Now it's kind of a playground for me to learn more...

One other thing is that it's educational: A simple module is a good practice for me to learn how to build modules and publish them on PyPI and show others how easy it is.

## Features

- Cross-platform
- No external dependencies
- CLI
- Module

## Author

- [Hasan Sezer Tasan](https://www.github.com/hasansezertasan), It's me :wave:
- [Kory Becker](https://github.com/primaryobjects), owner of the original script.

## Disclaimer

Based on [chrome-version](https://gist.github.com/primaryobjects/d5346bf7a173dbded1a70375ff7461b4) by [Kory Becker](https://github.com/primaryobjects).

This package provides a CLI wrapper for the original project. All credit reserved to the author of the original code.

## License

`chrome-version` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

<!-- Links -->
[untedected-chromedriver]: https://github.com/ultrafunkamsterdam/undetected-chromedriver
