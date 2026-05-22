"""Shared fixtures for the uv-forge template tests."""

from __future__ import annotations

import pytest


@pytest.fixture(scope="session")
def copier_template_paths() -> list[str]:
    """Copy only the template itself into pytest-copier's isolated template.

    Without this, pytest-copier copies the whole repo (including ``.git``) and its
    internal ``git commit`` fails on a clean checkout (e.g. in CI) with
    "nothing to commit".
    """
    return ["copier.yml", "template"]
