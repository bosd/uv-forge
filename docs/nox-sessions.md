# Nox sessions

Generated projects use [nox](https://nox.thea.codes/) as the task runner, with **uv** as the
backend. List everything:

```console
uv run nox -l
```

Run the default suite (what CI runs):

```console
uv run nox
```

Run a single session, optionally pinned to a Python version:

```console
uv run nox -s tests
uv run nox -s tests -p 3.13
```

## Default sessions

These run with a bare `uv run nox` and in CI.

`pre-commit`
: Lint and format everything — Ruff (lint + format), pydoclint, ty, zizmor and actionlint on the
workflows, prettier, and the file-hygiene hooks.

`mypy`
: Strict static type checking across all supported Python versions.

`ty`
: [Astral's ty](https://github.com/astral-sh/ty) as a fast secondary type check. mypy stays the
authoritative checker.

`tests`
: The pytest suite across all supported Python versions, in parallel (`pytest-xdist`) and in random
order (`pytest-randomly`).

`typeguard`
: Runs the tests with runtime type checking enabled.

`xdoctest`
: Executes the examples embedded in your docstrings.

`docs-build`
: Builds the Sphinx documentation once (HTML).

## On-demand sessions

Not part of the default suite — run them explicitly.

`coverage`
: Combines coverage data and prints the report; enforces the **100%** gate.

`docs`
: Serves the docs locally with live reload (`sphinx-autobuild`) — handy while writing docs.

`docs-linkcheck`
: Checks external documentation links. Runs **weekly** (and on demand) via the `linkcheck`
workflow — never on pull requests, so a flaky external link can't block a merge.

`tests_compiled`
: _Only when `extension=mypyc`._ Builds the mypyc C extension and runs the suite against the
compiled build.
