# Takes the outputted formatted data and does post processing to get the data in a format python understands

FILE_TO_PROCESS = "OutputSubset.output"
OUT_FILE = "OutputData_data.py"

with open(FILE_TO_PROCESS, 'r') as rfp:
    with open(OUT_FILE, 'w') as wfp:
        wfp.write ("generatedSets = [\n")
        for line in rfp:
            # FIXME - verify none of these will ever be part of a Pokemon name or other piece of data
            line = line.replace("name:", "'name':")
            line = line.replace("species:", "'species':")
            line = line.replace("gender:", "'gender':")
            line = line.replace("moves:", "'moves':")
            line = line.replace("ability:", "'ability':")
            line = line.replace("evs:", "'evs':")
            line = line.replace("hp:", "'hp':")
            line = line.replace("atk:", "'atk':")
            line = line.replace("def:", "'dfs':")
            line = line.replace("spa:", "'spa':")
            line = line.replace("spd:", "'spd':")
            line = line.replace("spe:", "'spe':")
            line = line.replace("ivs:", "'ivs':")
            line = line.replace("item:", "'item':")
            line = line.replace("level:", "'level':")

            wfp.write(line)
        wfp.write ("]")
