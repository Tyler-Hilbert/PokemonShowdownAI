# Create tree of game states

import sys
sys.path.insert(1, '../')
import Pokedex
import Pokemon

DEBUG = False

def search(allyPkmn, foePkmn, allyPkmnLst, foePkmnLst, depth):

    if DEBUG:
        print ("\n\n", "*-*"*depth)
        print ("allyPkmn:", allyPkmn.toString(), "\nfoePkmn:", foePkmn.toString(), "\nallyPkmnLst:\n", Pokemon.teamToString(allyPkmnLst), "foePkmnLst:\n", Pokemon.teamToString(foePkmnLst))
    else:
        print ("-"*depth, "allyPkmn:", allyPkmn.toString().split('\t')[0], "foePkmn:", foePkmn.toString().split('\t')[0])

    score = allyPkmn.battle(foePkmn)
    if score > 0:
        foePkmnLst.remove(foePkmn)
        for pkmn in foePkmnLst:
            search(allyPkmn, pkmn, allyPkmnLst.copy(), foePkmnLst.copy(), depth+1)
    elif score < 0:
        allyPkmnLst.remove(allyPkmn)
        for pkmn in allyPkmnLst:
            search(pkmn, foePkmn, allyPkmnLst.copy(), foePkmnLst.copy(), depth+1)
    else:
        if DEBUG:
            print ("Unknown winner")

# Load Pokemon teams
pokedex = Pokedex.Pokedex()
allyPkmnLst = Pokemon.getPokemonInStr("Jolteon Espeon Flareon", pokedex)
foePkmnLst = Pokemon.getPokemonInStr("Vaporeon Umbreon Leafeon", pokedex)
# TODO -- loop through other ally pokemon
for pkmn in foePkmnLst:
    search (allyPkmnLst[0], pkmn, allyPkmnLst, foePkmnLst, 1)
