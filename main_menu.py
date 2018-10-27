import sys
import time
from command_parsing import command_parsing
import os
import game_play
from typing import Tuple, List
import city
from items import ActionType

TIME_TO_WAIT_FOR_WRITE_OVER = 1

#####################################################################################################################
# Main  Menu
# Displayed when the game starts
#
# Ref: https://stackoverflow.com/questions/465348/how-can-i-print-over-the-current-line-in-a-command-line-application
#####################################################################################################################

# GLOBAL VARIABLE

GAME_WIDTH = 100


def dotted_line(count):
    print("-" * count)


def empty_line(count):
    for i in range(count):
        print("")


def empty_space(count):
    space = ""
    for i in range(count):
        space += " "
    print(space, end=" ")


def print_in_the_middle(line_length, the_string):
    string_len = len(the_string)
    count = int((line_length / 2) - (string_len / 2))
    space = ""
    for i in range(count):
        space += " "
    print(space, end=" ")
    print(the_string)

def print_left_indented(indentation, the_string):
    space = ""
    for i in range(indentation):
        space += " "
    print(space, end=" ")
    print(the_string)


def write_over(the_string):
    sys.stdout.write(the_string)
    sys.stdout.flush()
    # time.sleep(TIME_TO_WAIT_FOR_WRITE_OVER)
    # sys.stdout.write('\r')
    # sys.stdout.flush()
    # sys.stdout.write(" " * 99)
    # sys.stdout.flush()
    # sys.stdout.write('\r')
    # sys.stdout.flush()

def main_selection(the_input):

    # inputs to be recognized as valid
    list_one = [1, "1", "new", "new game", "1. new game", "start", "begin", "go", "play"]
    list_two = [2, "2", "load", "load game", "2. load game", "continue"]
    list_three = [3, "3", "exit", "quit", "exit game", "quit game", "3. exit", "bye"]

    selection = 0
    wrong_input = True
    the_input = str(the_input)
    lowered_input = the_input.lower()  # to make the input case insensitive

    while wrong_input:

        if command_parsing(lowered_input, list_one):
            selection = 1
            break

        if command_parsing(lowered_input, list_two):
            selection = 2
            break

        if command_parsing(lowered_input, list_three):
            selection = 3
            break

        if wrong_input:
            if len(the_input) > 99:
                write_over("Your input is too long.")
            write_over("Invalid Input.  Try again.")
            sys.stdout.write("\033[F")      # go up one line
            sys.stdout.write("\033[K")      # clear line
            command_line = "Make your selection >>> "
            the_input = input(command_line)
            the_input = str(the_input)
            lowered_input = the_input.lower()
    return int(selection)

def load_selection(the_input: str, slot_tracker: []) -> int:

    # inputs to be recognized as valid
    list_one =      [1, "1", "1.", "game1", "slot1", "game slot 1", "gameslot 1", "gameslot1", "game 1", "slot 1"]
    list_two =      [2, "2", "2.", "game2", "slot2", "game slot 2", "gameslot 2", "gameslot2", "game 2", "slot 2"]
    list_three =    [3, "3", "3.", "game3", "slot3", "game slot 3", "gameslot 3", "gameslot3", "game 3", "slot 3"]
    list_exit =     [4, "4", "exit", "quit", "q", "exit game", "quit game", "4. exit", "bye", "byebye"]

    selection = 0
    wrong_input = True
    the_input = str(the_input)
    lowered_input = the_input.lower()  # to make the input case insensitive

    while wrong_input:

        if command_parsing(lowered_input, list_one):
            selection = 1
            if slot_tracker[0] == False:
                write_over("Invalid choice. Save file does not exists.")
                sys.stdout.write("\033[F")  # go up one line
                sys.stdout.write("\033[K")  # clear line
                command_line = "Make your selection >>> "
                the_input = input(command_line)
                the_input = str(the_input)
                lowered_input = the_input.lower()
                continue
            break

        if command_parsing(lowered_input, list_two):
            selection = 2
            if slot_tracker[1] == False:
                write_over("Invalid choice. Save file does not exists.")
                sys.stdout.write("\033[F")  # go up one line
                sys.stdout.write("\033[K")  # clear line
                command_line = "Make your selection >>> "
                the_input = input(command_line)
                the_input = str(the_input)
                lowered_input = the_input.lower()
                continue
            break

        if command_parsing(lowered_input, list_three):
            selection = 3
            if slot_tracker[2] == False:
                write_over("Invalid choice. Save file does not exists.")
                sys.stdout.write("\033[F")  # go up one line
                sys.stdout.write("\033[K")  # clear line
                command_line = "Make your selection >>> "
                the_input = input(command_line)
                the_input = str(the_input)
                lowered_input = the_input.lower()
                continue
            break

        if command_parsing(lowered_input, list_exit):
            selection = 4
            break

        if wrong_input:
            if len(the_input) > 99:
                write_over("Your input is too long.")
            write_over("Invalid Input.  Try again.")
            sys.stdout.write("\033[F")      # go up one line
            sys.stdout.write("\033[K")      # clear line
            command_line = "Make your selection >>> "
            the_input = input(command_line)
            the_input = str(the_input)
            lowered_input = the_input.lower()

    return int(selection)

def exit_selection(the_input) -> int:

    # inputs to be recognized as valid
    list_one =      ["y", "yes", "yep", "true"]
    list_two =      ["n", "no", "nope", "false"]

    selection = 0
    wrong_input = True
    the_input = str(the_input)
    lowered_input = the_input.lower()  # to make the input case insensitive

    while wrong_input:

        if command_parsing(lowered_input, list_one):
            selection = 1
            break

        if command_parsing(lowered_input, list_two):
            selection = 2
            break

        if wrong_input:
            if len(the_input) > 99:
                write_over("Your input is too long.")
            write_over("Invalid Input.  Try again.")
            sys.stdout.write("\033[F")      # go up one line
            sys.stdout.write("\033[K")      # clear line
            command_line = "Yes/No >>> "
            the_input = input(command_line)
            the_input = str(the_input)
            lowered_input = the_input.lower()

    return int(selection)


def gameplay_selection(ga, the_input: str,
                       nswe_districts: Tuple[str, str, str, str],
                       district_exits: Tuple[str, str, str, str],
                       this_district: city.District) -> str:

    screen_refresh = False
    # Change nswe_districts to lower case
    # e.g. ['hawkins', None, 'greenland grove', 'oak square']
    nswe_districts = list(map(lambda x: x.lower() if x is not None else x, nswe_districts))

    # Change district_exits to lower case
    # e.g. ['dayton dr', '', 'summer ln', 'shore blvd']
    district_exits = list(map(lambda x: x.lower() if x is not None else x, district_exits))

    # 2D general action array
    #   1st element of each 1D action list is the key action noun
    general_action_array = [
        ["exit", "quit", "q", "exit game", "quit game", "bye", "byebye", "main", "main menu"],
        ["inventory", "bag", "open inventory", "open bag", "see inventory", "check inventory"],
        ["help", "help me", "manual", "guide", "q&a", "open help"],
        # ....
    ]

    # 2D NSWE movement array
    #   1st element of each 1D action list is the key action noun
    nswe_actions = [    ["go up", "go north", "go to north", "north", "up"],
                        ["go down", "go south", "go to south", "south", "down"],
                        ["go left", "go west", "go to west", "west", "left"],
                        ["go right", "go east", "go to east", "east", "right"]      ]

    # Add additional word parsing for each NSEW movement based on district name
    for i in range(4):
        if nswe_districts[i] is not None:
            arr = nswe_actions[i]
            whole_name = nswe_districts[i]                  # ex: 'greenland grove'
            first_word = whole_name.split()[0]              # ex: 'greenland'
            arr.append(whole_name)                          # ex: greenland grove
            arr.append(first_word)                          # ex: greenland
            arr.append("go " + whole_name)                  # ex: go greenland grove
            arr.append("go to " + whole_name)               # ex: go to greenland grove
            arr.append("go " + first_word)                  # ex: go greenland
            arr.append("go to " + first_word)               # ex: go to greenland
            arr.append("travel " + whole_name)              # ex: travel greenland grove
            arr.append("travel to " + whole_name)           # ex: travel to greenland grove
            arr.append("travel " + first_word)              # ex: travel greenland
            arr.append("travel to " + first_word)           # ex: travel to greenland
            general_action_array.append(arr)

            if district_exits[i] != "":
                whole_exit_name = district_exits[i]             # ex: 'shore blvd'
                first_exit_word = whole_exit_name.split()[0]    # ex: 'shore'
                arr.append(whole_exit_name)                     # ex: shore blvd
                arr.append(first_exit_word)                     # ex: shore
                arr.append("go " + whole_exit_name)             # ex: go shore blvd
                arr.append("go to " + whole_exit_name)          # ex: go to shore blvd
                arr.append("go " + first_exit_word)             # ex: go shore
                arr.append("go to " + first_exit_word)          # ex: go to shore
                arr.append("travel " + whole_exit_name)              # ex: travel shore blvd
                arr.append("travel on " + whole_exit_name)           # ex: travel on shore blvd
                arr.append("travel " + first_exit_word)              # ex: travel shore
                arr.append("travel on " + first_exit_word)           # ex: travel on shore

            general_action_array.append(arr)

    # Build district_items_action array for items in district
    district_items_action = []
    for item in this_district._district_items:
        for action in item.action:
            for command in action.commands:
                district_items_action.append(command)

    selection = None
    the_input = str(the_input).lower()  # to make the input case insensitive

    while selection == None:

        # Check for valid action in general action array
        for action_list in general_action_array:
            if the_input in action_list:
                selection = action_list[0]
                break

        # TODO: Check for district-specific action
        # ...
        if the_input in district_items_action:
            for item in this_district._district_items:
                for action in item.action:
                    if the_input in action.commands:
                        if action.response_type == ActionType.DISPLAY:
                            sys.stdout.write("\033[K")  # clear line
                            print(action.response)
                            screen_refresh = False
                        if action.response_type == ActionType.ACTION:
                            if action.more_response_type == ActionType.TAKE_LEGENDARY:
                                sys.stdout.write("\033[K")  # clear line
                                print(action.response)
                                ga.add_to_inventory(item.name)
                                if item.name == "Vision Orb":
                                    ga.add_to_inventory(item)
                                    ga.game_state._vision_orb = True
                                    time.sleep(2)
                                elif item.name == "Magic Sword":
                                    ga.add_to_inventory(item)
                                    ga.game_state._magic_sword = True
                                    time.sleep(2)
                                screen_refresh = True
                            elif action.more_response_type == ActionType.TAKE_ITEM:
                                sys.stdout.write("\033[K")  # clear line
                                print(action.response)
                                ga.add_to_inventory(item.name)
                                screen_refresh = False
                if screen_refresh == True:
                    break
            if screen_refresh == True: 
                break
            
                            
            sys.stdout.write("\033[F")      # go up one line
            sys.stdout.write("\033[F")      # go up one line
            sys.stdout.write("\033[K")      # clear line
            the_input = str(input(">>> ")).lower()
            continue

        # Else, bad action
        if screen_refresh == True:
            screen_refresh == False
            continue
        else:
            if selection == None:
                if len(the_input) > 99:
                    write_over("Your input is too long.")
                write_over("Invalid Input.  Try again.")
                sys.stdout.write("\033[K")      # clear line
                sys.stdout.write("\033[F")      # go up one line
                sys.stdout.write("\033[K")      # clear line
                the_input = str(input(">>> ")).lower()

    return selection


def main_menu():
    game_version = "1.0"
    title = "New San Diego Saga"

    # Main Menu Options
    new_game = "1. New Game "
    load_game = "2. Load Game"
    exit_game = "3. Exit     "

    dotted_line_length = GAME_WIDTH
    dotted_line(dotted_line_length)

    empty_line(1)

    print_in_the_middle(dotted_line_length, title)


    empty_line(1)
    print_in_the_middle(dotted_line_length, new_game)
    print_in_the_middle(dotted_line_length, load_game)
    print_in_the_middle(dotted_line_length, exit_game)
    empty_line(1)

    print("Ver. " + game_version)
    dotted_line(dotted_line_length)

    command_line = "Make your selection >>> "

    the_input = input(command_line)

    selection = main_selection(the_input)

    return selection


def load_menu():
    game_version = "1.0"
    title = "Load Game"

    # Load Menu Options
    menu_options = ["1. Game Slot 1",
                    "2. Game Slot 2",
                    "3. Game Slot 3",
                    "4. Go back"        ]

    slot_tracker = [False, False, False]

    dirname = os.path.join(os.path.realpath('.'), "savedgames")

    for num in range(3):
        game_slot = num + 1
        filename = "savedgame_" + str(game_slot)
        fullpath = os.path.join(dirname, filename)
        if os.path.exists(fullpath):
            menu_options[num] += " -- " + str(time.ctime(os.path.getmtime(fullpath)))
            slot_tracker[num] = True
        else:
            menu_options[num] += " -- no file"

    dotted_line_length = GAME_WIDTH
    dotted_line(dotted_line_length)

    empty_line(1)

    print_in_the_middle(dotted_line_length, title)

    empty_line(1)
    for x in menu_options:
        print_left_indented(int(dotted_line_length/3.5), x)
    empty_line(1)

    print("Ver. " + game_version)
    dotted_line(dotted_line_length)

    selection = load_selection(input("Make your selection >>> "), slot_tracker)

    return selection

def exit_game_confirmation():
    game_version = "1.0"
    title = "Are you sure you want to exit the GAME?"

    dotted_line_length = GAME_WIDTH
    dotted_line(dotted_line_length)
    empty_line(1)
    print_in_the_middle(dotted_line_length, title)
    empty_line(1)
    dotted_line(dotted_line_length)

    selection = exit_selection(input("Yes/No >>> "))

    return selection

def exit_to_main_confirmation():
    game_version = "1.0"
    msg1 = "Are you sure you want to exit to MENU?"
    msg2 = "Any unsaved progress will be loss."

    dotted_line_length = GAME_WIDTH
    dotted_line(dotted_line_length)
    empty_line(1)
    print_in_the_middle(dotted_line_length, msg1)
    print_in_the_middle(dotted_line_length, msg2)
    empty_line(1)
    dotted_line(dotted_line_length)

    selection = exit_selection(input("Yes/No >>> "))

    return selection
