import json
import pygame as py


class User:
    # Creates an object to use as a player data template.
    def __init__(self, settings, save_data, scaler, tickrate):
        self.settings = settings
        self.save_data = save_data
        self.scaler = scaler
        self.tickrate = tickrate


# Creates an instance of user data.
def create_user_data():
    settings = load_settings()
    save = load_save(settings)
    self = User(
        settings,
        save,
        settings["Window_Size"]/100,
        settings["Tick_Rate"]
    )
    return self


# Dumps the dictionary's used for player data into the save file directory provided by the settings json file.
def dump_save(save_data, settings):
    try:
        with open(settings["Save_File_Name"], "w") as data:
            data.write(json.dumps(save_data, indent=2))
    except:
        print("Unable to save user data")


# Opens the settings and settings files, returning as a dictionary.
def load_settings():
    with open('settings.json') as settings:
        try:
            return json.load(settings)
        except:
            print("Unable to locate settings file")


# Loads the save file, returning as a dictionary.
def load_save(settings_file):
    try:
        with open(settings_file["Save_File_Name"]) as data:
            try:
                return json.load(data)
            except:
                print("Incorrect save name")
    except:
        print("Unable to locate settings file")


class ScreenOverlay:
    def __init__(self, opacity, image):
        self.opacity = opacity
        self.image = image


def initial_screen_overlay(user):
    overlay_image = []
    for i in range(1):
        image = py.image.load("Textures/Overlay/" + str(i) + ".png")
        overlay_image.append(py.transform.scale(image, (user.settings["Window_Size"], user.settings["Window_Size"])))

    return ScreenOverlay(
        [0, 0],
        overlay_image
    )


class TextOverlay:
    def __int__(self, opacity, contains):
        self.opacity = opacity
        self.contains = contains


class CropData:
    def __init__(self, textures, info):
        self.textures = textures
        self.info = info


# returns a list of raw image data for textures.
def initial_crop_data(user):

    try:
        with open("tile_info.json") as data:
            info = json.load(data)
    except:
        print("Unable to locate tile info file")

    crop_tiles = [[]]
    image = py.image.load("Textures/Crop Tiles/0.0.png")
    crop_tiles[0].append(py.transform.scale(image, (user.settings["Window_Size"], user.settings["Window_Size"])))
    for i in range(info["Crop_Num"]):
        tile = []
        for j in range((info["Crops"])[i]["max_type"]):
            # Concatenates a string to use as a file directory.
            image = py.image.load("Textures/Crop Tiles/" + str(i+1) + "." + str(j) + ".png")
            tile.append(py.transform.scale(image, (user.settings["Window_Size"], user.settings["Window_Size"])))
        crop_tiles.append(tile)
    return CropData(
        crop_tiles,
        info
    )



