import json

with open('primer-dataset.json') as f:
    data = [json.loads(line) for line in open('primer-dataset.json', 'r')]
    print(data)
