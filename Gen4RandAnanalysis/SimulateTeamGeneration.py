# This will simulate using the Pokemon Showdown gen 4 random team generator to generate `NUM_TEAMS_GENERATED`*6 Pokemon that can be used to analyze the random set generation.
# The following Pokemon Showdown directory will need to be clone: https://github.com/smogon/pokemon-showdown and this script placed and run within the root of that repo.
# Depending on the format you want, you may have to change the console.log() statements in https://github.com/smogon/pokemon-showdown/blob/master/pokemon-showdown or other locations


import subprocess

# Configuration Variables
NUM_TEAMS_GENERATED = 10
OUTPUT_FILENAME = "gen4randoms-parsed-to-be-closer-to-json.output"
TEMP_FILENAME = "temp.output"

# Simulate data
with open(TEMP_FILENAME, 'a') as out:
    for i in range(NUM_TEAMS_GENERATED):
        subprocess.call(["./pokemon-showdown", "generate-team", "gen4randombattle"], stdout=out)


# Parse out data that isn't needed to make data resemble json more closely
# TODO - this is terribly inefficient
with open(TEMP_FILENAME, 'r') as rfp:
  with open(OUTPUT_FILENAME, 'w') as wfp:
    for line in rfp:
      if ',' in line or '{' in line:
        wfp.write(line)
