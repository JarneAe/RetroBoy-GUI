import json

TargetFile = open("json_files\SnakeScore.json","r")
json_object = json.load(TargetFile)
TargetFile.close()
print(json_object)