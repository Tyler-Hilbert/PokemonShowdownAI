# This will generate generation 4 random teams the specified number of times and then append it to the specified file.
# The following Pokemon Showdown directory will need to be clone: https://github.com/smogon/pokemon-showdown and this script placed and run within the root of that repo

# FIXME - verify that `$./pokemon-showdown generate-team gen4randoms` generates the same distribution as the server

import subprocess

NUM_TEAMS_GENERATED = 10
OUTPUT_FILENAME = "gen4randoms.output"

with open(OUTPUT_FILENAME, 'a') as out:
    for i in range(NUM_TEAMS_GENERATED):
        subprocess.call(["./pokemon-showdown", "generate-team", "gen4randombattle"], stdout=out)
