import sys
import time
from command_parsing import command_parsing
import os
import game_play

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
    time.sleep(2)
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(" " * 99)
    sys.stdout.flush()
    sys.stdout.write('\r')
    sys.stdout.flush()


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
            command_line = "Make your selection >>> "
            the_input = input(command_line)
            the_input = str(the_input)
            lowered_input = the_input.lower()
    return int(selection)

def load_selection(the_input) -> int:

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
            break

        if command_parsing(lowered_input, list_two):
            selection = 2
            break

        if command_parsing(lowered_input, list_three):
            selection = 3
            break

        if command_parsing(lowered_input, list_exit):
            selection = 4
            break

        if wrong_input:
            if len(the_input) > 99:
                write_over("Your input is too long.")
            write_over("Invalid Input.  Try again.")
            command_line = "Make your selection >>> "
            the_input = input(command_line)
            the_input = str(the_input)
            lowered_input = the_input.lower()

    return int(selection)


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
                    "4. Exit"           ]

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

    while True:

        game_play.clear()

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

        command_line = "Make your selection >>> "

        # the_input = input(command_line)

        selection = load_selection(input(command_line))

        if 1 <= selection <= 3 and slot_tracker[selection - 1] == False:
            empty_line(2)
            print_left_indented(int(dotted_line_length/3.5), "Invalid choice. Save file does not exists.")
            empty_line(2)
        else:
            break

    return selection

