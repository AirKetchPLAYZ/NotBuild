#! /usr/bin/python3
# Creates a new project

i = input("Project name: ")
import os
import sys
import zipfile
import importlib
os.mkdir(i)
with zipfile.ZipFile(os.path.join(os.path.dirname(__loader__.get_filename()), "npc.zip")) as z:
    os.chdir(i)
    open("buildconfig.csv","w+").close()
    z.extract("builder.py")
    os.mkdir("building")
    os.rename("builder.py", "building/builder.py")
    with open("addons.txt", "w+") as fi:
        for f in z.namelist():
            if f.startswith("addons/") and f != "addons/" and f.endswith(".py"):
                i = input("Add addon " + f[7:] + "? (y for yes, anything else for no)")
                if i == "y":
                    z.extract(f)
                    sys.path.append(os.getcwd())
                    importlib.invalidate_caches()
                    thingy = importlib.import_module("addons." + f[7:].rstrip(".py").strip())
                    fi.write(thingy.id + "\n")
                    del thingy
                    print("Added")

    os.rename("addons", "building/addons")
