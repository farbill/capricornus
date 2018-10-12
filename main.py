import main_menu
from game_play import *

def main():

    main_menu_choice = main_menu.main_menu()
    if main_menu_choice == 1:
        game_play()
    elif main_menu_choice == 2:
        print("TESTING PURPOSE:   LOAD GAME")
    elif main_menu_choice == 3:
        print("Exiting...\nGood Bye!")

# Game starts
main()
