import sys

import main_menu
from command_parsing import command_parsing
from main_menu import clear_screen


def command_help(width):
        main_menu.print_in_the_middle(width, ("------ Examples of Available Commands -------- "))
        print()
        main_menu.print_in_the_middle(width, ("1. Go to North, South, East, or West           "))
        main_menu.print_in_the_middle(width, ("2. Interact with items or characters           "))
        main_menu.print_in_the_middle(width, ("   Examples:                                   "))
        main_menu.print_in_the_middle(width, ("        \"talk to hobo\"                       "))
        main_menu.print_in_the_middle(width, ("        \"look at red chest\"                  "))
        main_menu.print_in_the_middle(width, ("        \"pick up coin\"                       "))
        main_menu.print_in_the_middle(width, ("          And MANY more!                       "))
        main_menu.print_in_the_middle(width, ("3. Inventory                                   "))
        main_menu.print_in_the_middle(width, ("   i.   Clues: Check collected clues           "))
        main_menu.print_in_the_middle(width, ("   ii.  Items: View/drop all obtained items    "))
        main_menu.print_in_the_middle(width, ("4. Help                                        "))
        main_menu.print_in_the_middle(width, ("5. Savegame                                    "))
        main_menu.print_in_the_middle(width, ("6. Loadgame                                    "))

def inventory_open(width):
        main_menu.print_in_the_middle(width, "1. Clues       ")
        main_menu.print_in_the_middle(width, "2. Items       ")
        main_menu.print_in_the_middle(width, "3. Resume Game ")


def help_menu():
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, "Type \"Help\" for game commands")

def start_narration1():
	title_narration_part1 = \
                  "You are Agent Dope, who is tasked with the mission of finding and apprehending " \
                  "Dr. Crime - a once renowned scientist from the affluent Crime family, " \
                  "known for their charity and philanthropy. After spending nearly a decade " \
                  "working on the theory of Dark Magic to restore Life, Dr. Crime’s work was " \
                  "met with great criticism and disapproval from the scientific community, and " \
                  "was ridiculed for such preposterous ideas. Dr. Crime went down a terrible " \
                  "spiral and started to use Dark Magic for mischief and evil. He vowed to " \
                  "take vengeance on the citizens of the city of New San Diego by using Dark " \
                  "Magic to poison the city and kill all of its citizens. "
	
	return title_narration_part1
	
	
def start_narration2():
	title_narration_part2 = "The latest reconnaissance shows that Dr. Crime has established a lair " \
                    "which is protected by a Magical Barrier, which can only be destroyed by " \
                    "an individual who possess the Magical Orbs. The reconnaissance also revealed " \
                    "that Dr. Crime is clothed in a Magical Armor that can be only penetrated by " \
                    "the Magic Sword of Light. With none of these in hand, the cautious, yet " \
                    "courageous Agt. Dope must explore the city of New San Diego, find all the " \
                    "necessary artifacts, and use them to stop Dr. Crime before the poison is " \
                    "released. Hurry, time is ticking!"
	
	return title_narration_part2


def short_for_agt_dope():
	text = "An elite secret agent who's after Dr. Crime" 
	
	return text
	
	
def long_for_agt_dope():
	text  = "An elite secret agent who is an expert in forensic and many other scientific " \
                     "principles with multiple years of training MMA."
	
	return text
	
	
def short_for_dr_crime():
	text  = "An evil scientist who was once renowned scientist from the affluent Crime family, " \
                   "known for their charity and philanthropy."
	
	return text
	
	
def long_for_dr_crime():
	text  = "An evil scientist who was once renowned scientist from the affluent Crime family, " \
                   "known for their charity and philanthropy, who spent nearly a decade " \
                   "working on the theory of Dark Magic to restore Life." 
	
	return text


def narration(the_string, line_length):
    counter = 0

    to_print = " " * int(line_length / 8)
    last_line_indicator = 0

    for i in the_string:
        to_print += i
        counter += 1
        last_line_indicator += 1

        if counter > (int(line_length * 5 / 8)):
            if i != " ":
                continue
            print(to_print)
            counter = 0
            to_print = " " * int(line_length / 8)

    if last_line_indicator <= len(the_string):
        print(to_print)


def left_narration(the_string, line_length):
    counter = 0

    to_print = ""
    last_line_indicator = 0

    for i in the_string:
        to_print += i
        counter += 1
        last_line_indicator += 1

        if counter > (int(line_length * 2/3)):
            if i != " ":
                continue
            print(to_print)
            counter = 0
            to_print = ""

    if last_line_indicator <= len(the_string):
        print(to_print)

def mainCharNarration(agtD, drC):
    clear_screen()
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    narration("Agent Dope", main_menu.GAME_WIDTH)
    main_menu.empty_line(1)
    narration(agtD, main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("Press [Enter] to continue...")
    clear_screen()
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    narration("Dr. Crime", main_menu.GAME_WIDTH)
    main_menu.empty_line(1)
    narration(drC, main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("Press [Enter] to continue...")
    #
    # clear_screen()
    # main_menu.dotted_line(main_menu.GAME_WIDTH)
    # main_menu.empty_line(2)
    # narration("Hobo: A hobo, a very regular hobo at that.", main_menu.GAME_WIDTH)
    # main_menu.empty_line(1)
    # narration("Business man: literally, a businessman", main_menu.GAME_WIDTH)
    # main_menu.empty_line(1)
    # narration("Daneil Webers Jr. Jr.: Daniel's Webster's grandson", main_menu.GAME_WIDTH)
    # main_menu.empty_line(1)
    # narration("Skateboarder: card carrying thrasher subscription holder.", main_menu.GAME_WIDTH)
    # main_menu.empty_line(1)
    # narration("Wizard: a wizard who can cast magics", main_menu.GAME_WIDTH)
    # main_menu.empty_line(1)
    # narration("Student: literally, a student standing around", main_menu.GAME_WIDTH)
    # main_menu.empty_line(2)
    # main_menu.dotted_line(main_menu.GAME_WIDTH)
    # input("Press [Enter] to continue...")
    clear_screen()
    
def gameNarrationHelp(narr1, narr2):
    clear_screen()
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    narration(narr1, main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("Press [Enter] to continue...")
    clear_screen()
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    narration(narr2, main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("Press [Enter] to continue...")
    clear_screen()
    
def itemHelp():
    itemString = "There are regular items and legendary items. " \
                    "Both can be picked up and dropped. But "\
                    "Legendary items are imperative in order to defeat Dr.Crime." \
                    "Obtaining certain items can add a clue.  Clue remains " \
                    "even if the item is dropped, because it's considered " \
                    "an intellectual property."
    clear_screen()
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    narration(itemString, main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("Press [Enter] to continue...")
    clear_screen()
        
def help_menu_screen():
    back_to_game = False
    while back_to_game == False:
        standard_title_display("Help")
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, ("1. Game Story   "))
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, ("2. Characters   "))
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, ("3. Game Commands"))
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, ("4. Items        "))
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, ("5. Resume Game  "))
        main_menu.empty_line(3)
        main_menu.dotted_line(main_menu.GAME_WIDTH)

        list_game_story = ["1", "game story", "story", "about game", "1. game story"]
        list_characters = ["2", "character", "characters", "char", "chars", "game characters", "2. characters"]
        list_game_commands = ["3", "game commands", "game command", "commands", "command", "3. game commands"]
        list_items = ["4", "item", "items", "about items", "4. items"]
        list_back = ["5", "exit", "return", "back", "resume", "resume game", "5. resume game"]

        selection = input(">>> ")

        while True:
            if command_parsing(selection, list_game_story) == 1: #Help for game story
                gameNarrationHelp(start_narration1(), start_narration2())
                break
            if command_parsing(selection, list_characters) == 1: #Help for game characters
                mainCharNarration(long_for_agt_dope(), long_for_dr_crime())
                break
            if command_parsing(selection, list_game_commands) == 1: #Help for game commands
                clear_screen()
                main_menu.dotted_line(main_menu.GAME_WIDTH)
                main_menu.empty_line(2)
                command_help(main_menu.GAME_WIDTH)
                main_menu.empty_line(2)
                main_menu.dotted_line(main_menu.GAME_WIDTH)
                input("Press [Enter] to continue...")
                clear_screen()
                break
            if command_parsing(selection, list_items) == 1:         #Help for game items
                itemHelp()
                break
            if command_parsing(selection, list_back) == 1:          #Back to the game
                clear_screen()
                back_to_game = True
                break
            main_menu.write_over("Invalid Input.  Try again.")
            sys.stdout.write("\033[F")      # go up one line
            sys.stdout.write("\033[K")      # clear line
            selection = str(input(">>> ")).lower()


def standard_title_display(string):
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    main_menu.print_in_the_middle(main_menu.GAME_WIDTH, (string))
    main_menu.empty_line(2)

def narrationScreen(msg: str):
    clear_screen()
    dotted_line_length = main_menu.GAME_WIDTH
    main_menu.dotted_line(dotted_line_length)
    main_menu.empty_line(1)
    narration(msg, main_menu.GAME_WIDTH)
    main_menu.empty_line(1)
    main_menu.dotted_line(dotted_line_length)
    input("Press [Enter] to continue...")
