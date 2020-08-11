# Selects best pokemon to switch into given 2 strings that have all pokemon names
# The selection is done by finding the ally pokemon with the fewest number of weaknesses against the foe's pokemon types

import re
from TypeMatchups_data import *

##########  INPUT VARIABLES  ############################################################
#########################################################################################
# Enter a string that contains the name of all your pokemon (can contain non-pokemon characters/words and isn't formatted)
allyPkmnNameLst = "jolteon bisharp espeon leafeon vaporeon flareon"
# Enter a string that contains the name of all your opponent pokemon (can contain non-pokemon characters/words and isn't formatted)
foePkmnNameLst = "Incineroar / Skarmory / Kyurem / Mamoswine / Tyranitar / Celebi"
# FIXME - "Silvally-*" could be parsed wrong. Check for other odd cases on the name
# FIXME - galar pokemon don't work either
# FIXME - do alola work? Maybe I just have to filter out '-'
#########################################################################################
#########################################################################################


##########  CLASSES  ####################################################################
#########################################################################################
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

        # FIXME - cases where pokemon has one weakness to a pokemon and a strength to the same pokemon
        # TODO - set weaknesses and strengths in same loop
        # Set weaknesses
        self.weaknesses = [] # TODO - calculate this on the spot
        for type in self.types:
            # FIXME - Add way for 4 times weakness
            typeStr = type.lower() + "Defending"
            self.addWeakness(typeStr)

        # Set strengths
        self.strengths = [] # TODO - calculate this on the spot
        for type in self.types:
            # FIXME - Add way for immunity
            typeStr = type.lower() + "Defending"
            self.addStrength(typeStr)

     # FIXME - passing in key a better way
    def addWeakness(self, defending):
        self.weaknesses.append(defendingMatchups[defending])
        # FIXME - adding weakness (ultimately this should be calculated on the spot rather than a variable)

     # FIXME - passing in key a better way
    def addStrength(self, defending):
        self.strengths.append(defendingMatchups[defending])
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

    # Returns True if the attacking pokemon is not very effective
    def isStrong(self, attackingPokemon):
        for attackType in attackingPokemon.types:
            for allyPokemonKey in self.strengths:
                for key in allyPokemonKey:
                    if ( (allyPokemonKey[key] == NOT_VERY_EFFECTIVE) or (allyPokemonKey[key] == IMMUNE) ) and key == attackType:
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
                return Pokemon(p['name'], p['types'])
##### class Pokedex #####



#########################################################################################
#########################################################################################

##########  Methods  ####################################################################
#########################################################################################
# Returns list of all pokemon found in the input string
def getPokemonInStr(str, pokedex):
    # Parse out pokemon names
    strWords = re.split('[^a-zA-Z]', str)
    # Lower Case Words
    strWordsLwr = []
    for w  in strWords:
        strWordsLwr.append(w.lower())
    # Remove Duplicates
    potentialNameStr = []
    [potentialNameStr.append(x) for x in strWordsLwr if x not in potentialNameStr]
    # Search remaining words for Pokemon names
    pkmnLst = []
    for n in potentialNameStr:
        # TODO - fix this so it only looks up once
        if pokedex.findPokemonUsingName(n) != None:
            pkmnLst.append(pokedex.findPokemonUsingName(n))
    return pkmnLst

#########################################################################################
#########################################################################################


########## MAIN  ####################################################################
#########################################################################################

pokedex = Pokedex()

foePkmnLst = getPokemonInStr(foePkmnNameLst, pokedex)
allyPkmnLst = getPokemonInStr(allyPkmnNameLst, pokedex)

highestNet = -99 # Arbitrary low number that will always have matchups with higher net
highestNetName = "PLACEHOLDER"

for allyPkmn in allyPkmnLst:
    print (allyPkmn.toString())
    # Calculate number of weaknesses/strengths
    # Weaknesses
    numWeaknesses = 0
    for foePkmn in foePkmnLst:
        if allyPkmn.isWeak(foePkmn):
            s = allyPkmn.name + " has weakness to " + foePkmn.name
            print (s)
            numWeaknesses += 1
    s = allyPkmn.name + " has " + str(numWeaknesses) + " weaknesses\n"
    print (s)

    # Strengths
    numStrengths = 0
    for foePkmn in foePkmnLst:
        if allyPkmn.isStrong(foePkmn):
            s = allyPkmn.name + " has strength to " + foePkmn.name
            print (s)
            numStrengths += 1
    s = allyPkmn.name + " has " + str(numStrengths) + " strengths\n\n"
    print (s)

    # Calculate difference (net) in strengths vs weaknesses
    net = numStrengths - numWeaknesses
    if net > highestNet:
        highestNet = net
        highestNetName = allyPkmn.name


# Print pokemon with best net
s = highestNetName + " has net of " + str(highestNet)
print (s)
