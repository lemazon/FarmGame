import pygame as py
import json
import tiles
import random as ra
import pygame.image
import pygame_gui as py_gui
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
        image = py.image.load("Textures/Overlay/" + str(i) + ".png")
        overlay_image.append(pygame.transform.scale(image, (settings["Window_Size"], settings["Window_Size"])))
    global clock
    clock = py.time.Clock()
    clock.tick(30)
    global scaler
    scaler = settings["Window_Size"] / 100
    global manager
    manager = py_gui.UIManager((settings["Window_Size"], settings["Window_Size"]))
    global text_input

    # Opens the tile info json file, loading it to global variable tile_ifo as a dict before iterating through
    # dictionary and dumping corresponding tile images into a 2d array for later use (i,e, rendering to screen).
    with open("tile_info.json") as data:
        global tile_info
        tile_info = json.load(data)
    global crop_tiles
    crop_tiles = [[]]
    image = py.image.load("Textures/Crop Tiles/0.0.png")
    crop_tiles[0].append(pygame.transform.scale(image, (settings["Window_Size"], settings["Window_Size"])))
    for i in range(tile_info["Crop_Num"]):
        tile = []
        for j in range((tile_info["Crops"])[i]["max_type"]):
            # Concatenates a string to use as a file directory.
            image = py.image.load("Textures/Crop Tiles/" + str(i+1) + "." + str(j) + ".png")
            tile.append(pygame.transform.scale(image, (settings["Window_Size"], settings["Window_Size"])))
        crop_tiles.append(tile)
    # Generates data for the pos of the tiles, dumping the info to an array
    global crop_data
    crop_data = tiles.initial_tile_POS(scaler)


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


class Animations:
    def call_all():
        frames = 0
        t = 0
        loop = True
        while loop:
            frames += 1
            if (frames % 4 == 0) and (frames <= 36):
                t += 1
            for i in range(t):
                crop_data[i].call(scaler)
            render()
            if frames >= 46:
                loop = False

    def push_all():
        frames = 0
        t = 0
        loop = True
        while loop:
            frames += 1
            if (frames % 4 == 0) and (frames <= 36):
                t += 1
            for i in range(t):
                crop_data[i].push(scaler)
            render()
            if frames >= 46:
                loop = False


# A render function that calls relevant actions before updating the display.
def render():
    screen.fill((1, 14, 19))
    for i in range(9):
        x = save_data["Crops"][i]["Tile_id"]
        screen.blit(
            crop_tiles[x[0]][x[1]],
            (crop_data[i].goal_x, crop_data[i].y)
        )
    for i in range(len(overlay)):
        if overlay[i] >= 0:
            screen.blit(overlay_image[i], (0, 0))
            overlay[i] -= 1
    py.display.update()


# The main function where the main game loop is run
def main():
    start = True
    global tick
    tick = 0
    tick_update = settings["Tick_Rate"]
    auto_save = settings["Auto_Save"]
    while start:
        ui_refresh_rate = clock.tick(30)/500
        if tick >= tick_update:
            tick = 0
            update_crops(tick_update)
            if auto_save:
                save_game()
        else:
            tick = + 1

        render()
        for event in py.event.get():
            if event.type == py.QUIT:
                save_game()
                Animations.push_all()
                py.display.quit()
                py.quit()
                start = False

            manager.process_events(event)

        manager.update(ui_refres_rate)


# Checks if file is run as main file before initialising application and starting the main function.
if __name__ == "__main__":
    py.init()
    initialise()
    py.display.set_caption(settings["Farm_Name"])
    global screen
    screen = py.display.set_mode((settings["Window_Size"], settings["Window_Size"]))
    Animations.call_all()
    main()
