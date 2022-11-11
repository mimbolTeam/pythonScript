import json
f = open('times.json','r')
# работа с файлом
json_string = ''.join(f.readlines())
print(json_string)
data = json.loads(json_string)
print(data)
f.close()