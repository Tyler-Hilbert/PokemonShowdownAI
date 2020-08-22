# Lists all Pokemon names

import json

f = open('FormattedData.json',)
data = json.load(f)
f.close()


names = []
for pkmn in data:
    if pkmn['name'] not in names:
        names.append(pkmn['name'])

for name in names:
    print (name)

s = str(len(names)) + " unique pokemon names found out of " + str(len(data)) + " generated pokemon"
print (s)
