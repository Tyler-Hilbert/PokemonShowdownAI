# Calculates how often each type is generated

# FIXME - verify that calculated numbers are correct

# FIXME - how to deal with Arceus

# FIXME - are Alolas correct?

import sys
sys.path.insert(0, '../../SelectLead')
import Pokemon
import Pokedex

import json

DEBUG = False # If debug printing is on


f = open('../FormattedData.json',)
data = json.load(f)
f.close()

pokedex = Pokedex.Pokedex() # TODO - get all pokedex files in same location


typeAndCountLst = []
typeCount = 0 # Total number of types
debugCount = 0 # TODO - only used for debugging
for pkmn in data: # Loop through each generated pokemon
    if DEBUG:
        print (debugCount)
        print (pkmn['name'])
    debugCount += 1

    if pkmn['name'] == "Sirfetch’d": # FIXME - handle this in a cleaner way
        pkmn['name'] = "Sirfetchd"
        if DEBUG:
            print (pkmn['name'])
    elif pkmn['name'] == "Farfetch’d": # FIXME - handle this in a cleaner way
        pkmn['name'] = "Farfetchd"
        if DEBUG:
            print (pkmn['name'])


    if pkmn['name'] == "Urshifu":
        # TODO - verify this is being calculated correct
        pkmnTypes = ["Water", "Fighting", "Dark"]
    elif pkmn['name'] == "Zarude":
        # TODO - verify this is being calculated correct
        pkmnTypes = ["Grass", "Dark"]
    else:
        if DEBUG:
            print(Pokemon.getPokemonInStr(pkmn['name'], pokedex)[0].name)
            print(Pokemon.getPokemonInStr(pkmn['name'], pokedex)[0].types)
        pkmnTypes = Pokemon.getPokemonInStr(pkmn['name'], pokedex)[0].types # TODO - find better way of getting the pokemon's types

    for t in pkmnTypes:
        typeCount += 1
        found = False
        for i in range (len(typeAndCountLst)): # Loop through each type already counted
            # FIXME - verify this hits the last case
            if t == typeAndCountLst[i]['type']:
                typeAndCountLst[i]['count'] += 1
                found = True
                break
        if not found: # TODO - there are a limited number of types so it may be easier to hardcode them ahead of time
            typeAndCountLst.append({
                'type': t,
                'count': 1
            })


for i in range (len(typeAndCountLst)):
    # FIXME - verify this hits the last case
    s = typeAndCountLst[i]['type'] + " was generated " + str(typeAndCountLst[i]['count']) + " out of " + str(typeCount)
    print (s)
