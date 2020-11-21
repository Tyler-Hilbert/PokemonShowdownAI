# Create tree of game states
# Use `$dot -Tpng GameState.gv -o GameState.png` to create graphic

import sys
sys.path.insert(1, '../SelectLead')
import Pokedex
import Pokemon

OUTPUT_FILENAME = "GameState.gv"

def search(allyPkmn, foePkmn, allyPkmnLst, foePkmnLst, depth, parentStr):
    # Write graph node
    nodeStr = "ally_" + allyPkmn.name.upper() + "_"
    for pkmn in allyPkmnLst:
        nodeStr += pkmn.name + "_"
    nodeStr += "__foe_" + foePkmn.name.upper() + "_"
    for pkmn in foePkmnLst:
        nodeStr += pkmn.name + "_"
    s = parentStr + " -> " + nodeStr + "\n"
    f = open(OUTPUT_FILENAME, "a")
    f.write(s)
    f.close()

    '''
    if VERBOSE:
        print ("\n\n", "*-*"*depth)
        print ("allyPkmn:", allyPkmn.toString(), "\nfoePkmn:", foePkmn.toString(), "\nallyPkmnLst:\n", Pokemon.teamToString(allyPkmnLst), "foePkmnLst:\n", Pokemon.teamToString(foePkmnLst))
    else:
        print ("-"*depth, "allyPkmn:", allyPkmn.toString().split('\t')[0], "foePkmn:", foePkmn.toString().split('\t')[0])
    '''

    # Continue search
    score = allyPkmn.battle(foePkmn)
    if score > 0:
        foePkmnLst.remove(foePkmn)
        for pkmn in foePkmnLst:
            search(allyPkmn, pkmn, allyPkmnLst.copy(), foePkmnLst.copy(), depth+1, nodeStr)
    elif score < 0:
        allyPkmnLst.remove(allyPkmn)
        for pkmn in allyPkmnLst:
            search(pkmn, foePkmn, allyPkmnLst.copy(), foePkmnLst.copy(), depth+1, nodeStr)

# Create File
f = open(OUTPUT_FILENAME, "w")
f.write("digraph G {\n")
f.close()

# Load Pokemon teams
pokedex = Pokedex.Pokedex()
allyPkmnLst = Pokemon.getPokemonInStr("Jolteon Espeon Flareon", pokedex)
foePkmnLst = Pokemon.getPokemonInStr("Vaporeon Umbreon Leafeon", pokedex)
# TODO -- loop through other ally pokemon
for pkmn in foePkmnLst:
    search (allyPkmnLst[0], pkmn, allyPkmnLst.copy(), foePkmnLst.copy(), 1, allyPkmnLst[0].name)

# Finish File
f = open(OUTPUT_FILENAME, "a")
f.write("}")
f.close()
