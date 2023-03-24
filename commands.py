import data
import datetime


def commands(cm, user, overlay, crop):
    command = cm.split()
    match command[0]:
        case "hello":
            return print("hello", user.settings["Farm_Name"]+"s")

        case "save":
            overlay.opacity[0] = 100
            data.dump_save(user.save_data, user.settings)
            return "Game saved"

        case "water":
            overlay.opacity[1] = 100
            return "Plants watered"

        case "plant":
            if command[2] in user.save_data["Inventory"].keys():
                print("1")
                user.save_data["Inventory"][command[2]] -= 1
                if user.save_data["Inventory"][command[2]] == 0:
                    print("2")
                    del user.save_data["Inventory"][command[2]]

                user.save_data["Crops"][command[2]]["Tile_id"] = [crop.info["Name"].index(command[1]), 0]
                print([crop.info["Name"].index(command[1]), 0])

            return "Planted" + command[1]

        case "inventory":
            return user.save_data["Inventory"]

        case "money":
            return "money: " + str(user.save_data["Money"])

        case "shop":
            message = ""
            for i in range(crop.info["Crop_Num"]):
                message = message + crop.info["Name"][i] + " : " + str(crop.info["Crops"][i]["Price"]) + "\n"
            return message

        case "buy":
            return

        case "harvest":
            try:
                pos = command[1]
                harvest = user.save_data["Crops"][pos]["Tile_id"]
                print(harvest)
                if (crop.info["Crops"][(harvest[0]-1)]["max_type"] - 1) == harvest[1]:
                    user.save_data["Money"] = user.save_data["Money"] + crop.info["Crops"][harvest[0]-1]["Harvest"]

                user.save_data["Crops"][pos]["Tile_id"] = [0, 0]

                return "Crop harvested"

            except:
                return "Invalid args"


        case _:
            return str("Unknown command: " + cm)


