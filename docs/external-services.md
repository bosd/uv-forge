# External services

A generated project integrates with several services. Most work out of the box on GitHub; a few need
a one-time setup (an account, a repository secret, or a configured publisher).

## PyPI and TestPyPI

Releases publish to **PyPI** using **trusted publishing** (OIDC — no API token):

1. Create the project on PyPI (or let the first trusted-publishing upload create it).
2. Add a *trusted publisher* pointing at your repo's `release.yml` workflow and the `pypi`
   environment.

Pushes to `main` also publish to **TestPyPI**, which uses a token — add a `TEST_PYPI_TOKEN`
repository secret.

## Documentation hosting

Depending on the `docs_host` you chose:

- **Read the Docs** — import the repo at <https://readthedocs.org/>; it picks up `.readthedocs.yml`.
- **GitHub Pages** — the `docs.yml` workflow builds and deploys; enable Pages
  (Settings → Pages → Source: GitHub Actions).

## Codecov

Coverage is uploaded to [Codecov](https://about.codecov.io/) — add a `CODECOV_TOKEN` repository
secret.

## Built in (no setup)

- **GitHub Actions** — CI, release, labeler, and the weekly link check.
- **Dependabot** — dependency and action updates (config included; keeps the SHA-pinned actions
  current).
- **Sigstore** — release artifacts are signed via OIDC; no secret required.

## Secrets summary

| Secret | Needed for |
| --- | --- |
| `TEST_PYPI_TOKEN` | Publishing to TestPyPI on pushes to `main` |
| `CODECOV_TOKEN` | Uploading coverage to Codecov |

Production **PyPI** needs no secret — it uses trusted publishing.
