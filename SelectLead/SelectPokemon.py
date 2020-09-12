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
highestNet = -99 # Arbitrary low number that will always have matchups with higher net
highestNetName = "PLACEHOLDER"
for allyPkmn in allyPkmnLst:
    print (allyPkmn.toString())
    score = 0
    for foePkmn in foePkmnLst:
        score += allyPkmn.battle(foePkmn)
    print (score)
