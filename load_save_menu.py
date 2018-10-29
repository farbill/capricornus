import os
import time

import gameaction
from command_parsing import command_parsing
from main_menu import GAME_WIDTH, dotted_line, empty_line, print_in_the_middle, print_left_indented, write_over, \
    go_up_and_clear, exit_selection

from game_play import clear

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


def load_selection(the_input: str, slot_tracker: []) -> int:

    # inputs to be recognized as valid
    list_one =      [1, "1", "1.", "game1", "slot1", "game slot 1", "gameslot 1", "gameslot1", "game 1", "slot 1"]
    list_two =      [2, "2", "2.", "game2", "slot2", "game slot 2", "gameslot 2", "gameslot2", "game 2", "slot 2"]
    list_three =    [3, "3", "3.", "game3", "slot3", "game slot 3", "gameslot 3", "gameslot3", "game 3", "slot 3"]
    list_exit =     [4, "4", "exit", "quit", "q", "exit game", "quit game", "4. exit", "bye", "byebye", "back", "go back" ]

    selection = 0
    wrong_input = True
    the_input = str(the_input)
    lowered_input = the_input.lower()  # to make the input case insensitive

    while wrong_input:

        if command_parsing(lowered_input, list_one):
            selection = 1
            if slot_tracker[0] == False:
                write_over("Invalid choice. Save file does not exists.")
                go_up_and_clear()
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
                go_up_and_clear()
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
                go_up_and_clear()
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
            go_up_and_clear()
            command_line = "Make your selection >>> "
            the_input = input(command_line)
            the_input = str(the_input)
            lowered_input = the_input.lower()

    return int(selection)

def save_menu():
    game_version = "1.0"
    title = "Save Game"

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

    selection = save_selection(input("Make your selection >>> "), slot_tracker)

    return selection, slot_tracker

def save_selection(the_input: str, slot_tracker: []) -> int:

    # inputs to be recognized as valid
    list_one =      [1, "1", "1.", "game1", "slot1", "game slot 1", "gameslot 1", "gameslot1", "game 1", "slot 1"]
    list_two =      [2, "2", "2.", "game2", "slot2", "game slot 2", "gameslot 2", "gameslot2", "game 2", "slot 2"]
    list_three =    [3, "3", "3.", "game3", "slot3", "game slot 3", "gameslot 3", "gameslot3", "game 3", "slot 3"]
    list_exit =     [4, "4", "exit", "quit", "q", "exit game", "quit game", "4. exit", "bye", "byebye", "back", "go back" ]

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
            go_up_and_clear()
            command_line = "Make your selection >>> "
            the_input = input(command_line)
            the_input = str(the_input)
            lowered_input = the_input.lower()

    return int(selection)

# Offers user the load menu and load a game slot
def load_game(ga: gameaction.GameAction) -> (gameaction.GameAction, int):
    load_menu_choice = load_menu()
    if (1 <= load_menu_choice <= 3):
        ga.game_state.load_game_state(load_menu_choice)
    return (ga, load_menu_choice)

# Offers user the load menu in game
def ingame_load_game(ga: gameaction.GameAction) -> (gameaction.GameAction, int):
    load_menu_choice = load_menu()
    if (1 <= load_menu_choice <= 3):
        clear()
        if load_game_confirmation(load_menu_choice) == 2: # user chooses 'no'
            return (ga, 4)
        ga.game_state.load_game_state(load_menu_choice)
    return (ga, load_menu_choice)

def load_game_confirmation(slot_num: int):
    game_version = "1.0"
    msg1 = "Are you sure you want to load GAME SLOT " + str(slot_num) + "?"
    msg2 = "Any unsaved progress in current game will be loss."

    dotted_line_length = GAME_WIDTH
    dotted_line(dotted_line_length)
    empty_line(1)
    print_in_the_middle(dotted_line_length, msg1)
    print_in_the_middle(dotted_line_length, msg2)
    empty_line(1)
    dotted_line(dotted_line_length)

    selection = exit_selection(input("Yes/No >>> "))

    return selection

# Offers user the save menu in game
def ingame_save_game(ga: gameaction.GameAction) -> (gameaction.GameAction, int):
    save_menu_choice, slot_tracker = save_menu()
    if (1 <= save_menu_choice <= 3):
        clear()
        if slot_tracker[save_menu_choice - 1] is True: # if existing slot, confirm overwrite
            if save_game_confirmation(save_menu_choice) == 2: # user chooses 'no':
                return (ga, 4)
        ga.game_state.save_game_state(save_menu_choice)
    return (ga, save_menu_choice)

def save_game_confirmation(slot_num: int):
    game_version = "1.0"
    msg1 = "Are you sure you want to overwrite GAME SLOT " + str(slot_num) + "?"

    dotted_line_length = GAME_WIDTH
    dotted_line(dotted_line_length)
    empty_line(1)
    print_in_the_middle(dotted_line_length, msg1)
    empty_line(1)
    dotted_line(dotted_line_length)

    selection = exit_selection(input("Yes/No >>> "))

    return selection