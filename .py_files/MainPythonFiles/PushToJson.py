import json

def PushBColor(color):
    
    TargetFile = open("json_files\Settings.json","r")
    json_object = json.load(TargetFile)
    json_object["BColor"] = color
    
    TargetFile.close()
    
    TargetFile = open("json_files\Settings.json",'w')
    json.dump(json_object,TargetFile)
    TargetFile.close()
    return color

def PushTimeFormat(TimeFormat):
    TargetFile = open("json_files\Settings.json","r")
    json_object = json.load(TargetFile)
    json_object["Time"] = TimeFormat
    TargetFile.close()
    
    TargetFile = open("json_files\Settings.json",'w')
    json.dump(json_object,TargetFile)
    TargetFile.close()

    

def PushDateFormat(DateFormat):
    TargetFile = open("json_files\Settings.json","r")
    json_object = json.load(TargetFile)
    json_object["Date"] = DateFormat
    TargetFile.close()
    
    TargetFile = open("json_files\Settings.json",'w')
    json.dump(json_object,TargetFile)
    TargetFile.close()