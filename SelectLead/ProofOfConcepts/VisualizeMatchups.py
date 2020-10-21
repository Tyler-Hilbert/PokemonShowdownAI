# Creates visual for how each pokemon matches up against each other pokemon in the opponent team
# Takes an HTML input file

# FIXME - Loading icons hasn't been checked for every pokemon and some may crash the program if the name isn't the same as the filename

import sys
sys.path.insert(1, '../')
import Pokedex
import Pokemon

import re
from bs4 import BeautifulSoup
import glob, os
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


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


# Create plot
size = 6
fig, ax = plt.subplots()
ax.set_xlim(0, size)
ax.set_ylim(0, size)
# Add pokemon icons
teamNum = 0
for team in [allyPkmnLst, foePkmnLst]:
    for i in range(len(team)):
        name = team[i].name.lower().replace("alola", "-alola")
        name = name.replace("fan", "-fan")
        name = name.replace("frost", "-frost")
        name = name.replace("heat", "-heat")
        name = name.replace("mow", "-mow")
        name = name.replace("wash", "-wash")

        filename = "../icons/" + name + ".png"
        img = mpimg.imread(filename)
        imagebox = OffsetImage(img)
        ab = AnnotationBbox(imagebox, (teamNum, i))
        ax.add_artist(ab)
    teamNum += size

# Plot matchups
pokedex = Pokedex.Pokedex()
for aI in range(len(allyPkmnLst)):
    for pI in range(len(foePkmnLst)):
        battle = allyPkmnLst[aI].battle(foePkmnLst[pI])
        print (battle)
        if battle < 0:
            plt.plot ([0, size], [aI,pI], color='red', linewidth=-1*battle)
        elif battle > 0:
            plt.plot([0, size], [aI,pI], color='green', linewidth=battle)

# Show
plt.axis('off')
plt.show()
