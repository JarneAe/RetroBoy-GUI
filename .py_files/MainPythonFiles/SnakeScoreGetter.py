import json


TargetFile = open("json_files\SnakeScore.json","r")
SnakeScore = json.load(TargetFile)
TargetFile.close()
