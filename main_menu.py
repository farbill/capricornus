import sys
from command_parsing import command_parsing

TIME_TO_WAIT_FOR_WRITE_OVER = 1

#####################################################################################################################
# Main  Menu
# Displayed when the game starts
#
# Ref: https://stackoverflow.com/questions/465348/how-can-i-print-over-the-current-line-in-a-command-line-application
#####################################################################################################################

# GLOBAL VARIABLE

GAME_WIDTH = 100

def go_up_and_clear():
    sys.stdout.write("\033[F")      # go up one line
    sys.stdout.write("\033[K")      # clear line

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
            go_up_and_clear()
            command_line = "Make your selection >>> "
            the_input = input(command_line)
            the_input = str(the_input)
            lowered_input = the_input.lower()
    return int(selection)


def exit_selection(the_input) -> int:

    # inputs to be recognized as valid
    list_one =      ["y", "yes", "yep", "true", "ye", "yse", "1"]
    list_two =      ["n", "no", "nope", "false", "nah", "0"]

    selection = 0
    wrong_input = True
    the_input = str(the_input)
    lowered_input = the_input.lower()  # to make the input case insensitive

    while wrong_input:

        if command_parsing(lowered_input, list_one):  # yes
            selection = 1
            break

        if command_parsing(lowered_input, list_two): # no
            selection = 2
            break

        if wrong_input:
            if len(the_input) > 99:
                write_over("Your input is too long.")
            write_over("Invalid Input.  Try again.")
            go_up_and_clear()
            command_line = "Yes/No >>> "
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
