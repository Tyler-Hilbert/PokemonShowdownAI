# This will simulate using the Pokemon Showdown gen 4 random team generator to generate `NUM_TEAMS_GENERATED`*6 Pokemon that can be used to analyze the random set generation.
# The following Pokemon Showdown directory will need to be clone: https://github.com/smogon/pokemon-showdown and this script placed and run within the root of that repo.
# Depending on the format you want, you may have to change the console.log() statements in https://github.com/smogon/pokemon-showdown/blob/master/pokemon-showdown or other locations

# FIXME - There is a bug where the last generated Pokemon doesn't add a ',' after the '}'. This is an issue because it causes problems in post processing when turning the output data into a Python data structure

# TODO - should this file not only simulate but also format the data into a usable output? It would make it easier to use from a user standpoint since only one script would need to be run. It would make development slower though since it would need to resimulate all data just to make changes to the parsing algorithm.

import subprocess

# Configuration Variables
NUM_TEAMS_GENERATED = int(102/6) * 297 # Should generate each pokemon 102 times since there are 297 pokemon and 6 pokemon per team
OUTPUT_FILENAME = "raw.output"

# FIXME -- delete original output file

# Simulate data
with open(OUTPUT_FILENAME, 'a') as out:
    for i in range(NUM_TEAMS_GENERATED):
        subprocess.call(["./pokemon-showdown", "generate-team", "gen4randombattle"], stdout=out)
