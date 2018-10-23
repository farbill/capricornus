import gamestate
import gameaction
import characters
import city

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

# Work in progress --------------------------
def gametext_output(ga, map_arr) -> [str, str, str, str]:
    # Current x,y coord
    this_district = None
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
            xy_coord = district_obj._id.get_id()

    # get N, S, W, E districts
    # https://stackoverflow.com/questions/1169725/adding-values-from-tuples-of-same-length
    for i in range(4):
        static_coord[i] = tuple(sum(x) for x in zip(xy_coord, relative_coord[i]))

    # Assign district names to NSWE
    for district_obj in map_arr:
        for i in range(4):
            if static_coord[i] == district_obj._id.get_id():
                nswe_districts[i] = district_obj._district_name

    # main_menu.empty_line(1)
    if ga.check_visited(ga.current_location) == False:
        print(this_district._long_description)
        ga.change_visited(ga.current_location)
    else:
        print(this_district._short_description)
    main_menu.empty_line(3)

    for i in range(4):
        if nswe_districts[i] is not None:
            print("To the " + cardinal_dir[i] + " is " + nswe_districts[i] + ".")
     
    #print(nswe_districts)
    #swe_districts = list(map(lambda x: x.lower() if x is not None else x, nswe_districts))
    #print(nswe_districts)

    return nswe_districts

def general_info(ga, map_arr):
    main_menu.empty_line(2)
    main_menu.print_in_the_middle(main_menu.GAME_WIDTH, ("Remaining Turns:%s"%ga.turns_remaining))
    main_menu.print_in_the_middle(main_menu.GAME_WIDTH, ("Current Location:%s"%ga.current_location))
    main_menu.empty_line(2)
    nswe_districts = gametext_output(ga, map_arr)
    main_menu.empty_line(2)
    legendary_status(ga)
    main_menu.empty_line(2)
    narration.help_menu()
    main_menu.empty_line(1)
    return nswe_districts


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


def game_play(ga: gameaction.GameAction):

    # TODO: Load in all game data

    # Initializing a small map for TESTING ----------------------------
    city_hall = city.District(city.DistrictId(2, 3),
                              "City Hall",
                              ["an item - key1"],
                              ["a clue - the eagle has landed1"],
                              [], # character list
                              "City Hall short description",
                              "City Hall long description")
    hawkins = city.District(city.DistrictId(2, 4),
                              "Hawkins",
                              ["an item - key2"],
                              ["a clue - the eagle has landed2"],
                              [], # character list
                              "Hawkins short description",
                              "Hawkins long description")
    greenland_grove = city.District(city.DistrictId(1, 3),
                              "Greenland Grove",
                              ["an item - key3"],
                              ["a clue - the eagle has landed3"],
                              [], # character list
                              "Greenland Grove short description",
                              "Greenland Grove long description")
    oak_square = city.District(city.DistrictId(3, 3),
                              "Oak Square",
                              ["an item - key4"],
                              ["a clue - the eagle has landed4"],
                              [], # character list
                              "Oak Square short description",
                              "Oak Square long description")
    
    #Hyoung's portion:
    washington_heights = city.District(city.DistrictId(1, 2),
                              "Washington Heights",
                              ["an item - key5"],
                              ["a clue - the eagle has landed5"],
                              [], # character list
                              "Washington Heights short description",
                              "Wahsington Heights long description")
    gato_springs = city.District(city.DistrictId(1, 1),
                              "Gato Springs",
                              ["an item - key6"],
                              ["a clue - the eagle has landed6"],
                              [], # character list
                              "Gato Springs short description",
                              "Gato Springs long description")
    webster_mountain = city.District(city.DistrictId(2, 1),
                              "Webster Mountain",
                              ["an item - key7"],
                              ["a clue - the eagle has landed7"],
                              [], # character list
                              "Webster Mountain short description",
                              "Webster Mountain long description")
    lemon_field = city.District(city.DistrictId(3, 1),
                              "Lemon Field",
                              ["an item - key8"],
                              ["a clue - the eagle has landed8"],
                              [], # character list
                              "Lemon Field short description",
                              "Lemon Field long description")
    colt_wood = city.District(city.DistrictId(3, 0),
                              "Coltwood",
                              ["an item - key9"],
                              ["a clue - the eagle has landed9"],
                              [], # character list
                              "Coltwood short description",
                              "Coltwood long description")
    map_arr = [city_hall, hawkins, greenland_grove, oak_square, washington_heights, gato_springs, webster_mountain, lemon_field, colt_wood]
    # --------------------------------------------------------------------

    # print("Initializing Character Information...")
    agt_dope = characters.AgentDope(narration.short_for_agt_dope(), narration.long_for_agt_dope())
    #Dr. Crime needs to be initialized with specified PUZZLE and DIALOGS
    dr_crime = characters.DrCrime(narration.short_for_dr_crime(), narration.long_for_dr_crime(), 0, 0)


    clear()
    # For new games, play intro narration
    if ga.check_visited(STARTING_LOCATION) == False:
        intro_narration()
        clear()

    # Game loop
    while True:

        clear()

        # TODO: display game stuff
        main_menu.dotted_line(main_menu.GAME_WIDTH)
        nswe_districts = general_info(ga, map_arr)
        main_menu.dotted_line(main_menu.GAME_WIDTH)

        # get validated input
        selection = main_menu.gameplay_selection(input(">>> "), nswe_districts)
        # print("TESTING - YOU'VE SELECTED: " + selection)
        # time.sleep(2)

        # TODO: perform action based on key action noun
        # ....

        if selection == "exit":
            clear()
            confirmation = main_menu.exit_to_main_confirmation()
            if confirmation == 1:
                break
        elif selection == "inventory":
            clear()
        elif selection == "help":
            clear()
            narration.help_menu_screen()
        elif selection == "go up":
            ga.change_location(nswe_districts[0])
            ga.decrement_turns_remaining()
            clear()
        elif selection == "go down":
            ga.change_location(nswe_districts[1])
            ga.decrement_turns_remaining()
            clear()
        elif selection == "go left":
            ga.change_location(nswe_districts[2])
            ga.decrement_turns_remaining()
            clear()
        elif selection == "go right":
            ga.change_location(nswe_districts[3])
            ga.decrement_turns_remaining()
            clear()
        

# Offers user the load menu and load a game slot
def load_game(ga: gameaction.GameAction) -> (gameaction.GameAction, int):
    load_menu_choice = main_menu.load_menu()
    if (1 <= load_menu_choice <= 3):
        ga.game_state.load_game_state(load_menu_choice)
    return (ga, load_menu_choice)
