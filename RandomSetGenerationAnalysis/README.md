To run the program:  
1) Clone the Pokemon Showdown repo https://github.com/smogon/pokemon-showdown  
2) Copy `pokemon-showdown` and `SimulateTeamGeneration.py` into the root of the pokemon-showdown repo  
3) Run `python3 SimulateTeamGeneration.py` within the pokemon-showdown root directory  
4) Copy the simulated data file `raw.output` from the root directory of pokemon-showdown to the root directory of this repo  
5) Run `python3 RawtoJSON.py` to convert the outputted simulated data into a valid JSON format
6) To analyze the unique sets for each pokemon run `python3 WriteGeneratedPokemon.py`. This will output the data into the subdirectory GeneratedGen8Pokemon  


The file Notes.txt documents the decisions I made while creating this software. It is in chronological order and I do not remove any notes, so what is listed at the top may be irrelevant to the current state of the software. All the same, reading through it should explain why I made some of the choices I did.
