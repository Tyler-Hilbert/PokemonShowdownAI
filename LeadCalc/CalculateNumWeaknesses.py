# Calculates the number of weakness a pokemon has

import re
import json

# Loads and stores Pokedex data
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
            NORMAL = "Normal"
            SUPER_EFFECTIVE = "Super effective"
            NOT_VERY_EFFECTIVE = "NOT_VERY_EFFECTIVE"
            IMMUNE = "IMMUNE"

            bugDefending = {
                "Bug": NORMAL,
                "Dark": NORMAL,
                "Dragon": NORMAL,
                "Electric": NORMAL,
                "Fairy": NORMAL,
                "Fighting": NOT_VERY_EFFECTIVE,
                "Fire": SUPER_EFFECTIVE,
                "Flying": SUPER_EFFECTIVE,
                "Ghost": NORMAL,
                "Grass": NOT_VERY_EFFECTIVE,
                "Ground": NOT_VERY_EFFECTIVE,
                "Ice": NOT_VERY_EFFECTIVE,
                "Normal": NORMAL,
                "Poison": NORMAL,
                "Psychic": NORMAL,
                "Rock": SUPER_EFFECTIVE,
                "Steel": NORMAL,
                "Water": NORMAL
            }

            darkDefending = {
            	"Bug": SUPER_EFFECTIVE,
            	"Dark": NOT_VERY_EFFECTIVE,
            	"Dragon": NORMAL,
            	"Electric": NORMAL,
            	"Fairy": SUPER_EFFECTIVE,
            	"Fighting": SUPER_EFFECTIVE,
            	"Fire": NORMAL,
            	"Flying": NORMAL,
            	"Ghost": NOT_VERY_EFFECTIVE,
            	"Grass": NORMAL,
            	"Ground": NORMAL,
            	"Ice": NORMAL,
            	"Normal": NORMAL,
            	"Poison": NORMAL,
            	"Psychic": IMMUNE,
            	"Rock": NORMAL,
            	"Steel": NORMAL,
            	"Water": NORMAL
            }

            dragonDefending = {
            	"Bug": NORMAL,
            	"Dark": NORMAL,
            	"Dragon": SUPER_EFFECTIVE,
            	"Electric": NOT_VERY_EFFECTIVE,
            	"Fairy": SUPER_EFFECTIVE,
            	"Fighting": NORMAL,
            	"Fire": NOT_VERY_EFFECTIVE,
            	"Flying": NORMAL,
            	"Ghost": NORMAL,
            	"Grass": NOT_VERY_EFFECTIVE,
            	"Ground": NORMAL,
            	"Ice": SUPER_EFFECTIVE,
            	"Normal": NORMAL,
            	"Poison": NORMAL,
            	"Psychic": NORMAL,
            	"Rock": NORMAL,
            	"Steel": NORMAL,
            	"Water": NOT_VERY_EFFECTIVE
            }

            electricDefending = {
            	"Par": IMMUNE,
            	"Bug": NORMAL,
            	"Dark": NORMAL,
            	"Dragon": NORMAL,
            	"Electric": NOT_VERY_EFFECTIVE,
            	"Fairy": NORMAL,
            	"Fighting": NORMAL,
            	"Fire": NORMAL,
            	"Flying": NOT_VERY_EFFECTIVE,
            	"Ghost": NORMAL,
            	"Grass": NORMAL,
            	"Ground": SUPER_EFFECTIVE,
            	"Ice": NORMAL,
            	"Normal": NORMAL,
            	"Poison": NORMAL,
            	"Psychic": NORMAL,
            	"Rock": NORMAL,
            	"Steel": NOT_VERY_EFFECTIVE,
            	"Water": NORMAL
            }

            fairyDefending: {
            	"Bug": NOT_VERY_EFFECTIVE,
            	"Dark": NOT_VERY_EFFECTIVE,
            	"Dragon": IMMUNE,
            	"Electric": NORMAL,
            	"Fairy": NORMAL,
            	"Fighting": NOT_VERY_EFFECTIVE,
            	"Fire": NORMAL,
            	"Flying": NORMAL,
            	"Ghost": NORMAL,
            	"Grass": NORMAL,
            	"Ground": NORMAL,
            	"Ice": NORMAL,
            	"Normal": NORMAL,
            	"Poison": SUPER_EFFECTIVE,
            	"Psychic": NORMAL,
            	"Rock": NORMAL,
            	"Steel": SUPER_EFFECTIVE,
            	"Water": NORMAL
            }

            fightingDefending = {
            	"Bug": NOT_VERY_EFFECTIVE,
            	"Dark": NOT_VERY_EFFECTIVE,
            	"Dragon": NORMAL,
            	"Electric": NORMAL,
            	"Fairy": SUPER_EFFECTIVE,
            	"Fighting": NORMAL,
            	"Fire": NORMAL,
            	"Flying": SUPER_EFFECTIVE,
            	"Ghost": NORMAL,
            	"Grass": NORMAL,
            	"Ground": NORMAL,
            	"Ice": NORMAL,
            	"Normal": NORMAL,
            	"Poison": NORMAL,
            	"Psychic": SUPER_EFFECTIVE,
            	"Rock": NOT_VERY_EFFECTIVE,
            	"Steel": NORMAL,
            	"Water": NORMAL
            }


            fireDefending = {
            	"Brn": IMMUNE,
            	"Bug": NOT_VERY_EFFECTIVE,
            	"Dark": NORMAL,
            	"Dragon": NORMAL,
            	"Electric": NORMAL,
            	"Fairy": NOT_VERY_EFFECTIVE,
            	"Fighting": NORMAL,
            	"Fire": NOT_VERY_EFFECTIVE,
            	"Flying": NORMAL,
            	"Ghost": NORMAL,
            	"Grass": NOT_VERY_EFFECTIVE,
            	"Ground": SUPER_EFFECTIVE,
            	"Ice": NOT_VERY_EFFECTIVE,
            	"Normal": NORMAL,
            	"Poison": NORMAL,
            	"Psychic": NORMAL,
            	"Rock": SUPER_EFFECTIVE,
            	"Steel": NOT_VERY_EFFECTIVE,
            	"Water": SUPER_EFFECTIVE
            }

            flyingDefending = {
            	"Bug": NOT_VERY_EFFECTIVE,
            	"Dark": NORMAL,
            	"Dragon": NORMAL,
            	"Electric": SUPER_EFFECTIVE,
            	"Fairy": NORMAL,
            	"Fighting": NOT_VERY_EFFECTIVE,
            	"Fire": NORMAL,
            	"Flying": NORMAL,
            	"Ghost": NORMAL,
            	"Grass": NOT_VERY_EFFECTIVE,
            	"Ground": IMMUNE,
            	"Ice": SUPER_EFFECTIVE,
            	"Normal": NORMAL,
            	"Poison": NORMAL,
            	"Psychic": NORMAL,
            	"Rock": SUPER_EFFECTIVE,
            	"Steel": NORMAL,
            	"Water": NORMAL
            }

            ghostDefending = {
            	"Trapped": IMMUNE,
            	"Bug": NOT_VERY_EFFECTIVE,
            	"Dark": SUPER_EFFECTIVE,
            	"Dragon": NORMAL,
            	"Electric": NORMAL,
            	"Fairy": NORMAL,
            	"Fighting": IMMUNE,
            	"Fire": NORMAL,
            	"Flying": NORMAL,
            	"Ghost": SUPER_EFFECTIVE,
            	"Grass": NORMAL,
            	"Ground": NORMAL,
            	"Ice": NORMAL,
            	"Normal": IMMUNE,
            	"Poison": NOT_VERY_EFFECTIVE,
            	"Psychic": NORMAL,
            	"Rock": NORMAL,
            	"Steel": NORMAL,
            	"Water": NORMAL
            }

            grassDefending = {
            	"Powder": IMMUNE,
            	"Bug": SUPER_EFFECTIVE,
            	"Dark": NORMAL,
            	"Dragon": NORMAL,
            	"Electric": NOT_VERY_EFFECTIVE,
            	"Fairy": NORMAL,
            	"Fighting": NORMAL,
            	"Fire": SUPER_EFFECTIVE,
            	"Flying": SUPER_EFFECTIVE,
            	"Ghost": NORMAL,
            	"Grass": NOT_VERY_EFFECTIVE,
            	"Ground": NOT_VERY_EFFECTIVE,
            	"Ice": SUPER_EFFECTIVE,
            	"Normal": NORMAL,
            	"Poison": SUPER_EFFECTIVE,
            	"Psychic": NORMAL,
            	"Rock": NORMAL,
            	"Steel": NORMAL,
            	"Water": NOT_VERY_EFFECTIVE
            }

            groundDefending = {
            	"Sandstorm": IMMUNE,
            	"Bug": NORMAL,
            	"Dark": NORMAL,
            	"Dragon": NORMAL,
            	"Electric": IMMUNE,
            	"Fairy": NORMAL,
            	"Fighting": NORMAL,
            	"Fire": NORMAL,
            	"Flying": NORMAL,
            	"Ghost": NORMAL,
            	"Grass": SUPER_EFFECTIVE,
            	"Ground": NORMAL,
            	"Ice": SUPER_EFFECTIVE,
            	"Normal": NORMAL,
            	"Poison": NOT_VERY_EFFECTIVE,
            	"Psychic": NORMAL,
            	"Rock": NOT_VERY_EFFECTIVE,
            	"Steel": NORMAL,
            	"Water": SUPER_EFFECTIVE
            }

            iceDefending = {
            	"Hail": IMMUNE,
            	"Frz": IMMUNE,
            	"Bug": NORMAL,
            	"Dark": NORMAL,
            	"Dragon": NORMAL,
            	"Electric": NORMAL,
            	"Fairy": NORMAL,
            	"Fighting": SUPER_EFFECTIVE,
            	"Fire": SUPER_EFFECTIVE,
            	"Flying": NORMAL,
            	"Ghost": NORMAL,
            	"Grass": NORMAL,
            	"Ground": NORMAL,
            	"Ice": NOT_VERY_EFFECTIVE,
            	"Normal": NORMAL,
            	"Poison": NORMAL,
            	"Psychic": NORMAL,
            	"Rock": SUPER_EFFECTIVE,
            	"Steel": SUPER_EFFECTIVE,
            	"Water": NORMAL
            }

            normalDefending = {
            	"Bug": NORMAL,
            	"Dark": NORMAL,
            	"Dragon": NORMAL,
            	"Electric": NORMAL,
            	"Fairy": NORMAL,
            	"Fighting": SUPER_EFFECTIVE,
            	"Fire": NORMAL,
            	"Flying": NORMAL,
            	"Ghost": IMMUNE,
            	"Grass": NORMAL,
            	"Ground": NORMAL,
            	"Ice": NORMAL,
            	"Normal": NORMAL,
            	"Poison": NORMAL,
            	"Psychic": NORMAL,
            	"Rock": NORMAL,
            	"Steel": NORMAL,
            	"Water": NORMAL
            }

            poisonDefending = {
            	"Psn": IMMUNE,
            	"Tox": IMMUNE,
            	"Bug": NOT_VERY_EFFECTIVE,
            	"Dark": NORMAL,
            	"Dragon": NORMAL,
            	"Electric": NORMAL,
            	"Fairy": NOT_VERY_EFFECTIVE,
            	"Fighting": NOT_VERY_EFFECTIVE,
            	"Fire": NORMAL,
            	"Flying": NORMAL,
            	"Ghost": NORMAL,
            	"Grass": NOT_VERY_EFFECTIVE,
            	"Ground": SUPER_EFFECTIVE,
            	"Ice": NORMAL,
            	"Normal": NORMAL,
            	"Poison": NOT_VERY_EFFECTIVE,
            	"Psychic": SUPER_EFFECTIVE,
            	"Rock": NORMAL,
            	"Steel": NORMAL,
            	"Water": NORMAL
            }

            psychicDefending = {
            	"Bug": SUPER_EFFECTIVE,
            	"Dark": SUPER_EFFECTIVE,
            	"Dragon": NORMAL,
            	"Electric": NORMAL,
            	"Fairy": NORMAL,
            	"Fighting": NOT_VERY_EFFECTIVE,
            	"Fire": NORMAL,
            	"Flying": NORMAL,
            	"Ghost": SUPER_EFFECTIVE,
            	"Grass": NORMAL,
            	"Ground": NORMAL,
            	"Ice": NORMAL,
            	"Normal": NORMAL,
            	"Poison": NORMAL,
            	"Psychic": NOT_VERY_EFFECTIVE,
            	"Rock": NORMAL,
            	"Steel": NORMAL,
            	"Water": NORMAL
            }

            rockDefending = {
            	"Sandstorm": IMMUNE,
            	"Bug": NORMAL,
            	"Dark": NORMAL,
            	"Dragon": NORMAL,
            	"Electric": NORMAL,
            	"Fairy": NORMAL,
            	"Fighting": SUPER_EFFECTIVE,
            	"Fire": NOT_VERY_EFFECTIVE,
            	"Flying": NOT_VERY_EFFECTIVE,
            	"Ghost": NORMAL,
            	"Grass": SUPER_EFFECTIVE,
            	"Ground": SUPER_EFFECTIVE,
            	"Ice": NORMAL,
            	"Normal": NOT_VERY_EFFECTIVE,
            	"Poison": NOT_VERY_EFFECTIVE,
            	"Psychic": NORMAL,
            	"Rock": NORMAL,
            	"Steel": SUPER_EFFECTIVE,
            	"Water": SUPER_EFFECTIVE
            }

            steelDefending = {
            	"Psn": IMMUNE,
            	"Tox": IMMUNE,
            	"Sandstorm": IMMUNE,
            	"Bug": NOT_VERY_EFFECTIVE,
            	"Dark": NORMAL,
            	"Dragon": NOT_VERY_EFFECTIVE,
            	"Electric": NORMAL,
            	"Fairy": NOT_VERY_EFFECTIVE,
            	"Fighting": SUPER_EFFECTIVE,
            	"Fire": SUPER_EFFECTIVE,
            	"Flying": NOT_VERY_EFFECTIVE,
            	"Ghost": NORMAL,
            	"Grass": NOT_VERY_EFFECTIVE,
            	"Ground": SUPER_EFFECTIVE,
            	"Ice": NOT_VERY_EFFECTIVE,
            	"Normal": NOT_VERY_EFFECTIVE,
            	"Poison": IMMUNE,
            	"Psychic": NOT_VERY_EFFECTIVE,
            	"Rock": NOT_VERY_EFFECTIVE,
            	"Steel": NOT_VERY_EFFECTIVE,
            	"Water": NORMAL
            }

            waterDefending = {
            	"Bug": NORMAL,
            	"Dark": NORMAL,
            	"Dragon": NORMAL,
            	"Electric": SUPER_EFFECTIVE,
            	"Fairy": NORMAL,
            	"Fighting": NORMAL,
            	"Fire": NOT_VERY_EFFECTIVE,
            	"Flying": NORMAL,
            	"Ghost": NORMAL,
            	"Grass": SUPER_EFFECTIVE,
            	"Ground": NORMAL,
            	"Ice": NOT_VERY_EFFECTIVE,
            	"Normal": NORMAL,
            	"Poison": NORMAL,
            	"Psychic": NORMAL,
            	"Rock": NORMAL,
            	"Steel": NOT_VERY_EFFECTIVE,
            	"Water": NOT_VERY_EFFECTIVE
            }

            # FIXME - load is defending data for all pokemon




            if  type == "Bug":
                self.addWeaknesses(bugDefending)
            elif type == "Dark":
                self.addWeaknesses(darkDefending)
            elif type == "Dragon":
                 self.addWeaknesses(dragonDefending)
            elif type == "Electric":
                self.addWeaknesses(electricDefending)
            elif type == "Fairy":
                self.addWeaknesses(fairyDefending)
            elif type == "Fighting":
                self.addWeaknesses(fightingDefending)
            elif type == "Fire":
                self.addWeaknesses(fireDefending)
            elif type == "Flying":
                self.addWeaknesses(flyingDefending)
            elif type == "Ghost":
                self.addWeaknesses(ghostDefending)
            elif type == "Grass":
                self.addWeaknesses(grassDefending)
            elif type == "Ground":
                self.addWeaknesses(groundDefending)
            elif type == "Ice":
                self.addWeaknesses(iceDefending)
            elif type == "Normal":
                self.addWeaknesses(normalDefending)
            elif type == "Poison":
                self.addWeaknesses(poisonDefending)
            elif type == "Psychic":
                self.addWeaknesses(psychicDefending)
            elif type == "Rock":
                self.addWeaknesses(rockDefending)
            elif type == "Steel":
                self.addWeaknesses (steelDefending)
            elif type == "Water":
                self.addWeaknesses(waterDefending)

    def addWeaknesses(self, defending):
        # FIXME - don't want these hardcoded in 2 places
        NORMAL = "Normal"
        SUPER_EFFECTIVE = "Super effective"
        NOT_VERY_EFFECTIVE = "NOT_VERY_EFFECTIVE"
        IMMUNE = "IMMUNE"
        for key in defending:
            if defending[key] == SUPER_EFFECTIVE:
                self.weaknesses.append(key)

    def toString(self):
        # TODO - add more data to print
        s = self.name
        for type in self.types:
            s += "\t" + type
        return s

    def isWeak(self, attackingPokemon):
        for w in self.weaknesses:
            for ap in attackingPokemon.types:
                if w == ap:
                    return True
        return False

##### class Pokedex #####


## MAIN
pokedex = Pokedex()

allyPkmnNameLst = ["jolteon", "umbreon", "espeon", "leafeon", "vaporeon", "flareon"]

# Opponent pokemon string
gameStr = "Chandelure / Talonflame / Incineroar / Darmanitan / Silvally-* / Charizard" # FIXME - Silvally-*
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
        # find weaknesses
        # print (allyPkmn.weaknesses)
        for t in foePkmn.types:
            if t in allyPkmn.weaknesses:
                s = allyPkmn.name + " has weakness to " + foePkmn.name + " (" + t + ")"
                print (s)
                numWeaknesses += 1


    # Print
    s = allyPkmn.name + " has " + str(numWeaknesses) + " weaknesses" + "\n"
    print (s)
