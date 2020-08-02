### PrintWeakness.py
## Prints all other pokemon ally pokemon is weak against

# Loads and stores Pokedex data
class Pokedex:
    # Loads self.Pokdex
    def __init__(self):
        # Open data file
        fp = open('pokedex.data', 'r')
        data = fp.readlines()
        fp.close()

        self.pokedex = []

        # Parse out names and types
        name = "n/a"
        types = "n/a"
        for d in data:
            if ":" in d and "{" in d and "}" not in d:
                name = d.split(":")[0].strip()

            if "types" in d:
                types = "".join(d.split(",")[0:-1])
                pokemon = {'name': name, 'types': types}
                self.pokedex.append(pokemon)


    # Find Pokemon based on name
    def findPokemonUsingName(self, pkmnName): # FIXME - Pokemon Loading
        pkmnName = pkmnName.strip().lower()
        for p in self.pokedex:
            if p['name'].strip().lower() == pkmnName:
                return p
##### class Pokedex #####

# Saves information about a Pokemon
class Pokemon:
    def __init__(self, name, types, weakness):
        self.name = name
        self.weakness = weakness
        typesLst = types.split('"')
        self.types = []
        while len(typesLst) > 1:
            self.types.append(typesLst[1])
            typesLst = typesLst[2:]

    def toString(self):
        s = self.name
        for type in self.types:
            s += "\t" + type
        return s

    def outcomeDefending(self, attackingPokemon):
        s = self.name + " is defending against " + attackingPokemon.name + "\n"
        for w in self.weakness:
            for ap in attackingPokemon.types:
                if w == ap:
                    s += self.name + " weak against " + ap
        print (s)

##### class Pokedex #####



## MAIN
allyPkmnName = "Pidgey"
allyWeakAgainst = ["Electric", "Ice", "Rock"]

pokedex = Pokedex()
allyPkmn = Pokemon(pokedex.findPokemonUsingName(allyPkmnName)['name'], pokedex.findPokemonUsingName(allyPkmnName)['types'], allyWeakAgainst) # TODO- Pokemon Loading

foeLst = ["Pikachu", "Umbreon", "Carbink"]
for foe in foeLst:
    print ("Ally: ")
    print (allyPkmn.toString())
    print ("Foe: ")
    print(foe)

    foePkmn = Pokemon(pokedex.findPokemonUsingName(foe)['name'], pokedex.findPokemonUsingName(foe)['types'], ["FIXME", "WEAKTYPES"]) # TODO - Pokemon Loading


    print("\n(allyPkmn.outcomeDefending(foePkmn))")
    print(allyPkmn.outcomeDefending(foePkmn))
