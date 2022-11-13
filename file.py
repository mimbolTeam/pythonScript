"""
Provides import json module
"""
import json

with open('times.json', 'r', encoding='utf8') as temp_file:
    contents = temp_file.read()
JSON_STRING = ''.join(contents.readlines())
print(JSON_STRING)
data = json.loads(JSON_STRING)
print(data)
