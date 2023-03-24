import pygame as py
import tiles
import data
import commands
import pygame_gui as py_gui


# Will iterate through the crops list in user data, updating it older plant tiles.
def update_crops():
    for i in range(9):
        if not (user_data.save_data["Crops"][i]["Tile_id"][0] == 0 or user_data.save_data["Crops"][i]["Tile_id"][1] == crop_data.info["Crops"][int(user_data.save_data["Crops"][i]["Tile_id"][0]) - 1]["max_type"] - 1):
            user_data.save_data["Crops"][i]["Tile_id"][1] += 1


# A static class to organise the animations used in the project.
class Animations:
    @staticmethod
    # A method to call all of the tiles, staggering them and using the .call animation from tiles
    def call_all():
        frames = 0
        t = 0
        loop = True
        while loop:
            frames += 1
            if (frames % 4 == 0) and (frames <= 36):
                t += 1
            for i in range(t):
                tile_pos[i].call(user_data.scaler)
            render()
            if frames >= 46:
                loop = False

    @staticmethod
    # A method to push all of the tiles, staggering them and using the .push animation from tiles
    def push_all():
        frames = 0
        t = 0
        loop = True
        while loop:
            frames += 1
            if (frames % 4 == 0) and (frames <= 36):
                t += 1
            for i in range(t):
                tile_pos[i].push(user_data.scaler)
            render()
            if frames >= 46:
                loop = False


# A render function that calls relevant actions before updating the display.
def render():
    ui_refresh_rate = clock.tick(30) / 500
    screen.fill((1, 14, 19))
    for i in range(9):
        x = user_data.save_data["Crops"][i]["Tile_id"]
        screen.blit(
            crop_data.textures[x[0]][x[1]],
            (tile_pos[i].goal_x, tile_pos[i].y)
        )
    for i in range(2):
        if overlay_data.opacity[i] >= 0:
            screen.blit(overlay_data.image[i], (0, 0))
            overlay_data.opacity[i] -= 1
    manager.update(ui_refresh_rate)
    manager.draw_ui(screen)
    py.display.update()


# The main function where the main game loop is run
def main():
    start = True
    tick = 0
    tick_update = user_data.tickrate
    auto_save = user_data.settings["Auto_Save"]
    while start:

        render()

        if tick >= tick_update:
            tick = 0
            update_crops()
            if auto_save:
                data.dump_save(user_data.save_data, user_data.settings)
                overlay_data.opacity[0] = 100
        else:
            tick += 1

        for event in py.event.get():
            if event.type == py_gui.UI_TEXT_ENTRY_FINISHED:

                print(commands.commands(event.text, user_data, overlay_data, crop_data))

            manager.process_events(event)

            if event.type == py.QUIT:
                data.dump_save(user_data.save_data, user_data.settings)
                overlay_data.opacity[0] = 100
                Animations.push_all()
                py.display.quit()
                py.quit()
                start = False


# Checks if file is run as main file before initialising application and starting the main function.
if __name__ == "__main__":
    # Initializes pygame
    clock = py.time.Clock()
    clock.tick(30)
    py.init()

    # Takes the user data and the tile library's/Data from around the file before dumping it to relevant classes.
    user_data = data.create_user_data()
    crop_data = data.initial_crop_data(user_data)
    overlay_data = data.initial_screen_overlay(user_data)
    tile_pos = tiles.initial_tile_POS(user_data.scaler)
    py.display.set_caption(user_data.settings["Farm_Name"])
    screen = py.display.set_mode((user_data.settings["Window_Size"], user_data.settings["Window_Size"]))
    manager = py_gui.UIManager((user_data.settings["Window_Size"], user_data.settings["Window_Size"]))
    overlay_data.opacity[0] = 100
    Animations.call_all()

    # Created the element for text input, allowing the user to input commands.
    text_input = py_gui.elements.UITextEntryLine(relative_rect=py.Rect((2 * user_data.scaler, 87 * user_data.scaler),
                (96*user_data.scaler, 11*user_data.scaler)), manager=manager, object_id="#main_text_entery"
    )

    main()
