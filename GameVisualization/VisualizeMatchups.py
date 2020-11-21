# Creates visual for how each pokemon matches up against each other pokemon in the opponent team
# Takes an HTML input file saved to this directory

import sys
sys.path.insert(1, '../SelectLead')
import Pokedex
import Pokemon

import re
from bs4 import BeautifulSoup
import glob, os
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import shutil


# Verify there is a file to read
if len(glob.glob("*.html")) != 1:
    sys.exit("Error: Exactly 1 html file should be in this directory")

# Read file
filename = glob.glob("*html")[0]
f = open(filename, encoding="utf8")
soup = BeautifulSoup(f, 'html.parser')
f.close()

# Move file to another directory. This makes it faster to download file next game
ARCHIVE_DIRECTORY = "OldGameBeginningDownloads"
if not os.path.isdir(ARCHIVE_DIRECTORY):
    os.mkdir(ARCHIVE_DIRECTORY+"/")
shutil.move(filename, ARCHIVE_DIRECTORY+"/"+filename)

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
        name = name.replace("galar", "-galar")
        name = name.replace("resolute", "-resolute")
        name = name.replace("fan", "-fan")
        name = name.replace("frost", "-frost")
        name = name.replace("heat", "-heat")
        name = name.replace("mow", "-mow")
        name = name.replace("wash", "-wash")
        name = name.replace("null", "-null")

        filename = "icons/" + name + ".png"
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
