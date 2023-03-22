import pygame as py
import json
import random as ra
import pygame.image
from pygame.locals import *
import os

# This code declares the global variables to be used in this game and long with preloading assets to be displayed in the
# scene.
def initialise():

    # The overlay is a global array containing the timer variables used on each overlay, this is combined with the
    # overlay_image-array that contains the image data for the overlays to provide visual feedback on what actions have
    # occurred (i.e. watering or saving).
    global overlay
    overlay = [0, 0]
    global overlay_image
    overlay_image = []
    load_save()
    for i in range(len(overlay)):
        image = py.image.load("Textures/Overlay"+str(i)+".png")
        overlay_image.append(pygame.transform.scale(image, (settings["Window_Size"], settings["Window_Size"])))
    clock = py.time.Clock()
    clock.tick(30)

    # Opens the tile info json file, loading it to global variable tile_ifo as a dict before iterating through
    # dictionary and dumping corresponding tile images into a 2d array for later use (i,e, rendering to screen).
    with open("tile_info.json") as data:
        global tile_info
        tile_info = json.load(data)
    global tiles
    crop_tiles = []
    for i in range(tile_info["Crop_Num"]):
        tile = []
        for j in range((tile_info["Crops"])[i]["max_type"]):
            # Concatenates a string to use as a file directory.
            image = py.image.load("Textures/Crop_Tiles" + str(i+1) + "." + str(j+1) + ".png")
            tile.append(pygame.transform.scale(image, (settings["Window_Size"], settings["Window_Size"])))
        crop_tiles.append(tile)


# Dumps the dictionary's used for player data into the save file directory provided by the settings json file.
def save_game():
    overlay[0] = 100
    with open(settings["Save_File_Name"], "w") as data:
        data.write(json.dumps(save_data, indent=2))


# Opens the settings and save files, saving them as public dictionary's.
def load_save():
    overlay[0] = 100
    global settings
    global save_data
    with open('settings.json') as sett:
        settings = json.load(sett)
    with open(settings["Save_File_Name"]) as data:
        save_data = json.load(data)


def update_crops(tick_update):
    return


def call_animation():
    start = True
    frames = 0
    while start:
        if frames <= 81:
            frames =+ 1
        for i in range(frames // 10):
            return
        return



def render():
    screen.fill((1, 14, 19))
    for i in range(len(overlay)):
        if overlay[i] >= 0:
            screen.blit(overlay_image[i], (0, 0))
            overlay[i] -= 1
    py.display.update()


class CropTiles:
    def __init__(self, goal_x, goal_y, y, ):
        self.goal_x = goal_x
        self.goal_y = goal_y
        


# The main function where the main game loop is run
def main():
    start = True
    global tick
    tick = 0
    tick_update = 1800 // settings["Tick_Rate"]
    while True:
        if tick >= tick_update:
            tick = 0
            update_crops(tick_update)
        else:
            tick =+ 1

        render()
        for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.enter:
                    return
            if event.type == py.QUIT:
                save_game()
                py.display.quit()
                py.quit()


# Checks if file is run as main file before initialising application and starting the main function.
if __name__ == "__main__":
    py.init()
    initialise()
    py.display.set_caption(settings["Farm_Name"])
    screen = py.display.set_mode((settings["Window_Size"], settings["Window_Size"]))
    main()

