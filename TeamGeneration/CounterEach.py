# Generates at least one pokemon that can counter each OU ranked pokemon
# Uses the highest ranked pokemon from the viability rankings that can counter each pokemon

import Viability_data # This where where the viability ranking data is stored
import sys
sys.path.insert(1, '../SelectLead')
import Pokedex
import Pokemon

import copy

# Returns a counter pokemon that from valid list that is not in usedLst
def findCounter(oppPkmn, validLst, usedLst):
    for testPkmn in validLst:
        if testPkmn.battle(oppPkmn) > 0 and testPkmn not in usedLst:
            return testPkmn

# Returns list of pokemon that still need to be countered
def removeCounters(pkmn, toCounter):
    counterLst = []
    for cPkmn in toCounter:
        if pkmn.battle(cPkmn) <= 0:
            counterLst.append(cPkmn)
    return counterLst

def teamToString(pkmnLst):
    s = ""
    for pkmn in pkmnLst:
        s += pkmn.toString() + "\n"
    return s

pkmnLst = Viability_data.pkmnLst
toCounter = copy.copy(pkmnLst) # List of pokemon that need a counter generated
allyTeam = []

while len(toCounter) > 0: # Loops until every pokemon is countered
    countered = findCounter(toCounter[0], pkmnLst, allyTeam)
    allyTeam.append(countered)
    toCounter = removeCounters(countered, toCounter)
    print ("Ally team", teamToString(allyTeam))
    print ("To counter", teamToString(toCounter))
    print ("*")

print ("****")
print (teamToString(allyTeam))
