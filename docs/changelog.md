# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to [Semantic Versioning].

## [Unreleased]

- Nothing yet.

## [0.3.1] - 2023-12-31

### Changed

- `README.md`: Updated `disclaimer` and `installation` section.

## [0.3.0] - 2023-09-30

### Changed

- `README.md`
- `pyproject.toml`
- Python Version Support range is changed to `^3.6` from `^3.8`.

### Added

- Simple CLI Tool to get the Chrome version with zero dependencies.

### Removed

- CLI Tool wrapping the module with typer is removed.
- Optional dependency `typer` for CLI Tool is removed.

## [0.2.0] - 2023-09-16

### Added

- Module itself with poetry.
- CLI Tool wrapping the module with typer.
- Optional dependency `typer` for CLI Tool.
- MkDocs for documentation.
- GitHub Actions:
  - Generate Documentation.
  - Publish to PyPI.
- Dependabot for dependency management.
- Funding options for GitHub Sponsors.

### Changed

- `README.md` to include installation and usage instructions.
- Dependencies to fit the project.

## [0.1.0] - 2023-09-08

- initial release

### Added

- Project Structure
- Hello World CLI Tool.
- Pre Commit Hooks
- `CHANGELOG.md`
- `README.md`
- `LICENSE`

<!-- Links -->
[keep a changelog]: https://keepachangelog.com/en/1.1.0/
[semantic versioning]: https://semver.org

<!-- Versions -->
[unreleased]: https://github.com/hasansezertasan/chrome-version/compare/0.3.0...HEAD
[0.3.1]: https://github.com/hasansezertasan/chrome-version/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/hasansezertasan/chrome-version/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/hasansezertasan/chrome-version/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/hasansezertasan/chrome-version/releases/tag/0.1.0
