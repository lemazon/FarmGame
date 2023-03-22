import json

def load_save():
    global settings
    global save_data
    with open('settings.json') as sett:
        settings = json.load(sett)
        print(settings)
    with open(settings["Save_File_Name"]) as data:
        save_data = json.load(data)

load_save()
print(save_data)