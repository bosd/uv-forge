"""Sphinx configuration for the uv-forge documentation."""

project = "uv-forge"
author = "bosd"
copyright = f"2026, {author}"
extensions = [
    "myst_parser",
    "sphinx_copybutton",
]
html_theme = "shibuya"
html_static_path = ["_static"]
html_logo = "_static/uv-forge.png"
html_title = "uv-forge"
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
