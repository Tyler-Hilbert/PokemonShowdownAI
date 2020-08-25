# Calculates how often each pokemon is generated

# FIXME - verify that calculated numbers are correct

# FIXME - pokemon like Deoxys have many forms but all get counted as one pokemon
# FIXME - rotom
# FIXME - alola

import json

f = open('FormattedData.json',)
data = json.load(f)
f.close()


nameAndCountLst = []
for pkmn in data: # Loop through each generated pokemon
    found = False
    for i in range (len(nameAndCountLst)): # Loop through each pokemon already counted
        # FIXME - verify this hits the last case
        if pkmn['name'] == nameAndCountLst[i]['name']:
            nameAndCountLst[i]['count'] += 1
            found = True
    if not found:
        nameAndCountLst.append({
            'name': pkmn['name'],
            'count': 1
        })


for i in range (len(nameAndCountLst)):
    # FIXME - verify this hits the last case
    s = nameAndCountLst[i]['name'] + " was generated " + str(nameAndCountLst[i]['count']) + " out of " + str(len(data))
    print (s)

print (len(nameAndCountLst))
