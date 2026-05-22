# Project overview

uv-forge generates a complete, opinionated Python project so you can start writing code instead of
wiring up tooling. It's a [Copier](https://copier.readthedocs.io/) template — the maintained
successor to the cookiecutter "hypermodern Python" line — built around the fast, Rust-based
[Astral](https://astral.sh/) toolchain (uv, Ruff, ty) alongside mypy, nox, and Sphinx.

## Goals

- **Batteries included, opinionated.** A generated project ships linting, formatting, typing,
  testing with 100% coverage, docs, and a release pipeline that already works.
- **Maintained and updatable.** Because it's Copier, you can `copier update` an existing project to
  pull in template improvements — something cookiecutter can't do. A goal is to consolidate the
  scattered, often-unmaintained hypermodern-python forks into one well-kept template.
- **Secure by default.** Workflows are SHA-pinned and least-privilege, linted with zizmor and
  actionlint; releases use trusted publishing, Sigstore signing, and SLSA build provenance.

## Options at a glance

uv-forge asks a few questions when generating (see [Options](options.md)):

- `extension` — pure-Python (Hatchling) or **mypyc**-compiled wheels.
- `docs_host` — Read the Docs or GitHub Pages.
- `license` — MIT, Apache-2.0, or GPL-3.0.

## License

uv-forge itself is distributed under the **MIT license**. Generated projects get whichever license
you pick from the `license` question.
