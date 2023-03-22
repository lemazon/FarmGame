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
        image = py.image.load("Textures/Overlay/" + str(i) + ".png")
        overlay_image.append(pygame.transform.scale(image, (settings["Window_Size"], settings["Window_Size"])))
    clock = py.time.Clock()
    clock.tick(30)
    global scaler
    scaler = settings["Window_Size"] / 100

    # Opens the tile info json file, loading it to global variable tile_ifo as a dict before iterating through
    # dictionary and dumping corresponding tile images into a 2d array for later use (i,e, rendering to screen).
    with open("tile_info.json") as data:
        global tile_info
        tile_info = json.load(data)
    global crop_tiles
    crop_tiles = []
    for i in range(tile_info["Crop_Num"]):
        tile = []
        for j in range((tile_info["Crops"])[i]["max_type"]):
            # Concatenates a string to use as a file directory.
            image = py.image.load("Textures/Crop Tiles/" + str(i + 1) + "." + str(j + 1) + ".png")
            tile.append(pygame.transform.scale(image, (settings["Window_Size"], settings["Window_Size"])))
        crop_tiles.append(tile)
    # Generates data for the pos of the tiles, dumping the info to an array
    global crop_data
    crop_data = [
        # Crop tile 1
        CropTiles(
            36 * scaler,
            7 * scaler,
            107 * scaler
        ),
        # Crop tile 2
        CropTiles(
            50 * scaler,
            14 * scaler,
            114 * scaler
        ),
        # Crop tile 3
        CropTiles(
            64 * scaler,
            21 * scaler,
            121 * scaler
        ),
        # Crop tile 4
        CropTiles(
            22 * scaler,
            14 * scaler,
            114 * scaler
        ),
        # Crop tile 5
        CropTiles(
            36 * scaler,
            21 * scaler,
            121 * scaler
        ),
        # Crop tile 6
        CropTiles(
            50 * scaler,
            28 * scaler,
            128 * scaler
        ),
        # Crop tile 7
        CropTiles(
            8 * scaler,
            21 * scaler,
            121 * scaler
        ),
        # Crop tile 8
        CropTiles(
            22 * scaler,
            28 * scaler,
            128 * scaler
        ),
        # Crop tile 9
        CropTiles(
            36 * scaler,
            35 * scaler,
            135 * scaler
        )
    ]


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
    frames = 0
    t = 0
    loop = True
    while loop:
        print(frames)
        frames += 1
        if (frames % 4 == 0) and (frames <= 36):
            t += 1
        for i in range(t):
            crop_data[i].call()
        render()
        if frames >= 46:
            loop = False

def push_animation():
    frames = 0
    t = 0
    loop = True
    while loop:
        print(frames)
        frames += 1
        if (frames % 4 == 0) and (frames <= 36):
            t += 1
        for i in range(t):
            crop_data[i].push()
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


class CropTiles:
    def __init__(self, goal_x, goal_y, y, ):
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.y = y

    def call(self):
        if (self.y - self.goal_y) >= 1:
            self.y = self.goal_y + (self.y - self.goal_y) / 2
        else:
            self.y = self.goal_y

    def push(self):
        if self.y >= (self.goal_y + 100 * scaler):
            self.y = (self.goal_y + 100 * scaler)
        elif self.y == self.goal_y:
            self.y += scaler
        else:
            self.y = self.goal_y + (self.y - self.goal_y)*2


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
            tick = + 1

        render()
        for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.enter:
                    return
            if event.type == py.QUIT:
                push_animation()
                save_game()
                py.display.quit()
                py.quit()


# Checks if file is run as main file before initialising application and starting the main function.
if __name__ == "__main__":
    py.init()
    initialise()
    py.display.set_caption(settings["Farm_Name"])
    global screen
    screen = py.display.set_mode((settings["Window_Size"], settings["Window_Size"]))
    call_animation()
    main()
