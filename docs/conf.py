"""Sphinx configuration for the uv-forge documentation."""

project = "uv-forge"
author = "bosd"
copyright = f"2026, {author}"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

html_theme = "shibuya"
html_title = "uv-forge"
html_static_path = ["_static"]
html_logo = "_static/uv-forge.webp"
html_favicon = "_static/favicon.png"
html_css_files = ["custom.css"]

# Warm amber/brass accent to match the steampunk logo and banner.
html_theme_options = {
    "accent_color": "amber",
    "github_url": "https://github.com/bosd/uv-forge",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
