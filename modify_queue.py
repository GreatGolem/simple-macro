import json

with open('dragon.json','rb') as f:
    data = json.load(f)

data['victory'].append([])

with open('dragon.json','w') as f:
    json.dump(data,f)
