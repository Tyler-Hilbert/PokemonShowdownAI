# Calculates the number of weakness a pokemon has

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
    def __init__(self, name, types):
        self.name = name
        typesLst = types.split('"')
        self.types = []
        while len(typesLst) > 1:
            self.types.append(typesLst[1])
            typesLst = typesLst[2:]

        self.weaknesses = []
        # FIXME - doesn't account for 2 type changes
        if "Electric" in types:
            electric = ["Ground"]
            self.weaknesses += electric

        if "Dark" in types:
            dark = ["Bug", "Fairy", "Fighting"]
            self.weaknesses += dark

        if "Psychic" in types:
            psychic = ["Bug", "Dark", "Ghost"]
            self.weaknesses += psychic

        if "Grass" in types:
            grass = ["Bug", "Fire", "Ice", "Poison"]
            self.weaknesses += grass

        if "Water" in types:
            water = ["Electric", "Grass"]
            self.weaknesses += water

        if "Fire" in types:
            fire = ["Ground", "Rock", "Water"]
            self.weaknesses += fire

    def toString(self):
        s = self.name
        for type in self.types:
            s += "\t" + type
        return s

    def isWeak(self, attackingPokemon):
        for w in self.weaknesses:
            for ap in attackingPokemon.types:
                if w == ap:
                    return True
        return False

##### class Pokedex #####




## MAIN
pokedex = Pokedex()

allyPkmnNameLst = ["jolteon", "umbreon", "espeon", "leafeon", "vaporeon", "flareon"]
for allyPkmnName in allyPkmnNameLst:
    allyPkmn = Pokemon(pokedex.findPokemonUsingName(allyPkmnName)['name'], pokedex.findPokemonUsingName(allyPkmnName)['types']) # TODO- Pokemon Loading

    # Append all Pokemon names to list
    foeLst = []
    for p in pokedex.pokedex:
        foeLst.append(p['name'])

    numWeaknesses = 0
    for foe in foeLst:
        foePkmn = Pokemon(pokedex.findPokemonUsingName(foe)['name'], pokedex.findPokemonUsingName(foe)['types']) # TODO - Pokemon Loading
        if allyPkmn.isWeak(foePkmn):
            #print (foePkmn.toString())
            numWeaknesses += 1


    # Print
    s = allyPkmn.name + " has " + str(numWeaknesses) + " weaknesses"
    print (s)
