# Quick test to see if I can visualize the matchups of a battle

import sys
sys.path.insert(1, '../')
import Pokedex
import Pokemon


from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

######## INPUT VARIABLES ############
allyTeam = ["charizard", "butterfree", "celebi", "azelf", "beedrill", "chatot"]
oppTeam = ["baltoy", "aipom", "basculin", "breloom", "charizard", "bisharp"]
size = len(allyTeam)-1 # Best to not change
#####################################

# Create plot
fig, ax = plt.subplots()
ax.set_xlim(0, size)
ax.set_ylim(0, size)
# Add pokemon icons
teamNum = 0
for team in [allyTeam, oppTeam]:
    for i in range(len(team)):
        filename = "../icons/" + team[i] + ".png"
        img = mpimg.imread(filename)
        imagebox = OffsetImage(img)
        ab = AnnotationBbox(imagebox, (teamNum, i))
        ax.add_artist(ab)
    teamNum += size

# Plot matchups
pokedex = Pokedex.Pokedex()
for aI in range(len(allyTeam)):
    for oI in range(len(oppTeam)):
        battle = pokedex.findPokemonUsingName(allyTeam[aI]).battle(pokedex.findPokemonUsingName(oppTeam[oI]))
        print (battle)
        if battle < 0:
            plt.plot ([0, size], [aI,oI], color='red', linewidth=-1*battle)
        elif battle > 0:
            plt.plot([0, size], [aI,oI], color='green', linewidth=battle)

# Show
plt.axis('off')
plt.show()
