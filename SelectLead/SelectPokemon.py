# Selects best pokemon to switch into given 2 strings that have all pokemon names
# The selection is done by finding the ally pokemon with the fewest number of weaknesses against the foe's pokemon types

import re
import Pokedex
import Pokemon

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


########## MAIN  ####################################################################
#########################################################################################

pokedex = Pokedex.Pokedex()

foePkmnLst = Pokemon.getPokemonInStr(foePkmnNameLst, pokedex)
allyPkmnLst = Pokemon.getPokemonInStr(allyPkmnNameLst, pokedex)

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
