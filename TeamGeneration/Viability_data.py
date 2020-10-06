# Using viability rankings as data - https://www.smogon.com/forums/threads/ss-ou-viability-ranking-thread.3666340/

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
formattedDataLst = []
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
        formattedDataLst.append ({
            "Name": line.strip(),
            "Types": types,
            "Rank": rank
        })

pkmnLst = []
for data in formattedDataLst:
    pkmnLst.append(Pokemon.getPokemonInStr(data['Name'], pokedex)[0])
