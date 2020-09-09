# Selects best pokemon to switch into after downloading the .htm page to this directory

import re
import Pokedex
import Pokemon
from bs4 import BeautifulSoup
import glob, os
import sys

# Verify there is a file to read
if len(glob.glob("*.htm")) != 1:
    sys.exit("Error: Exactly 1 htm file should be in this directory")

# Read file
filename = glob.glob("*htm")[0]
f = open(filename, encoding="utf8")
soup = BeautifulSoup(f, 'html.parser')
f.close()

# Parse out pokemon
teams = []
for tag in soup.findAll("em"):
    text = str(tag)
    if " / " in text:
        teams.append(text)
allyPkmnNameLst = teams[0]
foePkmnNameLst = teams[1]
# FIXME - do alola work? Maybe I just have to filter out '-'
pokedex = Pokedex.Pokedex()
foePkmnLst = Pokemon.getPokemonInStr(foePkmnNameLst, pokedex)
allyPkmnLst = Pokemon.getPokemonInStr(allyPkmnNameLst, pokedex)

# Calculate
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
