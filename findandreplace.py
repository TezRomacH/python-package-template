"""
https://stackoverflow.com/questions/4205854/python-way-to-recursively-find-and-replace-string-in-text-files
"""

import os, fnmatch


def find_and_replace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)


if __name__ == "__main__":
    find_and_replace(
        ".",
        "TezRomacH/python-package-template",
        "william-cass-wright/cookiecutter-pypackage-slim",
        "*.md",
    )
