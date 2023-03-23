Welcome to FarmGame

requirements:
    Python 3.10 or higher
    models:
    pygame
    pygame gui
    json
    random

settings:
    The settings file contain a multitude of variables that will be used throughout the project, these are called upon
    from the settings.json file which can be edited using a text editor, (i.e. notepad, notepad++, or word).
    Windows_Size:
    -size in pixels of game screen
    Tick_Rate:
    -how many ticks occur per minute, a tick controls the update cycle of the farm and can be computationally demanding
    Farm_Name:
    -the name your farm will be referred to
    Save_File_Name:
    -The name of your save file, it should also contain the directory if the file is not saved in the game folder

inserting new plants:
    If you with to insert new plants into the game you can do so through the tile_info.json file, opening it inside a
    text editor and inserting a new Crop underneath the "Crop" title as a dictionary with the keys: "max_type" (the
    largest possible growth state), and "Chance" (the chance that a crop matures per minute).


