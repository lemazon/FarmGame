import data
import datetime


def commands(cm, user, overlay, crop):
    command = cm.split(" ")
    match command[0]:
        case "hello":
            print("hello", user.settings["Farm_Name"]+"s")
        case "save":
            overlay.opacity[0] = 100
            data.dump_save(user.save_data, user.settings)
            return "Game saved"
        case "water":
            overlay.opacity[1] = 100
            return "Plants watered"
        case "plant":
            return
        case "inventory":
            return
        case "shop":
            message = ""
            for i in range(crop.info["Crop_Num"]):
                message = message + crop.info["Name"][i] + " : " + str(crop.info["Crops"][i]["Price"]) + "\n"
            return message
        case "buy":
            return
        case "query":
            return
        case "harvest":
            return
        case _:
            return str("Unknown command: " + cm)


