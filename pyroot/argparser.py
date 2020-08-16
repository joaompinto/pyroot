from optparse import OptionParser
from setuptools_scm import get_version


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
    parser.add_option(
        "-n", "--name", dest="name", default=None, help="name of the package"
    )
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    return (options, args)
