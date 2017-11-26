import json, pprint

file = "output.json"
data = json.load(open(file, 'r'))
for key in data["Diseases"][0]:
    