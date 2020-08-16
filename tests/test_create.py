from pytest import fail
from tempfile import TemporaryDirectory
from shutil import rmtree
from pyroot.project import Project


def test_project_create():

    with TemporaryDirectory() as proj_dir:
        # Must fail when creating with existing dir
        proj = Project("test_project", proj_dir)
        try:
            proj.create()
        except SystemExit:
            pass
        else:
            fail("did not exist on existying dir")
        proj = Project("test_project", proj_dir)
        # Should continue if force is used
        proj.create(force=True)

    # Test regular creation
    proj = Project("test_project", proj_dir)
    proj.create()
    rmtree(proj_dir)
