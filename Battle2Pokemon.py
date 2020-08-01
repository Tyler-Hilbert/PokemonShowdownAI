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

    def toString(self):
        s = self.name
        for type in self.types:
            s += "\t" + type
        return s

    def outcomeDefending(self, attackingPokemon):
        s = self.name + " is defending against " + attackingPokemon.name
        if attackingPokemon.name.lower() == "pidgey" and self.name.lower() == "pikachu":
            return "2 - win - pidgey is not very effective"
        elif attackingPokemon.name.lower() == "pikachu" and self.name.lower() == "pidgey":
            return "1 - lose - pikachu is super effective"

    def outcomeAttacking(self, defendingPokemon):
        s = self.name + " is attacking against " + defendingPokemon.name
        if self.name.lower() == "pidgey" and defendingPokemon.name.lower() == "pikachu":
            return "2 - win - pidgey is not very effective"
        elif self.name.lower() == "pikachu" and defendingPokemon.name.lower() == "pidgey":
            return "1 - lose - pikachu is super effective"
##### class Pokedex #####


##### MAIN
set = 0

if set == 0:
    allyPkmnName = "Pidgey"
    foePkmnName = "Pikachu"
elif set == 1:
    allyPkmnName = "Umbreon"
    foePkmnName = "Blaziken"
elif set == 2:
    allyPkmnName = "Silvallysteel"
    foePkmnName = "Carbink"
elif set == 3:
    allyPkmnName = "Drampa"
    foePkmnName = "Dhelmise"
elif set == 4:
    allyPkmnName = "infernape"
    foePkmnName = "empoleon"

pokedex = Pokedex()

allyPkmn = Pokemon(pokedex.findPokemonUsingName(allyPkmnName)['name'], pokedex.findPokemonUsingName(allyPkmnName)['types']) # FIXME - Pokemon Loading
foePkmn = Pokemon(pokedex.findPokemonUsingName(foePkmnName)['name'], pokedex.findPokemonUsingName(foePkmnName)['types']) # FIXME - Pokemon Loading

print ("you are: ")
print (allyPkmn.toString())
print ("")
print ("against: ")
print(foePkmn.toString())
print ("")

print("\n(allyPkmn.outcomeAttacking(foePkmn))")
print(allyPkmn.outcomeAttacking(foePkmn))
print("\n(allyPkmn.outcomeDefending(foePkmn))")
print(allyPkmn.outcomeDefending(foePkmn))
print("\n(foePkmn.outcomeAttacking(allyPkmn))")
print(foePkmn.outcomeAttacking(allyPkmn))
print("\n(foePkmn.outcomeDefending(allyPkmn))")
print(foePkmn.outcomeDefending(allyPkmn))
