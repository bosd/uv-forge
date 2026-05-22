# Contributing

uv-forge is a [Copier](https://copier.readthedocs.io/) template. The files that get rendered into
generated projects live under `template/`; template variables use `{{ variable }}` and templated
filenames use a `.jinja` suffix.

## Make a change

1. Edit files under `template/` (or `copier.yml` to add/change a question).
2. Generate a project and run its checks:

   ```console
   uvx --with jinja2-time copier copy --defaults --trust --vcs-ref HEAD . /tmp/out
   cd /tmp/out && git init -q && git add -A && git commit -qm init
   uv run nox
   ```

3. Repeat for the toggle combinations you touched (`extension`, `docs_host`, `license`). CI runs the
   full matrix.

## Notes

- Workflow files with no template variables are kept static (literal `${{ }}` is fine); only files
  that interpolate Copier variables carry a `.jinja` suffix.
- Keep GitHub Actions SHA-pinned and the workflows `zizmor`-clean.
