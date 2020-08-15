import Pokemon

# Loads and stores Pokedex data
# TODO - convert the data into a friendlier format to read in Python and remove this string parsing
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
    def findPokemonUsingName(self, pkmnName): # TODO- Pokemon Loading
        pkmnName = pkmnName.strip().lower()
        for p in self.pokedex:
            if p['name'].strip().lower() == pkmnName:
                return Pokemon.Pokemon(p['name'], p['types'])
