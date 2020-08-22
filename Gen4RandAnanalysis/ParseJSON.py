# This file is only used to verify the output is valid JSON

import json

f = open('FormattedData.json',)
data = json.load(f)
f.close()
print (data)
