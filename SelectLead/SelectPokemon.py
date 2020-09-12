# Selects best pokemon to switch into after downloading the .html page to this directory
# Important: Only have 1 HTML file in this directory at a time

import re
import Pokedex
import Pokemon
from bs4 import BeautifulSoup
import glob, os
import sys

# Verify there is a file to read
if len(glob.glob("*.html")) != 1:
    sys.exit("Error: Exactly 1 html file should be in this directory")

# Read file
filename = glob.glob("*html")[0]
f = open(filename, encoding="utf8")
soup = BeautifulSoup(f, 'html.parser')
f.close()

# Parse out pokemon
teams = []
for tag in soup.findAll("em"):
    text = str(tag)
    if " / " in text:
        print (text)
        teams.append(text)
allyPkmnNameLst = teams[0]
foePkmnNameLst = teams[1]
# TODO - check entire pokemon for each pokemon property parsing
pokedex = Pokedex.Pokedex()
foePkmnLst = Pokemon.getPokemonInStr(foePkmnNameLst, pokedex)
allyPkmnLst = Pokemon.getPokemonInStr(allyPkmnNameLst, pokedex)

# Calculate
foeTotalScore = 0
allyTotalScore = 0

highestScore = -99 # Arbitrary low number that will always have matchups with lower score
highestScoreName = "PLACEHOLDER"
for allyPkmn in allyPkmnLst:
    print (allyPkmn.toString())
    score = 0
    for foePkmn in foePkmnLst:
        score += allyPkmn.battle(foePkmn)
    # TODO - handle score ties
    if score > highestScore:
        highestScoreName = allyPkmn.toString()
        highestScore = score
    allyTotalScore += score
    print (score)
s = "Your best move is " + highestScoreName + "\n"
s += "Ally Total Score " + str(allyTotalScore) + "\n"
print (s)

highestScore = -99 # Arbitrary low number that will always have matchups with lower score
highestScoreName = "PLACEHOLDER"
for foePkmn in foePkmnLst:
    print (foePkmn.toString())
    score = 0
    for allyPkmn in allyPkmnLst:
        score += foePkmn.battle(allyPkmn)
    # TODO - handle score ties
    if score > highestScore:
        highestScoreName = foePkmn.toString()
        highestScore = score
    foeTotalScore += score
    print (score)
s = "Foe best move is " + highestScoreName + "\n"
s += "Foe Total Score " + str(foeTotalScore) + "\n"
print (s)

if (allyTotalScore > foeTotalScore):
    print ("Ally predicted to win")
elif (allyTotalScore < foeTotalScore):
    print ("Foe team predicted to win")
else:
    print ("equal chances of winning")
