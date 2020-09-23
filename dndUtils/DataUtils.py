from dndUtils.DnDClasses import Setting
import json

def saveJSON(settings):
    with open('data.txt', 'w') as outfile:
        json.dump(settings, outfile)

def loadJSON():
    with open('data.txt') as json_file:
        data = json.load(json_file)
    return data
