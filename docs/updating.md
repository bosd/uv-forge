# Updating an existing project

Copier records your answers in `.copier-answers.yml`. When uv-forge improves, pull the changes into
your project:

```console
cd your-project
uvx --with jinja2-time copier update --trust
```

Copier re-renders the template with your saved answers, computes a diff against the version you
generated from, and applies it — prompting you to resolve any conflicts with files you've edited,
just like a Git merge. Commit the result.

To answer the questions again (for example, to switch `docs_host`):

```console
uvx --with jinja2-time copier update --trust --defaults=false
```

> Keep `.copier-answers.yml` committed and unmodified by hand — it's how `copier update` knows where
> you started from. The generated `.pre-commit-config.yaml` already excludes it from formatting.
