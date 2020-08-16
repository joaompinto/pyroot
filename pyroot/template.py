import re
import io
from zipfile import ZipFile
from pathlib import Path
from fileinput import FileInput


def create_zip():
    SCRIPT_DIR = Path(__file__).parent

    # Get readme
    template_files_path = Path(SCRIPT_DIR, "template_files.txt")
    with io.open(template_files_path, encoding="utf8") as f:
        file_list = f.read().splitlines()

    with ZipFile(Path("pyroot", "template.zip"), "w") as zipfile:
        for filename in file_list:
            if filename:
                zipfile.write(filename)


class Adjustments:
    def __init__(self, path):
        self._path = path

    def _delete_line(self, filename, del_line):
        filename = Path(self._path, filename)
        matched = re.compile(del_line).search
        with FileInput(filename, inplace=1, backup=".bak") as file:
            for line in file:
                if not matched(line):  # save lines that do not match
                    print(line, end="")  # this goes to filename due to inplace=1

    def run(self):
        self._delete_line("setup.py", "create_zip")
