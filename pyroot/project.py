from os import mkdir
from sys import stderr
from pathlib import Path


class Project:
    def __init__(self, name: str, project_dir: str):
        self._project_dir = project_dir
        self._name = name or Path(project_dir).basename()

    def create(self, force=False):
        proj_dir = self._project_dir
        print(f"Creating project {self._name} at {proj_dir}")
        try:
            mkdir(proj_dir)
        except FileExistsError:
            if not force:
                print(f"Directory {proj_dir} already exists", file=stderr)
                exit(2)
