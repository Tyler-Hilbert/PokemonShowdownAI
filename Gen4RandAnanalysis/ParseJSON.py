import json

f = open('FormattedData.json',)
data = json.load(f)
f.close()
print (data)
