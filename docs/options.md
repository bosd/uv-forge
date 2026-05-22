# Options

Copier prompts for these (defaults in parentheses):

| Question                         | Choices / form                           | Effect                                              |
| -------------------------------- | ---------------------------------------- | --------------------------------------------------- |
| `project_name`                   | string (`my-package`)                    | Distribution name; also the default for the others. |
| `package_name`                   | string (derived)                         | Importable package under `src/`.                    |
| `friendly_name`                  | string (derived)                         | Human-friendly title used in docs/metadata.         |
| `author`, `email`, `github_user` | strings                                  | Project metadata and URLs.                          |
| `version`                        | string (`0.0.0`)                         | Initial version.                                    |
| `license`                        | MIT / Apache-2.0 / GPL-3.0 (MIT)         | Generates the matching `LICENSE`.                   |
| `development_status`             | classifier (Alpha)                       | PyPI "Development Status" classifier.               |
| `docs_host`                      | readthedocs / github-pages (readthedocs) | Documentation **host** (see below).                 |
| `extension`                      | none / mypyc (none)                      | Compiled-**extension** strategy (see below).        |

## `extension`

- **`none`** (default) — pure-Python. Build backend is **Hatchling**; release builds a universal
  wheel + sdist with `uv build` and publishes via trusted publishing (with Sigstore + provenance).
- **`mypyc`** — compiled wheels. Build backend is **setuptools**, `setup.py` compiles `core.py` with
  mypyc, a `tests_compiled` nox session runs against the C extension, and the release workflow uses
  **cibuildwheel** to build per-platform wheels.

## `docs_host`

The docs are built with Sphinx either way; this chooses where they're served:

- **`readthedocs`** — ships a `.readthedocs.yml`; import the repo on Read the Docs.
- **`github-pages`** — ships a `docs.yml` workflow that builds and deploys to GitHub Pages.
