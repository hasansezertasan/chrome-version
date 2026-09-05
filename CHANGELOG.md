# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to [Semantic Versioning].

## [0.5.0](https://github.com/hasansezertasan/chrome-version/compare/0.4.0...v0.5.0) (2026-09-05)


### ⚠ BREAKING CHANGES

* adopt copier-pyproject template for project tooling ([#66](https://github.com/hasansezertasan/chrome-version/issues/66))

### 🚀 Features

* adopt copier-pyproject template for project tooling ([#66](https://github.com/hasansezertasan/chrome-version/issues/66)) ([b6c84ed](https://github.com/hasansezertasan/chrome-version/commit/b6c84edd043a47a5affef7e1c4270a57224f11e2))


### 🐛 Bug Fixes

* **typing:** resolve mypy no-redef and missing _version stub errors ([#55](https://github.com/hasansezertasan/chrome-version/issues/55)) ([ed3ecc9](https://github.com/hasansezertasan/chrome-version/commit/ed3ecc92b9fa38920745c991d3704861e280c2b9))


### ♻️ Refactoring

* **overall:** refactor code structure for improved readability and maintainability ([#42](https://github.com/hasansezertasan/chrome-version/issues/42)) ([ab94391](https://github.com/hasansezertasan/chrome-version/commit/ab943915c502b336528de9a62c03e57205734932))

## [0.4.0] - 2025-08-09

### 🚀 Features

- ref(project-structure): use src layout, uv, hatch, release-drafter, more generic `.gitignore`, semantic-pull-requests action, etc by @hasansezertasan in (#28)

### 👷 Continuous Integration

- Bump peaceiris/actions-gh-pages from 3 to 4 by @[dependabot[bot]](https://github.com/apps/dependabot) in (#19)
- Bump actions/setup-python from 4 to 5 by @[dependabot[bot]](https://github.com/apps/dependabot) in (#13)
- Bump actions/checkout from 3 to 4 by @[dependabot[bot]](https://github.com/apps/dependabot) in (#14)

### 📦 Dependencies

- Bump peaceiris/actions-gh-pages from 3 to 4 by @[dependabot[bot]](https://github.com/apps/dependabot) in (#19)
- Bump actions/setup-python from 4 to 5 by @[dependabot[bot]](https://github.com/apps/dependabot) in (#13)
- Bump actions/checkout from 3 to 4 by @[dependabot[bot]](https://github.com/apps/dependabot) in (#14)

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
[0.4.0]: https://github.com/hasansezertasan/chrome-version/compare/0.3.1...0.4.0
[0.3.1]: https://github.com/hasansezertasan/chrome-version/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/hasansezertasan/chrome-version/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/hasansezertasan/chrome-version/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/hasansezertasan/chrome-version/releases/tag/0.1.0
