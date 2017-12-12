#! /usr/bin/python3 -B

import os
import shutil

PURGE = ["doctrees"]
FORMATS = {
    "html": "html",
#    "xelatexpdf": "latex",
}


if __name__ == "__main__":
    file = os.path.realpath(__file__)
    directory = os.path.dirname(file)
    os.chdir(directory)
    for build in PURGE + list(FORMATS.values()):
        try:
            shutil.rmtree(os.path.join("build", build))
        except:
            pass
    for make in reversed(sorted(FORMATS.keys())):
        os.system(" ".join(["make", make]))
