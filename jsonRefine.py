import json

with open('kedarnathDatasetTwitter') as f:
  data = json.load(f)

for state in data['states']:
  del state['area_codes']

with open('new_Dataset.json', 'w') as f:
  json.dump(data, f, indent=2)