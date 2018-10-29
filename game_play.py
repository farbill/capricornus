import game_play_selection
import gameaction
import characters
import city
import load_save_menu

# import only system from os
from os import system, name

import narration
import main_menu
import time
from typing import Tuple

#for stub data
import stub_map

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

# Work in progress --------------------------
def gametext_output(ga, map_arr) -> Tuple[ Tuple[str, str, str, str],
                                            Tuple[str, str, str, str],
                                            city.District]:
    # Current x,y coord
    this_district = None
    district_exits = None
    xy_coord = (None, None)

    # North, South, West, East -- district info
    cardinal_dir = ["north", "south", "west", "east"]
    nswe_districts = [None, None, None, None]
    relative_coord = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    static_coord = [None, None, None, None]

    # Get x,y coords of current location
    for district_obj in map_arr:
        if ga.current_location == district_obj._district_name:
            this_district = district_obj
            district_exits = district_obj._district_exits.get_exits()
            xy_coord = district_obj._id.get_id()
            break

    # get N, S, W, E districts
    # https://stackoverflow.com/questions/1169725/adding-values-from-tuples-of-same-length
    for i in range(4):
        static_coord[i] = tuple(sum(x) for x in zip(xy_coord, relative_coord[i]))

    # Assign district names to NSWE
    for district_obj in map_arr:
        for i in range(4):
            if static_coord[i] == district_obj._id.get_id():
                nswe_districts[i] = district_obj._district_name

    # String to print
    str_to_print = None

    # Concat either long or short description
    if ga.check_visited(ga.current_location) == False:
        str_to_print = this_district._long_description
        ga.change_visited(ga.current_location)
    else:
        str_to_print = this_district._short_description

    # Print relevant item narration
    for item in this_district._district_items:
        str_to_print += " " + item.narration

    # Print narration
    narration.left_narration(str_to_print, main_menu.GAME_WIDTH)

    # TODO: Print dropped items

    main_menu.empty_line(3)

    for i in range(4):
        if nswe_districts[i] is not None:
            print("To the " + cardinal_dir[i] + " is " + nswe_districts[i] + ".", end=" ")
            if(district_exits[i] != ""):
                print(district_exits[i] + " is in that direction.")
            else:
                print("")
     
    #print(nswe_districts)
    #swe_districts = list(map(lambda x: x.lower() if x is not None else x, nswe_districts))
    #print(nswe_districts)
    return (nswe_districts, district_exits, this_district)

def general_info(ga, map_arr):
    main_menu.empty_line(2)
    main_menu.print_in_the_middle(main_menu.GAME_WIDTH, ("Remaining Turns:%s"%ga.turns_remaining))
    main_menu.print_in_the_middle(main_menu.GAME_WIDTH, ("Current Location:%s"%ga.current_location))
    main_menu.empty_line(2)
    (nswe_districts, district_exits, this_district) = gametext_output(ga, map_arr)
    main_menu.empty_line(2)
    legendary_status(ga)
    main_menu.empty_line(2)
    narration.help_menu()
    main_menu.empty_line(1)
    return (nswe_districts, district_exits, this_district)


def intro_narration():

    main_menu.dotted_line(main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    narration.narration(narration.start_narration1(), main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("\nPress [Enter] to continue...\n")

    clear()

    main_menu.dotted_line(main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    narration.narration(narration.start_narration2(), main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
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

#changes to different location and update the remaining turns
def location_change(ga, loc):
    ga.change_location(loc)
    ga.decrement_turns_remaining()
    clear()        
    

def game_play(ga: gameaction.GameAction):

    # TODO: Load in all game data

    # print("Initializing Character Information...")
    agt_dope = characters.AgentDope(narration.short_for_agt_dope(), narration.long_for_agt_dope())
    #Dr. Crime needs to be initialized with specified PUZZLE and DIALOGS
    dr_crime = characters.DrCrime(narration.short_for_dr_crime(), narration.long_for_dr_crime(), 0, 0)

    clear()
    # For new games, load in game data and play intro narration
    if ga.check_visited(STARTING_LOCATION) == False:
        map_arr = stub_map.get_map_stub()
        intro_narration()
        clear()
    else: # For load game, load stored map data into map_arr
        map_arr = ga.map_arr

    # Game loop
    while True:

        clear()

        # Display game stuff
        main_menu.dotted_line(main_menu.GAME_WIDTH)
        (nswe_districts, district_exits, this_district) = general_info(ga, map_arr)
        main_menu.dotted_line(main_menu.GAME_WIDTH)

        # Get validated input
        selection = game_play_selection.gameplay_selection(ga, input(">>> "), nswe_districts, district_exits, this_district)

        # Perform action based on key action noun
        if selection == "exit":
            clear()
            confirmation = main_menu.exit_to_main_confirmation()
            if confirmation == 1:
                break
        elif selection == "inventory":
            clear()
            narration.inventory_menu_screen(ga)
        elif selection == "help":
            clear()
            narration.help_menu_screen()
        elif selection == "go up":
            location_change(ga, nswe_districts[0])
        elif selection == "go down":
            location_change(ga, nswe_districts[1])
        elif selection == "go left":
            location_change(ga, nswe_districts[2])
        elif selection == "go right":
            location_change(ga, nswe_districts[3])
        elif selection == "savegame":
            clear()
            ga.set_map_arr(map_arr)
            ga, save_menu_choice = load_save_menu.ingame_save_game(ga)
            map_arr = ga.map_arr
        elif selection == "loadgame":
            clear()
            ga.set_map_arr(map_arr)
            ga, load_menu_choice = load_save_menu.ingame_load_game(ga)
            map_arr = ga.map_arr






