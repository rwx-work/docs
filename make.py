#! /usr/bin/python3 -B

import os
import shutil
import subprocess

FORMATS = {
    "html": "docs",
    "latex": "doc",
}
INPUT = "in"
OUTPUT = "out"


def run(*arguments):
    return subprocess.call(arguments)


def main():
    script_file = os.path.realpath(__file__)
    project_directory = os.path.dirname(script_file)
    os.chdir(project_directory)
    shutil.rmtree(OUTPUT, ignore_errors=True)
    for f, name in reversed(sorted(FORMATS.items())):
        run("sphinx-build",
            "-b", f,
            "-c", os.curdir,
            "-j", "2",
            "-D", "latex_paper_size=a4",
            INPUT, os.path.join(OUTPUT, name))


if __name__ == "__main__":
    main()
