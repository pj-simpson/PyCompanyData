import toml

from pycompanydata import __version__


def test_version():
    project_metadata = toml.load("./pyproject.toml")
    assert __version__ == project_metadata["tool"]["poetry"]["version"]
