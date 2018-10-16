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
title_narration_part1 = "Agent Dope, who is tasked with the mission of finding and appending " \
                  "Dr. Crime – a once renowned scientist from the affluent Crime family, " \
                  "known for their charity and philanthropy. After spending nearly a decade " \
                  "working on the theory of Dark Magic to restore Life, Dr. Crime’s work was " \
                  "met with great criticism and disapproval from the scientific community, and " \
                  "was ridiculed for such preposterous ideas. Dr. Crime went down a terrible " \
                  "spiral and started to use Dark Magic for mischief and evil. He vowed to " \
                  "take vengeance on the citizens of the city of New San Diego by using Dark " \
                  "Magic to poison the city and kill all of its citizens. "

title_narration_part2 = "The latest reconnaissance shows that Dr. Crime has established a lair " \
                    "which is protected by a Magical Barrier, which can only be destroyed by " \
                    "an individual who possess the Magical Orbs. The reconnaissance also revealed " \
                    "that Dr. Crime is clothed in a Magical Armor that can be only penetrated by " \
                    "the Magic Sword of Light. With none of these in hand, the cautious, yet " \
                    "courageous Agt. Dope must explore the city of New San Diego, find all the " \
                    "necessary artifacts, and use them to stop Dr. Crime before the poison is " \
                    "released. Hurry, time is ticking!"

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
    narration.narration(title_narration_part1, main_menu.GAME_WIDTH)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("\nPress any key to continue...\n")

    clear()

    main_menu.dotted_line(main_menu.GAME_WIDTH)
    narration.narration(title_narration_part2, main_menu.GAME_WIDTH)
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


