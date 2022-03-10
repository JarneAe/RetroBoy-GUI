import json
from datetime import date, datetime

#Reads json file and loads it to something readable
with open("json_files\Settings.json") as json_file:
    data = json.load(json_file)
    

#checks what color is selected for background
    if data["BColor"] == 'Dark':
        print('Dark color found')
        SelectedColor = "background-color:rgb(71, 82, 99);"

    elif(data["BColor"] == 'Light'):
        SelectedColor = "background-color:rgb(215, 227, 245);"

    elif(data["BColor"] == 'Pink'):
        SelectedColor = "background-color:rgb(220,20,60);"

    else:
        SelectedColor = "background-color:rgb(71, 82, 99);"


#checks the date in the json file 
    now = datetime.now()

    if data["Date"] == 'Day/Month/Year':
        DateFormat = now.strftime("%d-%m-%y")
    else:
        DateFormat = now.strftime("%m-%d-%y")
    
