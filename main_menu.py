import sys
import time

#####################################################################################################################
# Main  Menu
# Displayed when the game starts
#
# Ref: https://stackoverflow.com/questions/465348/how-can-i-print-over-the-current-line-in-a-command-line-application
#####################################################################################################################


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


def write_over(the_string):
    sys.stdout.write(the_string)
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(" " * 99)
    sys.stdout.flush()
    sys.stdout.write('\r')
    sys.stdout.flush()


def main_selection():
    command_line = "Make your selection >>> "
    the_input = input(command_line)

    # inputs to be recognized as valid
    list_one = [1, "1", "new", "new game", "1. new game"]
    list_two = [2, "2", "load", "load game", "2. load game"]
    list_three = [3, "3", "exit", "quit", "exit game", "quit game", "3. exit"]

    selection = 0
    wrong_input = True
    lowered_input = the_input.lower()  # to make the input case insensitive

    while wrong_input:

        for i in list_one:
            if lowered_input == i:
                selection = 1
                wrong_input = False
                break

        for i in list_two:
            if lowered_input == i:
                selection = 2
                wrong_input = False
                break

        for i in list_three:
            if lowered_input == i:
                selection = 3
                wrong_input = False
                break

        if wrong_input:
            if len(the_input) > 99:
                write_over("Your input is too long.")
            write_over("Invalid Input.  Try again.")
            the_input = input(command_line)
            lowered_input = the_input.lower()
    return selection


def main_menu():
    game_version = "1.0"
    title = "New San Diego Saga"

    # Main Menu Options
    new_game = "1. New Game "
    load_game = "2. Load Game"
    exit_game = "3. Exit     "

    dotted_line_length = 100
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

    selection = main_selection()

    # FOR TESTING
    print("FOR TESTING: Value returned from main_menu() is %s."%selection)

    return selection
