# Making a release

Releases are automated by the `release.yml` workflow. The version lives in `pyproject.toml`, and the
release notes are drafted automatically by
[Release Drafter](https://github.com/release-drafter/release-drafter).

## Flow

1. **Merge your pull requests.** Release Drafter keeps a _draft_ GitHub Release up to date with the
   changes since the last release, categorized by PR labels.
2. **Bump the version** in `pyproject.toml` and merge that change.
3. **Publish the draft release** on GitHub (Releases → edit the draft → Publish). Publishing creates
   the tag and triggers the release workflow.
4. The workflow then:
   - builds the distributions (`uv build`, or per-platform wheels via **cibuildwheel** when
     `extension=mypyc`);
   - generates **SLSA build-provenance** attestations;
   - **signs** the artifacts with Sigstore and attaches the signatures to the release;
   - **publishes to PyPI** via trusted publishing.

Every push to `main` also publishes to **TestPyPI**, so you can verify a build before cutting the
real release.

## Versioning

Projects follow [Semantic Versioning](https://semver.org/), starting from the `version` you chose
(default `0.0.0`). Bump it in `pyproject.toml` before publishing the release.

## Changelog

The changelog _is_ your project's **GitHub Releases** page — Release Drafter maintains it, and the
generated `pyproject.toml` points its `Changelog` URL there. (For uv-forge itself, that's
<https://github.com/bosd/uv-forge/releases>.)
