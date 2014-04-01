#!/usr/bin/python
import zipfile
import json
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
        zfile.extract(name, dirname)
        json_data=open(name)
        pyxel_data=json.load(json_data)
        data = {}
        data['animations'] = pyxel_data['animations']
        data['tileset'] = pyxel_data['tileset']
        exported_file = pyxel_data['name'] + "-anim.json"
        print "Creation of " + exported_file + "..."
        with open(exported_file, 'w') as outfile:
            json.dump(data, outfile)
        json_data.close()
        os.remove(name)
        print "Animation properties of " + pyxel_data['name'] + " project have been successfully exported."
zfile.close()



