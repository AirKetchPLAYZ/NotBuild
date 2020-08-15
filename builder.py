#! /usr/bin/python3

import importlib
import os
import sys
import csv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory",
                    help="the directory to build from", default=os.getcwd(), dest="dir")
parser.add_argument("addons", nargs="+",
                    help="the ids of the addons to use. Addon must be in addons.txt and have an addon with its id in building/addons")
args = parser.parse_args()
addonsu = args.addons
bd = args.dir
olddir = os.getcwd()
os.chdir(os.path.dirname(__loader__.get_filename()))
addonslist = []
for file in os.listdir("addons"):
    if (not os.path.isfile(os.path.join("addons", file))) or (not file.endswith(".py")):
        continue
    print("Found addon: " + file)
    addonslist.append(importlib.import_module('addons.' + file.rstrip('.py')))
os.chdir(olddir)
print('Addons loaded')
print('Building from: ' + bd)
if not os.path.isdir(bd):
    print('Error: No such directory')
    exit(1)
dir = os.path.abspath(bd)
if not os.path.isfile(os.path.join(dir, "addons.txt")):
    print('Error: No addons.txt found')
    exit(1)
addons = open(os.path.join(dir, "addons.txt"))
addons = addons.read().replace('\r', '').split('\n')
if not os.path.isfile(os.path.join(dir, "buildconfig.csv")):
    print('Error: No buildconfig.csv found')
    exit(1)
cfg = open(os.path.join(dir, "buildconfig.csv"))
cfgreader = csv.reader(cfg)
commands = []
for a in addons:
    if a.strip() == '': continue
    there = False
    for addon in addonslist:
        if addon.id == a:
            there = True
            break
    if not there:
        print("Error: addon defined in addons.txt not found: " + a)
        exit(1)
for a in addonslist:
    if a.id in addonsu and a.id in addons:
        addonsu.remove(a.id)
        os.chdir(dir)
        commands += a.pconfig(cfgreader)
        os.chdir(olddir)
if len(addonsu) > 0:
    print("Warn: The following addons were not found:\n" + ", ".join(addonsu))
for command in commands:
    print(command)
    if os.system(command) != 0:
        print('Error: Command returned a non-zero exit code')
        exit(1)
