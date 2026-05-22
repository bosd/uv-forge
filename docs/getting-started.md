# Getting started

## Prerequisites

You only need [uv](https://docs.astral.sh/uv/); it runs Copier for you via `uvx`.

## Generate a project

```console
uvx --with jinja2-time copier copy --trust gh:bosd/uv-forge path/to/your-project
```

- `--with jinja2-time` provides the `copyright_year` default.
- `--trust` is required because the template uses a Jinja extension.

Copier will ask a few questions (see [Options](options.md)) and write the project, recording your
answers in `.copier-answers.yml` so you can [update](updating.md) later.

## First steps in the new project

```console
cd path/to/your-project
git init && git add -A && git commit -m "Initial commit"
uv run nox            # pre-commit, mypy, ty, tests, typeguard, xdoctest, docs-build
```

Push to GitHub and the bundled workflows (tests, release, docs, labeler, weekly link check) take it
from there.
