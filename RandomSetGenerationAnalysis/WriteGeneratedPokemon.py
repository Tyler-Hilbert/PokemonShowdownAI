# Creates a file for each pokemon with each generated set

# FIXME - clear out GeneratedGen8Pokemon directory

# FIXME - Verify that no sets accidently got deleted and that there are no duplicates


import json
import os


OUT_FILE_PATH = "GeneratedGen8Pokemon/"
DATA_FILE = "FormattedData.json"
TEMP_FILE = OUT_FILE_PATH + "temp"


f = open(DATA_FILE,)
data = json.load(f)
f.close()




for pkmn in data:
    filename = OUT_FILE_PATH + pkmn['name']
    with open(filename, 'a') as wfp:
        pkmn['moves'].sort()
        wfp.write(json.dumps(pkmn))
        wfp.write("\n")

    # Remove duplicate lines
    # TODO - it would be better to just not write pokemon that are duplicates rather than remove them from the file after writing them
    lines_seen = set() # holds lines already seen
    outfile = open(TEMP_FILE, "w")
    for line in open(filename, "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    os.remove(filename)
    os.rename(TEMP_FILE, filename)
