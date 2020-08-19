To run the program:  
1) Clone the Pokemon Showdown repo https://github.com/smogon/pokemon-showdown  
2) Copy `pokemon-showdown` and `SimulateTeamGeneration.py` into the root of the pokemon-showdown repo  
3) Run `python3 SimulateTeamGeneration` within the pokemon-showdown root directory  
4) Copy the simulated data file `gen4randoms-formatted-data.output` from the root directory of pokemon-showdown to the root directory of this repo  
5) run `python3 PostProcessor.py` to convert the outputted simulated data into a format understood by Python  


The file Notes.txt documents the decisions I made while creating this software. It is in chronological order and I do not remove any notes, so what is listed at the top may be irrelevant to the current state of the software. All the same, reading through it should explain why I made some of the choices I did.
