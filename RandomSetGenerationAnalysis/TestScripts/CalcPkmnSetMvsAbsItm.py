# Locates Pokemon in json file and counts number of times each move is selected along with abilities and items

import json

# Input variables
DATA_FILE = "../FormattedData.json"
PKMN_NAME = "Charizard"

# Read json output from RawToJSON.py
f = open(DATA_FILE,)
data = json.load(f)
f.close()

# Count moves, abilities and items
moves = []
abilities = []
items = []
for pkmn in data: # Loop through each generated Pokemon
    if pkmn['species'].lower().strip() == PKMN_NAME.lower().strip():
        # Count moves
        for m in pkmn['moves']: # Loop through each generated move
            moveFound = False
            for i in range(len(moves)):
                if moves[i]['name'].lower().strip() == m.lower().strip():
                    moveFound = True
                    moves[i]['count'] += 1
            if not moveFound:
                moves.append({'name': m, 'count': 1})


        # Count abilities
        abilityFound = False
        for i in range(len(abilities)):
            if abilities[i]['name'].lower().strip() == pkmn['ability'].lower().strip():
                abilityFound = True
                abilities[i]['count'] += 1
        if not abilityFound:
            abilities.append({'name': pkmn['ability'].lower().strip(), 'count': 1})

        # Count items
        itemFound = False
        for i in range(len(items)):
            if items[i]['name'].lower().strip() == pkmn['item'].lower().strip():
                itemFound = True
                items[i]['count'] += 1
        if not itemFound:
            items.append({'name': pkmn['item'].lower().strip(), 'count': 1})

print (moves)
print (abilities)
print (items)
