from pyroot.project import Project
from tempfile import TemporaryDirectory
from shutil import rmtree


def test_project_create():

    with TemporaryDirectory() as proj_dir:
        # Must fail when creating one xisting dir
        proj = Project("test_project", proj_dir)
        try:
            proj.create()
        except SystemExit:
            pass
        else:
            raise Exception
        proj = Project("test_project", proj_dir)
        # Should continue if force is used
        proj.create(force=True)

    # Test regular creation
    proj = Project("test_project", proj_dir)
    proj.create()
    rmtree(proj_dir)
