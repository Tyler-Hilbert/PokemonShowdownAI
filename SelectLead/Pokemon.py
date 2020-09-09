import Pokedex
import TypeMatchups_data

import re

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

     # TODO - passing in key a better way
    def addWeakness(self, defending):
        self.weaknesses.append(TypeMatchups_data.defendingMatchups[defending])
        # FIXME - adding weakness (ultimately this should be calculated on the spot rather than a variable)

     # TODO - passing in key a better way
    def addStrength(self, defending):
        self.strengths.append(TypeMatchups_data.defendingMatchups[defending])
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
                    if allyPokemonKey[key] == TypeMatchups_data.SUPER_EFFECTIVE and key == attackType:
                        return True
        return False

    # Returns True if the attacking pokemon is not very effective
    def isStrong(self, attackingPokemon):
        for attackType in attackingPokemon.types:
            for allyPokemonKey in self.strengths:
                for key in allyPokemonKey:
                    if ( (allyPokemonKey[key] == TypeMatchups_data.NOT_VERY_EFFECTIVE) or (allyPokemonKey[key] == TypeMatchups_data.IMMUNE) ) and key == attackType:
                        return True
        return False

# TODO - is there a better place to include this?
# Returns list of all pokemon found in the input string
def getPokemonInStr(str, pokedex):
    # Parse out pokemon names
    strWords = re.split('[^a-zA-Z\-]', str)
    # Lower Case and remove -
    strWordsLwr = []
    for w in strWords:
        strWordsLwr.append(w.lower().replace('-', ''))
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
