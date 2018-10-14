from main_menu import main_menu
from game_play import load_game, clear, game_play
import gamestate
import gameaction

def main():

    clear()

    # Global gamestate and gameaction instances
    gs = gamestate.GameState()
    ga = gameaction.GameAction(gs)

    main_menu_choice = main_menu()

    if main_menu_choice == 1:
        game_play(ga)
    elif main_menu_choice == 2:
        clear()
        ga = load_game(ga)
        # game_play(ga)
    elif main_menu_choice == 3:
        # insert confirmation check
        print("Exiting...\nGood Bye!")



# Game starts
if __name__ == "__main__":
    main()
