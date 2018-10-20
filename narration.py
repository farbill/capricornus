import main_menu

def possible_menu():
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, "Possible Commands:                   ")
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, "- Go North, South, West, or East    ")
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, "- Open Inventory                    ")
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, "- Interact with the district feature")
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, "- Exit to the main menu             ")
        main_menu.print_in_the_middle(main_menu.GAME_WIDTH, "- Help                              ")

def start_narration1():
	title_narration_part1 = "Agent Dope, who is tasked with the mission of finding and appending " \
                  "Dr. Crime – a once renowned scientist from the affluent Crime family, " \
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

