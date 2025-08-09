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
uv add chrome-version
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

I needed to get the Chrome version for a project I was working on, which was using [Undetected Chromedriver][undetected-chromedriver]. I found [this gist][chrome-version-gist].

After using it in several projects, I decided to turn it into a module so I'll be free of copy/paste. It only have one functionality: getting the chrome version.

Then,

I decided to use this package to learn more about:

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

<!-- xc-heading -->
## Development

Clone the repository and cd into the project directory:

```sh
git clone https://github.com/hasansezertasan/hwid
cd hwid
```

The commands below can also be executed using the [xc task runner](https://xcfile.dev/), which combines the usage instructions with the actual commands. Simply run `xc`, it will popup an interactive menu with all available tasks.

### `pre-commit`

Run the pre-commit hooks:

```sh
uvx pre-commit run --all-files --hook-stage manual --show-diff-on-failure
```

### `checks`

Run all checks to ensure code quality:

```sh
uvx "validate-pyproject[all]" pyproject.toml
uvx typos
uvx vulture src
uvx ruff check
uvx taplo lint pyproject.toml
uvx ruff format
uvx taplo format pyproject.toml
uvx mypy src
uvx mypy --install-types --non-interactive src/chrome_version
```

### `docs:serve`

Serve the documentation locally:

```sh
uvx --with-requirements requirements.docs.txt --reinstall mkdocs serve
```

### `docs:build`

Build the documentation locally:

```sh
uvx --with-requirements requirements.docs.txt --reinstall mkdocs build
```

## Author

- [Hasan Sezer Taşan](https://www.github.com/hasansezertasan), It's me :wave:
- [Kory Becker](https://github.com/primaryobjects), owner of the original script.

## Disclaimer

Based on [chrome-version-gist] by [Kory Becker](https://github.com/primaryobjects).

This package provides a CLI wrapper for the original project. All credit reserved to the author of the original code.

## License

`chrome-version` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

<!-- Links -->
[undetected-chromedriver]: https://github.com/ultrafunkamsterdam/undetected-chromedriver
[chrome-version-gist]: https://gist.github.com/primaryobjects/d5346bf7a173dbded1a70375ff7461b4
