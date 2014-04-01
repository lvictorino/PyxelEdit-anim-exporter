#!/usr/bin/python

import zipfile
import json
import sys
import os.path
import os

if len(sys.argv) < 2:
    print "usage: pyxeledit-anim-exporter.py project.pyxel"
    sys.exit(0)

try:
    extracted = False
    project_name = ""
    file_path = sys.argv[1]
    # Unzip pyxel file
    zfile = zipfile.ZipFile(file_path)
    # List all files contained to find 'docData.json'
    for name in zfile.namelist():
        (dirname, filename) = os.path.split(name)
        if filename == "docData.json":

            try:
                # Extract docData.json from zip
                zfile.extract(name, dirname)
            except IOError:
                print "Error you're not allowed to create files in the current directory."
                sys.exit(1)

            # Load it as a JSON file
            json_data=open(name)
            pyxel_data=json.load(json_data)
            data = {}
            try:
                # Get interesting information for animations
                data['animations'] = pyxel_data['animations']
                data['tileset'] = pyxel_data['tileset']
                project_name = pyxel_data['name']
                # Create and fill a file named after the project name with animation properties
                exported_file = project_name + "-anim.json"
                with open(exported_file, 'w') as outfile:
                    json.dump(data, outfile)
                json_data.close()
                # Remove extracted file
                os.remove(name)
                extracted = True
            except KeyError:
                print "Error: the content of .pyxel file is not valid."
            break
    
    zfile.close()

    if extracted is not True:
        print "Error: the content of .pyxel file is not valid."
    else:
        print "Animation properties of " + project_name + " project have been successfully exported."

except IOError:
    print "Error: given file is not valid. Please give a .pyxel file as parameter."

