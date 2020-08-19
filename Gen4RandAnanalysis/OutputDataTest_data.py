# This is a test for converting the output data into a usable python format.
# The following steps needed to be done manually to convert the data to a python format:
# 1) output square brackets to turn the data structure into a list along with a variable needed to be declared
# 2) each set is going to be a dictionary. To do this the keys needed '' around them
# 3) the 'ev' and 'iv' keys needed their indentation fixed
# 4) def needed to be changed to dfs

generatedSets = [
  {
    'name': 'Illumise',
    'species': 'Illumise',
    'gender': 'F',
    'moves': [ 'bugbuzz', 'hiddenpowerground', 'encore', 'thunderbolt' ],
    'ability': 'Tinted Lens',
    'evs': {
        'hp': 81,
        'atk': 0,
        'dfs': 85,
        'spa': 85,
        'spd': 85,
        'spe': 85
    },
    'ivs': {
        'hp': 31,
        'atk': 3,
        'dfs': 31,
        'spa': 31,
        'spd': 31,
        'spe': 31
    },
    'item': 'Focus Sash',
    'level': 83,
  },
  {
    'name': 'Gastrodon',
    'species': 'Gastrodon-East',
    'gender': '',
    'moves': [ 'recover', 'earthpower', 'toxic', 'surf' ],
    'ability': 'Sticky Hold',
    'evs': {
        'hp': 85,
        'atk': 0,
        'dfs': 85,
        'spa': 85,
        'spd': 85,
        'spe': 85
    },
    'ivs': {
        'hp': 31,
        'atk': 0,
        'dfs': 31,
        'spa': 31,
        'spd': 31,
        'spe': 31
    },
    'item': 'Leftovers',
    'level': 83,
  },
  {
    'name': 'Wormadam',
    'species': 'Wormadam-Trash',
    'gender': 'F',
    'moves': [ 'protect', 'gyroball', 'toxic', 'stealthrock' ],
    'ability': 'Anticipation',
    'evs': {
        'hp': 85,
        'atk': 85,
        'dfs': 85,
        'spa': 85,
        'spd': 85,
        'spe': 0
    },
    'ivs': {
        'hp': 31,
        'atk': 31,
        'dfs': 31,
        'spa': 31,
        'spd': 31,
        'spe': 0
    },
    'item': 'Leftovers',
    'level': 83,
  },
]

print (generatedSets)
