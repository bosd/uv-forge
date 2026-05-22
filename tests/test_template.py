"""Tests for the uv-forge Copier template.

Uses pytest-copier's ``copier`` fixture to render the template with various
answers and assert on the result. ``copier.copy`` runs the template's tasks
(``uv lock``), so each case also exercises lockfile generation.
"""

from __future__ import annotations

from pathlib import Path

import pytest


def test_defaults_render(copier, tmp_path: Path) -> None:
    """Default answers produce a pure-Python (hatchling) project with a lockfile."""
    project = copier.copy(tmp_path / "default")
    assert (project / "pyproject.toml").exists()
    assert (project / "uv.lock").exists()
    assert (project / ".readthedocs.yml").exists()
    assert not (project / "setup.py").exists()
    assert not (project / ".github/workflows/docs.yml").exists()
    assert (
        'build-backend = "hatchling.build"' in (project / "pyproject.toml").read_text()
    )
    assert (project / "src/my_package/__init__.py").exists()


def test_mypyc_extension(copier, tmp_path: Path) -> None:
    """``extension=mypyc`` switches to setuptools + setup.py + cibuildwheel."""
    project = copier.copy(tmp_path / "mypyc", extension="mypyc")
    assert (project / "setup.py").exists()
    assert "setuptools.build_meta" in (project / "pyproject.toml").read_text()
    assert "cibuildwheel" in (project / ".github/workflows/release.yml").read_text()


def test_github_pages_docs(copier, tmp_path: Path) -> None:
    """``docs_host=github-pages`` adds docs.yml and drops .readthedocs.yml."""
    project = copier.copy(tmp_path / "pages", docs_host="github-pages")
    assert (project / ".github/workflows/docs.yml").exists()
    assert not (project / ".readthedocs.yml").exists()


@pytest.mark.parametrize(
    ("license_id", "marker"),
    [
        ("MIT", "MIT License"),
        ("Apache-2.0", "Apache License"),
        ("GPL-3.0", "GNU General Public License"),
    ],
)
def test_license_choice(copier, tmp_path: Path, license_id: str, marker: str) -> None:
    """Each license choice renders the matching LICENSE file."""
    project = copier.copy(tmp_path / "lic", license=license_id)
    assert marker.lower() in (project / "LICENSE").read_text().lower()


def test_package_name_derived(copier, tmp_path: Path) -> None:
    """package_name is derived from a dashed project_name."""
    project = copier.copy(tmp_path / "named", project_name="my-cool-tool")
    assert (project / "src/my_cool_tool/__init__.py").exists()
