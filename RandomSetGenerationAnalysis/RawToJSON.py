# Takes raw output piped from the modified pokemon-showdown file and converts it to valid json

FILE_TO_PROCESS = "raw.output"
TEMP_FILE = "temp.psuedojson" # USED FOR DEBUGGING
OUT_FILE = "FormattedData.json"

lines = []

with open(FILE_TO_PROCESS, 'r') as rfp:
    with open(TEMP_FILE, 'w') as wfp:
        for line in rfp:
            # FIXME - verify none of these parsings will ever mess up data

            # Replace Keys
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
            line = line.replace("gigantamax:", '"gigantamax":')

            # This is a quick hack that fixes the bug in SimulateTeamGeneration.py where every 6th pokemon is missing a ,
            line = line.replace("}", "},")
            line = line.replace("},,", "},")

            # Replace pokemon names that are different in the random set generation than the
            # TODO - is this programmed somewhere in the source code that I can use rather than writting myself?
            line = line.replace("Mr. Mime", "mrmime")
            line = line.replace("Mr. Rime", "mrrime")
            line = line.replace("Tapu Lele", "tapulele")
            line = line.replace("Tapu Fini", "tapufini")
            line = line.replace("Tapu Koko", "tapukoko")
            line = line.replace("Tapu Bulu", "tapubulu")
            line = line.replace("Kommo-o", "kommoo")
            line = line.replace("Type: Null", "typenull")
            line = line.replace("Ho-Oh", "hooh")

            # Replace '  with "
            # FIXME - verify that the ' can just be replaced without causing any problems
            line = line.replace("'", '"')

            wfp.write(line)
            lines.append(line)


index = 0
while index != len(lines)-1:
    if ']' in lines[index] and '[' in lines[index+1]: # Remove every 6th open close bracket
        lines.pop(index+1)
        lines.pop(index)
    index += 1

lines[-2] = "}" # Remove comma


with open(OUT_FILE, 'w') as wfp:
    for l in lines:
        wfp.write(l)
