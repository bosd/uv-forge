# uv-forge

A [Copier] template for forging modern, opinionated Python projects at high speed —
[uv] for everything, [Ruff], strict [mypy] (plus [ty]), [nox], 100% coverage, and a
hardened, SHA-pinned GitHub Actions setup with SLSA build provenance.

> Successor to [cookiecutter-uv-hypermodern-python][cc]. Unlike cookiecutter, Copier supports
> in-place updates (`copier update`), so generated projects can pull in template improvements later.

## Usage

```console
uvx --with jinja2-time copier copy --trust gh:bosd/uv-forge path/to/your-project
```

`jinja2-time` is needed for the `copyright_year` default; `--trust` is required because the template
uses a Jinja extension.

### Update an existing project

```console
cd your-project
uvx --with jinja2-time copier update --trust
```

## Options

| Question | Choices | Default | Effect |
| --- | --- | --- | --- |
| `extension` | `none`, `mypyc` | `none` | `none` → pure-Python (hatchling). `mypyc` → compiled wheels (setuptools + mypyc + cibuildwheel). *(Rust/PyO3 planned.)* |
| `docs_host` | `readthedocs`, `github-pages` | `readthedocs` | Read the Docs config, or a GitHub Pages build+deploy workflow. |
| `license` | MIT, Apache-2.0, GPL-3.0 | MIT | Project license. |

Plus the usual `project_name`, `package_name`, `author`, `email`, `github_user`, `version`,
`development_status`.

## What you get

- **uv** project management, **Ruff** lint+format, **mypy --strict**, **ty** (secondary), **pydoclint**.
- **nox** sessions (tests, mypy, ty, typeguard, xdoctest, docs); **pytest** with xdist + randomly; 100% coverage gate.
- **Sphinx** docs (shibuya theme) + a **non-blocking, weekly** link checker.
- **Hardened CI**: every action SHA-pinned, least-privilege permissions, `persist-credentials: false`,
  **zizmor** + **actionlint** pre-commit hooks.
- **Release**: trusted PyPI publishing (OIDC), Sigstore signing, and SLSA build-provenance attestations.

## License

MIT

[copier]: https://copier.readthedocs.io/
[uv]: https://docs.astral.sh/uv/
[ruff]: https://docs.astral.sh/ruff/
[mypy]: https://mypy.readthedocs.io/
[ty]: https://github.com/astral-sh/ty
[nox]: https://nox.thea.codes/
[cc]: https://github.com/bosd/cookiecutter-uv-hypermodern-python
