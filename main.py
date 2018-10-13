import main_menu
from game_play import *
import gamestate
import gameaction

def main():

    # Global gamestate and gameaction instances
    gs = gamestate.GameState()
    ga = gameaction.GameAction(gs)

    main_menu_choice = main_menu.main_menu()

    if main_menu_choice == 1:
        game_play(ga)
    elif main_menu_choice == 2:
        print("TESTING PURPOSE:   LOAD GAME")
        ga = load_game(ga)
        game_play(ga)
    elif main_menu_choice == 3:
        # insert confirmation check
        print("Exiting...\nGood Bye!")



# Game starts
if __name__ == "__main__":
    main()
