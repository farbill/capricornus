import gamestate
import gameaction
import characters

# import only system from os
from os import system, name
import narration
import main_menu
import time

# define our clear function
# Ref: https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#Game Start Narration
short_for_agt_dope = "An elite secret agent who's after Dr. Crime" 

long_for_agt_dope  = "An elite secret agent who is an expert in forensic and many other scientific " \
                     "principles with multiple years of training MMA."
				  
short_for_dr_crime = "An evil scientist who was once renowned scientist from the affluent Crime family, " \
                   "known for their charity and philanthropy."

long_for_dr_crime  = "An evil scientist who was once renowned scientist from the affluent Crime family, " \
                   "known for their charity and philanthropy, who spent nearly a decade " \
                   "working on the theory of Dark Magic to restore Life." 

def game_play(ga: gameaction.GameAction):

    clear()

    main_menu.dotted_line(main_menu.GAME_WIDTH)
    narration.narration(narration.start_narration1(), main_menu.GAME_WIDTH)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("\nPress any key to continue...\n")

    clear()

    main_menu.dotted_line(main_menu.GAME_WIDTH)
    narration.narration(narration.start_narration2(), main_menu.GAME_WIDTH)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("\nPress any key to continue...\n")
    
    clear()

    # print("\n\nTEST PURPOSE: GameState class for a new game need to be instantiated")
    # print("TEST PURPOSE: GameAction classes need to be instantiated")
    print("TEST PURPOSE: Agent Dope class needs to be instantiated")
    print("TEST PURPOSE: Dr. Crime class needs to be instantiated")
    print("TEST PURPOSE: City class needs to be instantiated")
    print("TEST PURPOSE: District classes need to be instantiated")
    print("TEST PURPOSE: Item classes need to be instantiated")
    print("TEST PURPOSE: Puzzle classes need to be instantiated\n")
    
    print("Initializing Character Information...")
    time.sleep(1)
    agt_dope = characters.AgentDope(short_for_agt_dope, long_for_agt_dope)
	#Dr. Crime needs to be initialized with specified PUZZLE and DIALOGS
    dr_crime = characters.DrCrime(short_for_dr_crime, long_for_dr_crime, 0, 0)
   
    print("Initializing Item Data...")
    time.sleep(1)
	
    print("Initializing Puzzle Data...")
    time.sleep(1)
	
    print("Initializing Location Data...")
    time.sleep(1)

def load_game(ga: gameaction.GameAction) -> gameaction.GameAction:
    # print("Load_game function called")
    # print("- Call load game function in GameAction class to load into GameState")
    # print("- return a loaded GameAction class obj")

    load_menu_choice = main_menu.load_menu()
    print("load_menu() returned: " + str(load_menu_choice))

    return ga


