from optparse import OptionParser
from setuptools_scm import get_version
from .project import Project


def arg_parser():
    usage = "usage: %prog [options] project_dir"
    version = f"%prog {get_version()}"
    parser = OptionParser(usage, version=version)
    parser.add_option(
        "-f",
        "--force",
        action="store_true",
        dest="force",
        default=False,
        help="overwrite existing directory",
    )
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    return (options, args)


def main():
    options, args = arg_parser()
    project_dir = args[0]
    proj = Project(project_dir)
    proj.create(options.force)


if __name__ == "__main__":
    main()
