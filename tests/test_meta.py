"""
Run meta tests on package (apply to muliple packages)

"""
from pathlib import Path

import lock_defaults as package
import toml


def test_versions_are_in_sync():
    """Checks if the pyproject.toml and package.__init__.py __version__ are in sync."""

    path = Path(__file__).resolve().parents[1] / "pyproject.toml"
    pyproject = toml.loads(open(str(path), encoding="utf-8").read())
    pyproject_version = pyproject["tool"]["poetry"]["version"]

    package_init_version = package.__version__

    assert package_init_version == pyproject_version
