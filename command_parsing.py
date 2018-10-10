def command_parsing(command, allowed_list):
    for i in allowed_list:
        if command == i:
            return 1

    return 0