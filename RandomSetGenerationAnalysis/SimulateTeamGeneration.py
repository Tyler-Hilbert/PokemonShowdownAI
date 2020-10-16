# This will simulate using the Pokemon Showdown gen 8 random team generator to generate `NUM_TEAMS_GENERATED`*6 Pokemon that can be used to analyze the random set generation.
# The following Pokemon Showdown directory will need to be clone: https://github.com/smogon/pokemon-showdown and this script placed and run within the root of that repo.
# Depending on the format you want, you may have to change the console.log() statements in https://github.com/smogon/pokemon-showdown/blob/master/pokemon-showdown or other locations

import subprocess
import os

# Configuration Variables
NUM_TEAMS_GENERATED = int(252/6) * 375 # Should generate each pokemon 252 times since there are 375 pokemon and 6 pokemon per team
OUTPUT_FILENAME = "raw.output"

# Backup previous 1 simulation in OUTPUT_FILENAME
os.rename(OUTPUT_FILENAME, (OUTPUT_FILENAME + ".old"))

# Simulate data
with open(OUTPUT_FILENAME, 'a') as out:
    for i in range(NUM_TEAMS_GENERATED):
        subprocess.call(["./pokemon-showdown", "generate-team", "gen8randombattle"], stdout=out)
