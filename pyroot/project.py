from os import makedirs, chdir, getcwd, system
from sys import stderr
from pathlib import Path
from shutil import rmtree
from pkg_resources import resource_filename
from zipfile import ZipFile
from .template import Adjustments


class Project:
    def __init__(self, name: str, project_dir: str):
        self._project_dir = project_dir
        self._name = name or Path(project_dir).name

    def create(self, force=False):
        proj_dir = self._project_dir
        print(f"Creating project {self._name} at {proj_dir}")
        self._make_dir(proj_dir, force)

        template_zip = resource_filename(__name__, "template.zip")
        with ZipFile(template_zip) as zip_file:
            zip_file.extractall(proj_dir)
        adj = Adjustments(proj_dir, self._name)
        adj.run()
        self._git_init()

    @staticmethod
    def _run(command):
        rc = system(command)
        if rc != 0:
            exit(rc)

    def _git_init(self):
        cwd = getcwd()
        chdir(self._project_dir)
        self._run("git init")
        self._run("git add .")
        self._run("git commit -m 'Initial commit'")
        chdir(cwd)

    @staticmethod
    def _make_dir(path, force):
        try:
            makedirs(path)
        except FileExistsError:
            if not force:
                print(f"Directory {path} already exists", file=stderr)
                exit(2)
            else:
                rmtree(path)
