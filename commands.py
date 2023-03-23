import data


def commands(command, user, overlay):
    command = command.split(" ")
    match command[0]:
        case "hello":
            print("hello", user.settings["Farm_Name"]+"s")
        case "save":
            overlay.opacity[0] = 100
            data.dump_save(user.save_data, user.settings)
        case "water":
            overlay.opacity[1] = 100

