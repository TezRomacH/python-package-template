"""
https://stackoverflow.com/questions/4205854/python-way-to-recursively-find-and-replace-string-in-text-files

** MAKE SURE TO RUN THIS SCRIPT FROM THE SCRIPTS DIRECTORY **
"""

import os, fnmatch


def find_and_replace(directory, find, replace, filePattern):
    abs_dir = os.path.abspath(directory)
    print(abs_dir)
    for path, dirs, files in os.walk(abs_dir):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)


if __name__ == "__main__":
    find_and_replace(
        "../.",
        "william-cass-wright/cookiecutter-pypackage-slim",
        "william-cass-wright/cookiecutter-pypackage-slim",
        "*.toml", # "*.md", "*.json", "*.toml",
    )
