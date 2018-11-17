import sys
import os
import time

import game_play
import gameaction
import gamestate
import load_save_menu
import main_menu
import narration

MINIMUM_WIDTH = 101
MINIMUM_HEIGHT = 35

def main():

    # Ensure window size is a minimum of 101 (width) x 35 (height)
    size_info = os.get_terminal_size()
    if size_info.columns < MINIMUM_WIDTH or size_info.lines < MINIMUM_HEIGHT:
        game_play.end_game_screen("Your window size must be a minimum of "
                                  "{0} (width) x {1} (height) to play the game.".format(MINIMUM_WIDTH, MINIMUM_HEIGHT),
                                  "Please try again.")
        return

    game_play.end_game_screen("Your window size must be a minimum of "
                              "{0} (width) x {1} (height) to play the game.".format(MINIMUM_WIDTH, MINIMUM_HEIGHT),
                              "Your window size currently satisfies this requirement. Remember to not change the window size during game play. Thank you!")

    while True:

        # Global gamestate and gameaction instances
        gs = gamestate.GameState()
        ga = gameaction.GameAction(gs)

        main_menu.clear_screen()
        main_menu_choice = main_menu.main_menu()

        if main_menu_choice == 1:
            game_play.game_play(ga)
        elif main_menu_choice == 2:
            main_menu.clear_screen()
            ga, load_menu_choice = load_save_menu.load_game(ga)
            if load_menu_choice == 4:
                continue
            game_play.game_play(ga)
        elif main_menu_choice == 3:
            # insert confirmation check
            main_menu.clear_screen()
            exit_choice = main_menu.exit_game_confirmation()
            if exit_choice == 2:    # 1 == exit, 2 == stay
                continue
            sys.stdout.write("\033[K")  # clear line
            print("\nThanks for playing! Good-bye!")
            input("\nPress [Enter] to continue...\n")
            break



# Game starts
if __name__ == "__main__":
    main()
