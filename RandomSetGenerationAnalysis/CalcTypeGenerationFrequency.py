# Calculates how often each type is generated

# FIXME - verify that calculated numbers are correct

# FIXME - how to deal with Arceus

import sys
sys.path.insert(0, '../SelectLead')
import Pokemon
import Pokedex

import json


f = open('FormattedData.json',)
data = json.load(f)
f.close()

pokedex = Pokedex.Pokedex()


typeAndCountLst = []
typeCount = 0 # Total number of types
debugCount = 0 # TODO - only used for debugging
for pkmn in data: # Loop through each generated pokemon
    print (debugCount)
    debugCount += 1
    print (pkmn['name'])
    if pkmn['name'] == "Sirfetch’d": # FIXME - handle this in a cleaner way
        pkmn['name'] = "Sirfetchd"
        print (pkmn['name'])
    elif pkmn['name'] == "Farfetch’d": # FIXME - handle this in a cleaner way
        pkmn['name'] = "Farfetchd"
        print (pkmn['name'])


    if pkmn['name'] == "Urshifu":
        # TODO - verify this is being calculated correct
        pkmnTypes = ["Water", "Fighting", "Dark"]
    elif pkmn['name'] == "Zarude":
        # TODO - verify this is being calculated correct
        pkmnTypes = ["Grass", "Dark"]
    else:
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
    print (typeAndCountLst[0]['type'])


for i in range (len(typeAndCountLst)):
    # FIXME - verify this hits the last case
    s = typeAndCountLst[i]['type'] + " was generated " + str(typeAndCountLst[i]['count']) + " out of " + str(typeCount)
    print (s)
