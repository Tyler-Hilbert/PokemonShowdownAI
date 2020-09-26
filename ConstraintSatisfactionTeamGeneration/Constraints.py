# Using viability rankings as data - https://www.smogon.com/forums/threads/ss-ou-viability-ranking-thread.3666340/
# This is a part hardcoded part automated way of generating a team.
# The algorithm used goes down the first 6 viability rankings and adds a pokemon to counter each.

import sys
sys.path.insert(1, '../SelectLead')
import Pokedex
import Pokemon

from io import StringIO


dataRaw = """
S Rank:

S Rank

 Clefable
 Toxapex

A Rank:

A+ Rank

 Corviknight
 Dragapult
 Excadrill
 Urshifu
 Volcarona
 Zeraora

A Rank

 Amoonguss
 Blissey
 Ferrothorn
 Hippowdon
 Hydreigon
 Kyurem
 Magnezone
 Rillaboom

A- Rank

 Aegislash
 Alakazam
 Kommo-o
 Mandibuzz
 Rotom-Heat
 Skarmory
 Tyranitar

B Rank:

B+ Rank

 Crawdaunt
 Ditto
 Gastrodon
 Gengar
 Reuniclus
 Rhyperior
 Scizor
 Slowbro
 Tangrowth
 Togekiss

B Rank

 Azumarill
 Hatterene
 Hawlucha
 Kingdra
 Mantine
 Necrozma
 Pelipper
 Quagsire
 Torkoal
 Toxtricity
 Urshifu-R
 Venusaur

B- Rank

 Bisharp
 Charizard
 Conkeldurr
 Diggersby
 Grimmsnarl
 Heracross
 Jirachi
 Keldeo
 Mew
 Primarina
 Terrakion
 Weezing-Galar

C Rank:

C+ Rank

 Barraskewda
 Chandelure
 Krookodile
 Mamoswine
 Marowak-Alola
 Obstagoon
 Rotom-Wash
 Salazzle
 Talonflame
 Weavile
 Xatu

C Rank

 Araquanid
 Chansey
 Cloyster
 Dracozolt
 Gyarados
 Ninetales-Alola
 Seismitoad
 Shuckle
 Slowbro-Galar

C- Rank

 Comfey
 Incineroar
 Jellicent
 Mienshao
 Mimikyu
 Slowking
 Snorlax
"""

data = StringIO(dataRaw)

# Format data
pokedex = Pokedex.Pokedex()
rank = ""
pkmnLst = []
for line in data:
    if "Rank" in line: # Save rank
        rank = line.strip()
    elif len(line.strip()) != 0:
        # Touch up line
        line = line.replace("-", "")
        line = line.replace("UrshifuR", "Urshifu")
        #print (line)
        # Update data list
        types = pokedex.findPokemonUsingName(line.strip()).types
        pkmnLst.append ({
            "Name": line.strip(),
            "Types": types,
            "Rank": rank
        })

# Count amount of each type
count = {
    "Normal": 0,
    "Fairy": 0,
    "Poison": 0,
    "Water": 0,
    "Flying": 0,
    "Steel": 0,
    "Dragon": 0,
    "Ghost": 0,
    "Ground": 0,
    "Fighting": 0,
    "Dark": 0,
    "Bug": 0,
    "Fire": 0,
    "Electric": 0,
    "Grass": 0,
    "Ice": 0,
    "Psychic": 0,
    "Rock": 0
}

for pkmn in pkmnLst:
    #print (pkmn)
    for type in pkmn['Types']:
        count[type] += 1

'''
for type in types:
    s = '{"type": "' + type + '", "count": 0},'
    print (s)
'''

print (count)



# Create team
allyTeam = []

# Find pokemon that is strong against clefable
# Clefable (steel)
for pkmn in pkmnLst:
    if "Steel" in pkmn['Types'] and pkmn not in allyTeam:
        allyTeam.append (pkmn)
        break
# Toxapex (electric)
for pkmn in pkmnLst:
    if "Electric" in pkmn['Types'] and pkmn not in allyTeam:
        allyTeam.append (pkmn)
        break
# Corviknight (fire)
for pkmn in pkmnLst:
    if "Fire" in pkmn['Types'] and pkmn not in allyTeam:
        allyTeam.append (pkmn)
        break
# Dragapult (fairy)
for pkmn in pkmnLst:
    if "Fairy" in pkmn['Types'] and pkmn not in allyTeam:
        allyTeam.append (pkmn)
        break
# Excadrill (water)
for pkmn in pkmnLst:
    if "Water" in pkmn['Types'] and pkmn not in allyTeam:
        allyTeam.append (pkmn)
        break
# Urshifu (fairy)
# Skipped since clefable is already added and I thought that was good enough
# Volcarona (rock)
for pkmn in pkmnLst:
    if "Rock" in pkmn['Types'] and pkmn not in allyTeam:
        allyTeam.append (pkmn)
        break
for pkmn in allyTeam:
    print (pkmn)
