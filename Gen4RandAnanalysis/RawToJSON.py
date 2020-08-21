# Takes raw output piped from the modified pokemon-showdown file and converts it to valid json

FILE_TO_PROCESS = "raw.output"
OUT_FILE = "FormattedData.json"

with open(FILE_TO_PROCESS, 'r') as rfp:
    with open(OUT_FILE, 'w') as wfp:
        for line in rfp:
            # FIXME - verify none of these will ever be part of a Pokemon name or other piece of data
            line = line.replace("name:", '"name":')
            line = line.replace("species:", '"species":')
            line = line.replace("gender:", '"gender":')
            line = line.replace("moves:", '"moves":')
            line = line.replace("ability:", '"ability":')
            line = line.replace("evs:", '"evs":')
            line = line.replace("hp:", '"hp":')
            line = line.replace("atk:", '"atk":')
            line = line.replace("def:", '"def":')
            line = line.replace("spa:", '"spa":')
            line = line.replace("spd:", '"spd":')
            line = line.replace("spe:", '"spe":')
            line = line.replace("ivs:", '"ivs":')
            line = line.replace("item:", '"item":')
            line = line.replace("level:", '"level":')
            line = line.replace("shiny:", '"shiny":')

            # This is a quick hack that fixes the bug in SimulateTeamGeneration.py where every 6th pokemon is missing a ,
            line = line.replace("}", "},")
            line = line.replace("},,", "},")

            # Replace '  with "
            # FIXME - verify that the ' can just be replaced without causing any problems
            line = line.replace("'", '"')

            wfp.write(line)

# FIXME - very last comma needs to be deleted
