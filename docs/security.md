# Security

Generated projects are hardened by default. Here's the full picture.

## Static analysis

- **[zizmor](https://docs.zizmor.sh/)** — security static analysis for the GitHub Actions workflows:
  template injection, excessive permissions, credential persistence, unpinned actions, and cache
  poisoning. It runs as a pre-commit hook and in CI, and the generated workflows are zizmor-clean.
- **[actionlint](https://github.com/rhysd/actionlint)** — workflow correctness linting.
- **Ruff `flake8-bandit` (`S`) rules** — bandit-style Python security linting, part of the Ruff set.

## Supply-chain hardening

- Every GitHub Action is **pinned to a full commit SHA** (with a version comment), kept current by
  Dependabot.
- Workflows declare **least-privilege `permissions:`** and use **`persist-credentials: false`** on
  checkouts.

## Releases

- **Trusted publishing** to PyPI (OIDC) — no long-lived API tokens.
- **Sigstore** signing of the published artifacts.
- **SLSA build-provenance** attestations (verifiable with `gh attestation verify`).

## Reporting a vulnerability

Use your repository's private vulnerability reporting (GitHub → Security → "Report a vulnerability")
or a `SECURITY.md` policy for disclosures.
