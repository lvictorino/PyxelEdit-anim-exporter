#!/usr/bin/python
import zipfile
import sys
import os.path
import os

if len(sys.argv) < 2:
    print "usage: pyxeledit-anim-exporter.py project.pyxel"
    sys.exit

file_path = sys.argv[1]
zfile = zipfile.ZipFile(file_path)
for name in zfile.namelist():
    (dirname, filename) = os.path.split(name)
    if filename == "docData.json":
        print "Decompressing " + filename
        zfile.extract(name, dirname)




