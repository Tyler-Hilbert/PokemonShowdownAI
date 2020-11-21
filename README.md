# PokemonShowdownAI
This is 3 projects I wrote while making a bot that is capable of playing the online player vs player game Pokemon Showdown.  
Note all scripts are tested on only Python3.8.  
## GameVisualization  
Scripts used to create visuals of a game. Currently contains two visualization scripts. One graphs the matchups of Pokemon between 2 teams. The other creates a game state tree plot like you would use in a minimax algorithm.  
## RandomSetGenerationAnalysis
This is an attempt to analyze the different sets that can be randomly generated. This will be useful information in situations where the opponent has unknown pokemon,moves,abilities, etc.
## SelectLead
This is a bot that is capable of making the first move in a game. This works for game modes that have all pokemon revealed at the beginning of the game. It currently tries to optimize the ratio of strengths to weaknesses for the first turn. It will be converted to look multiple turns ahead using a minimax algorithm.
