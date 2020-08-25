# Creates a file for each pokemon with each generated set

# FIXME - clear out GeneratedGen8Pokemon directory

# FIXME - don't write duplicate entries


OUT_FILE_PATH = "GeneratedGen8Pokemon/"
DATA_FILE = "FormattedData.json"


import json

f = open(DATA_FILE,)
data = json.load(f)
f.close()




for pkmn in data:
    filename = OUT_FILE_PATH + pkmn['name']
    with open(filename, 'a') as wfp:
        wfp.write(json.dumps(pkmn))
        wfp.write("\n")
