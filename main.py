import command_parsing
import load_save_menu
import main_menu
import game_play
import gamestate
import gameaction
import sys

def main():

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
