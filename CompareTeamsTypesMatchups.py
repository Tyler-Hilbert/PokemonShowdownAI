# Calculate number of weaknesses for each of your pokemon against list of enemies

import re
from TypeMatchups_data import *

##########  INPUT VARIABLES  ############################################################
#########################################################################################
# Enter your team (must be quoted and only pokemon within quotes)
allyPkmnNameLst = ["jolteon", "umbreon", "espeon", "leafeon", "vaporeon", "flareon"]
# Enter a string that contains the name of all your opponent pokemon (can contain non-pokemon characters/words)
gameStr = "Dugtrio / Scyther / Slowbro-Galar / Tsareena / Incineroar / Inteleon"
# FIXME - "Silvally-*" could be parsed wrong. Check for other odd cases on the name
#########################################################################################
#########################################################################################


##########  CLASSES  ####################################################################
#########################################################################################ßß
# Saves information about a Pokemon
class Pokemon:
    def __init__(self, name, types):
        # Set name and type
        self.name = name
        typesLst = types.split('"')
        self.types = []
        while len(typesLst) > 1:
            self.types.append(typesLst[1])
            typesLst = typesLst[2:]

        # Set weaknesses
        self.weaknesses = [] # TODO - calculate this on the spot
        for type in self.types:
            # FIXME - Add way for 4 times weakness
            typeStr = type.lower() + "Defending"
            self.addWeaknesses(typeStr)

     # FIXME - passing in key a better way
    def addWeaknesses(self, defending):
        self.weaknesses.append(defendingMatchups[defending])
        # FIXME - adding weakness (ultimately this should be calculated on the spot rather than a variable)

    def toString(self):
        # TODO - add more data to print
        s = self.name
        for type in self.types:
            s += "\t" + type
        return s

    # Returns True if the pokemon is weak against attackingPokemon
    def isWeak(self, attackingPokemon):
        for attackType in attackingPokemon.types:
            for allyPokemonKey in self.weaknesses:
                for key in allyPokemonKey:
                    if allyPokemonKey[key] == SUPER_EFFECTIVE and key == attackType:
                        return True
        return False
##### class Pokedex #####


# Loads and stores Pokedex data
# TODO - convert the data into a friendlier format to read in Python and remove this string parsing
class Pokedex:
    # Loads self.Pokdex
    def __init__(self):
        # Open data file
        fp = open('pokedex.data', 'r')
        data = fp.readlines()
        fp.close()

        self.pokedex = []

        # Parse out names and types
        name = "n/a"
        types = "n/a"
        for d in data:
            if ":" in d and "{" in d and "}" not in d:
                name = d.split(":")[0].strip()

            if "types" in d:
                types = "".join(d.split(",")[0:-1])
                pokemon = {'name': name, 'types': types}
                self.pokedex.append(pokemon)


    # Find Pokemon based on name
    def findPokemonUsingName(self, pkmnName): # TODO- Pokemon Loading
        pkmnName = pkmnName.strip().lower()
        for p in self.pokedex:
            if p['name'].strip().lower() == pkmnName:
                return p
##### class Pokedex #####



#########################################################################################
#########################################################################################


########## MAIN  ####################################################################
#########################################################################################
pokedex = Pokedex()

# Parse out pokemon names
strWords = re.split('[^a-zA-Z]', gameStr)
strWordsLwr = []
for w  in strWords:
    strWordsLwr.append(w.lower())

potentialNameStr = []
[potentialNameStr.append(x) for x in strWordsLwr if x not in potentialNameStr]

# Find foeLst
foeLst = []
for w in potentialNameStr:
    if pokedex.findPokemonUsingName(w) != None:
        foeLst.append(w)

s = "Foe List: " + str(foeLst) + "\n"
print (s)

for allyPkmnName in allyPkmnNameLst:
    allyPkmn = Pokemon(pokedex.findPokemonUsingName(allyPkmnName)['name'], pokedex.findPokemonUsingName(allyPkmnName)['types']) # TODO- Pokemon Loading

    # Calculate number of weaknesses
    numWeaknesses = 0
    for foe in foeLst:
        foePkmn = Pokemon(pokedex.findPokemonUsingName(foe)['name'], pokedex.findPokemonUsingName(foe)['types']) # TODO - Pokemon Loading
        if allyPkmn.isWeak(foePkmn):
            s = allyPkmn.name + " has weakness to " + foePkmn.name
            print (s)
            numWeaknesses += 1


    # Print
    s = allyPkmn.name + " has " + str(numWeaknesses) + " weaknesses" + "\n"
    print (s)
