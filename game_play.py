import gamestate
import gameaction
import characters

# import only system from os
from os import system, name
import narration
import main_menu
import time

STARTING_LOCATION = "City Hall"

# define our clear function
# Ref: https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def intro_narration():

    main_menu.dotted_line(main_menu.GAME_WIDTH)
    narration.narration(narration.start_narration1(), main_menu.GAME_WIDTH)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("\nPress [Enter] to continue...\n")

    clear()

    main_menu.dotted_line(main_menu.GAME_WIDTH)
    narration.narration(narration.start_narration2(), main_menu.GAME_WIDTH)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("\nPress [Enter] to continue...\n")

def legendary_status(ga):
    legendary_list = ga.check_legendary()
    status_list = [None] * 4
    for i in range(0, 4):
        if legendary_list[i] == False:
            status_list[i] = "Empty  "
        else:
            status_list[i] = "On hand"
    
    vision_and_strength = "Vision Orb:   %s   Strength Orb: %s"%(status_list[0], status_list[1])
    vitality_and_magic  = "Vitality Orb: %s   Magic Sword:  %s"%(status_list[2], status_list[3])
    main_menu.print_in_the_middle(main_menu.GAME_WIDTH, vision_and_strength)
    main_menu.print_in_the_middle(main_menu.GAME_WIDTH, vitality_and_magic)


def game_play(ga: gameaction.GameAction):

    clear()

    # For new games, play intro narration
    if ga.check_visited(STARTING_LOCATION) == False:
        intro_narration()
    
    clear()
    
    print("Initializing Character Information...")
    # time.sleep(1)

    agt_dope = characters.AgentDope(narration.short_for_agt_dope(), narration.long_for_agt_dope())

    #Dr. Crime needs to be initialized with specified PUZZLE and DIALOGS
    dr_crime = characters.DrCrime(narration.short_for_dr_crime(), narration.long_for_dr_crime(), 0, 0)

    # Game loop
    while True:

        clear()

        # TODO: display game stuff
        main_menu.dotted_line(main_menu.GAME_WIDTH)
        main_menu.empty_line(3)
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, ("Remaining Turns:%s"%ga.turns_remaining))
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, ("Current Location:%s"%ga.current_location))
        legendary_status(ga)
        main_menu.empty_line(3)
        main_menu.dotted_line(main_menu.GAME_WIDTH)

        # get validated input
        selection = main_menu.gameplay_selection(input(">>> "))
        print("TESTING - YOU'VE SELECTED: " + selection)
        time.sleep(1)

        # TODO: perform action
        # ....

	
        if selection == "exit":
            clear()
            confirmation = main_menu.exit_to_main_confirmation()
            if confirmation == 1:
                break

# Offers user the load menu and load a game slot
def load_game(ga: gameaction.GameAction) -> (gameaction.GameAction, int):
    load_menu_choice = main_menu.load_menu()
    if (1 <= load_menu_choice <= 3):
        ga.game_state.load_game_state(load_menu_choice)
    return (ga, load_menu_choice)
