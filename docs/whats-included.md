# What you get, and why

A generated project is opinionated so you can start writing code immediately.

## Tooling

- **[uv](https://docs.astral.sh/uv/)** — one fast tool for environments, dependencies, builds, and
  publishing. `nox` uses it as its backend.
- **[Ruff](https://docs.astral.sh/ruff/)** — linter *and* formatter, with a broad rule set
  (bugbear, simplify, pathlib, perflint, comprehensions, and more).
- **[mypy](https://mypy.readthedocs.io/) `--strict`** — the authoritative type checker, plus
  **[ty](https://github.com/astral-sh/ty)** as a fast secondary check.
- **[pydoclint](https://github.com/jsh9/pydoclint)** — keeps Google-style docstrings honest.
- **[pytest](https://docs.pytest.org/)** with `pytest-xdist` (parallel) and `pytest-randomly`
  (random order), and a **100% coverage** gate.
- **[nox](https://nox.thea.codes/)** sessions tie it together; **[Sphinx](https://www.sphinx-doc.org/)**
  (shibuya theme) builds the docs.

## Hardened CI/CD

- Every GitHub Action is **pinned to a commit SHA** (Dependabot keeps them current), with
  least-privilege `permissions:` and `persist-credentials: false`.
- **[zizmor](https://docs.zizmor.sh/)** and **actionlint** lint the workflows (pre-commit + CI).
- **Release**: trusted PyPI publishing (OIDC, no tokens), **Sigstore** signing, and **SLSA build
  provenance** attestations.
- **Link checking** runs **weekly and non-blocking** — a flaky external link never blocks a merge.
