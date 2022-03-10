import json


TargetFile = open("TestingFiles\JSONTesting\Settings.json","r")
json_object = json.load(TargetFile)
json_object["BColor"] = "Green"
TargetFile.close()
print(json_object)

TargetFile = open("TestingFiles\JSONTesting\Settings.json",'w')
json.dump(json_object,TargetFile)
TargetFile.close()
