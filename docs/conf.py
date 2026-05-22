"""Sphinx configuration for the uv-forge documentation."""

project = "uv-forge"
author = "bosd"
copyright = f"2026, {author}"
extensions = [
    "myst_parser",
    "sphinx_copybutton",
]
html_theme = "shibuya"
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
