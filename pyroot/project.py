from os import makedirs
from sys import stderr
from pathlib import Path
from shutil import rmtree, copyfile
import pkg_resources


BASE_FILES = """
LICENSE
pyproject.toml
README.md
requirements-dev.txt
requirements.txt
setup.cfg
setup.py
tox.ini
"""


class Project:
    def __init__(self, name: str, project_dir: str):
        self._project_dir = project_dir
        self._name = name or Path(project_dir).basename()

    def create(self, force=False):
        proj_dir = self._project_dir
        print(f"Creating project {self._name} at {proj_dir}")
        try:
            makedirs(proj_dir)
        except FileExistsError:
            if not force:
                print(f"Directory {proj_dir} already exists", file=stderr)
                exit(2)
            rmtree(proj_dir)
            makedirs(proj_dir)
        script_dir = Path(Path(__file__).parent, "..")

        print(pkg_resources.resource_filename(__name__, "template.zip"))
        exit(0)

        for filename in BASE_FILES.splitlines():
            if filename:
                copyfile(Path(script_dir, filename), Path(proj_dir, filename))
