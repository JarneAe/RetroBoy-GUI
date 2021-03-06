import json
from datetime import date, datetime


#Reads json file and loads it to something readable
with open("json_files\Settings.json") as json_file:
    data = json.load(json_file)
    

#checks what color is selected for background
    if data["BColor"] == 'Dark':
        SelectedColor = "background-color:rgb(71, 82, 99);"

    elif(data["BColor"] == 'Light'):
        SelectedColor = "background-color:rgb(215, 227, 245);"

    elif(data["BColor"] == 'Pink'):
        SelectedColor = "background-color:rgb(220,20,60);"
    
    elif(isinstance(data["BColor"],list)):
        print(data["BColor"])
        colors = data["BColor"]
        SelectedColor = "background-color:rgb({0},{1},{2})".format(colors[0],colors[1],colors[2])

    elif(isinstance(data["BColor"],str)):
        if data["BColor"] != 'Custom':
            SelectedColor = "background-color:rgb({});".format(data["BColor"])
        else:
            SelectedColor = "background-color:rgb(71, 82, 99);"  
    else:
        SelectedColor = "background-color:rgb(71, 82, 99);"


    if (data["ButtonColor"] == 'Default'):
        SelectedButtonColor = "background-color:rgb(255, 255, 255);""border-radius: 7px;"
        print("default color found")

    elif(isinstance(data["ButtonColor"],list)):
        print(data["ButtonColor"])
        colors = data["ButtonColor"]
        SelectedButtonColor = f"background-color:rgb({colors[0]},{colors[1]},{colors[2]});""border-radius: 7px;"
        print("list found")

    elif(isinstance(data["ButtonColor"],str)):
        if data["ButtonColor"] != 'Custom':
            color = data["ButtonColor"]
            SelectedButtonColor = f"background-color:rgb({color});""border-radius: 7px;"
        else:
            SelectedButtonColor = "background-color:rgb(71, 82, 99);""border-radius: 7px;"  
    else:
        SelectedButtonColor = "background-color:rgb(71, 82, 99);""border-radius: 7px;"




#checks the date in the json file 
    now = datetime.now()

    if data["Date"] == 'Day/Month/Year':
        DateFormat = now.strftime("%d-%m-%y")
    else:
        DateFormat = now.strftime("%m-%d-%y")
    
    if data["Time"] == "AM/PM":
        TimeFormat = "%I:%M %p"
    else:
        TimeFormat = "%H:%M:%S"
    
