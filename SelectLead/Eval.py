# Quick test to figure out best way to program battling multiple turns and predicting outcomes

import Pokedex
import Pokemon

# Load Pokemon teams
pokedex = Pokedex.Pokedex()
allyPkmnLst = Pokemon.getPokemonInStr("Charizard", pokedex)
foePkmnLst = Pokemon.getPokemonInStr("Blastoise vileplume hitmonlee", pokedex)

# Loop through and remove pokemon while they lose.
# Assuming list is always a LIFO of order pokemon are sent out.
while len(allyPkmnLst) != 0 and len(foePkmnLst) != 0:
    # Battle
    battleScore = allyPkmnLst[-1].battle(foePkmnLst[-1])
    s = "Ally " + allyPkmnLst[-1].toString() + " vs\nFoe " + foePkmnLst[-1].toString()
    print (s)
    print (battleScore)
    # Remove loser
    if battleScore < 0:
        allyPkmnLst.pop()
    elif battleScore == 0:
        print ("Tie")
        break
    else:
        foePkmnLst.pop()

s = "Ally Pokemon left: " + str(len(allyPkmnLst))
print (s)
s = "Foe Pokemon left: " + str(len(foePkmnLst))
print (s)
