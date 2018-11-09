import sys
from typing import Tuple, List

import city
from items import ActionType

import time
import gamestate
from main_menu import go_up_and_clear, write_over, informScreen

#checks if the city has the target item
def checkForItem(districtItems, itemsInCityList, targetItem):
    for i in range(len(districtItems)):
        if itemsInCityList[i].name == targetItem:
            itemsInCityList[i] = None

#creats list of items in the district then calss checkForItem function
def itemCheck(this_district, item):
    itemsInCityList = this_district._district_items
    checkForItem(this_district._district_items, itemsInCityList, item.name)

def gameplay_selection(ga, the_input: str,
                       nswe_districts: List[str],
                       district_exits: List[str],
                       this_district: city.District) -> str:

    screen_refresh = False

    # Change nswe_districts to lower case
    # e.g. ['hawkins', None, 'greenland grove', 'oak square']
    nswe_districts = list(map(lambda x: x.lower() if x is not None else x, nswe_districts))

    # Change district_exits to lower case
    # e.g. ['dayton dr', '', 'summer ln', 'shore blvd']
    district_exits = list(map(lambda x: x.lower() if x is not None else x, district_exits))

    # 2D general action array
    #   1st element of each 1D action list is the key action noun
    general_action_array = [
        ["exit", "quit", "q", "exit game", "quit game", "bye", "byebye", "main", "main menu"],
        ["inventory", "bag", "open inventory", "open bag", "see inventory", "check inventory"],
        ["help", "help me", "manual", "guide", "q&a", "open help"],
        ["savegame", "save game", "save"],
        ["loadgame", "load game", "load"]
        # ....
    ]

    # 2D NSWE movement array
    #   1st element of each 1D action list is the key action noun
    nswe_actions = [    ["go up", "go north", "go to north", "north", "up"],
                        ["go down", "go south", "go to south", "south", "down"],
                        ["go left", "go west", "go to west", "west", "left"],
                        ["go right", "go east", "go to east", "east", "right"]      ]

    # Add additional word parsing for each NSEW movement based on district name
    for i in range(4):
        if nswe_districts[i] is not None:
            arr = nswe_actions[i]
            whole_name = nswe_districts[i]                  # ex: 'greenland grove'
            first_word = whole_name.split()[0]              # ex: 'greenland'
            arr.append(whole_name)                          # ex: greenland grove
            arr.append(first_word)                          # ex: greenland
            arr.append("go " + whole_name)                  # ex: go greenland grove
            arr.append("go to " + whole_name)               # ex: go to greenland grove
            arr.append("go " + first_word)                  # ex: go greenland
            arr.append("go to " + first_word)               # ex: go to greenland
            arr.append("travel " + whole_name)              # ex: travel greenland grove
            arr.append("travel to " + whole_name)           # ex: travel to greenland grove
            arr.append("travel " + first_word)              # ex: travel greenland
            arr.append("travel to " + first_word)           # ex: travel to greenland

            if district_exits[i] != "":
                whole_exit_name = district_exits[i]             # ex: 'shore blvd'
                first_exit_word = whole_exit_name.split()[0]    # ex: 'shore'
                arr.append(whole_exit_name)                     # ex: shore blvd
                arr.append(first_exit_word)                     # ex: shore
                arr.append("go " + whole_exit_name)             # ex: go shore blvd
                arr.append("go to " + whole_exit_name)          # ex: go to shore blvd
                arr.append("go " + first_exit_word)             # ex: go shore
                arr.append("go to " + first_exit_word)          # ex: go to shore
                arr.append("travel " + whole_exit_name)              # ex: travel shore blvd
                arr.append("travel on " + whole_exit_name)           # ex: travel on shore blvd
                arr.append("travel " + first_exit_word)              # ex: travel shore
                arr.append("travel on " + first_exit_word)           # ex: travel on shore

            general_action_array.append(arr)

    # Build district_items_action array for items in district
    district_items_action = []
    for item in this_district._district_items:
        if item:
            for action in item.action:
                for commands in action.commands:
                    district_items_action.append(commands)

    # Build district_characters_action array for characters in district
    district_characters_action = []
    for character in this_district._characters:
        for action in character._action:
            for commands in action.commands:
                district_characters_action.append(commands)

    #Build user_items_action array for items in user's inventory
    user_items_action = []
    for item in ga.current_inventory:
        for action in item.action:
            for commands in action.commands:
                user_items_action.append(commands)


    selection = None
    the_input = str(the_input).lower()  # to make the input case insensitive

    while selection == None:

        # Check for valid action in general action array
        for action_list in general_action_array:
            if the_input in action_list:
                selection = action_list[0]
                break

        # Check for district-specific action, items
        if the_input in district_items_action:
            for item in this_district._district_items:
                for action in item.action:
                    if the_input in action.commands:
                        if action.response_type == ActionType.DISPLAY:
                            sys.stdout.write("\033[K")  # clear line
                            print(action.response)
                            screen_refresh = False
                        if action.response_type == ActionType.ACTION:
                            if action.more_response_type == ActionType.TAKE_LEGENDARY:
                                if(len(ga.game_state._current_inventory) < gamestate.MAX_INVENTORY):
                                    sys.stdout.write("\033[K")  # clear line
                                    ga.add_to_inventory(item)
                                    informScreen(action.response)
                                    if item.name == "Vision Orb":
                                        ga.game_state._vision_orb = True
                                        itemCheck(this_district, item)
                                    elif item.name == "Magic Sword":
                                        ga.game_state._magic_sword = True
                                        itemCheck(this_district, item)
                                    elif item.name == "Strength Orb":
                                        ga.game_state._strength_orb = True
                                        itemCheck(this_district, item)
                                    elif item.name == "Vitality Orb":
                                        ga.game_state._vitality_orb = True
                                        itemCheck(this_district, item)
                                    screen_refresh = True
                                else:
                                    print("You can't carry anymore.  Max inventory is %s."%gamestate.MAX_INVENTORY)
                                    sys.stdout.write("\033[K")  # clear line
                            elif action.more_response_type == ActionType.TAKE_ITEM:
                                if(len(ga.game_state._current_inventory) < gamestate.MAX_INVENTORY):
                                    item_remains = True
                                    sys.stdout.write("\033[K")  # clear line
                                    
                                    if (item.name == "Time Stone"):
                                        ga.game_state._turns_remaining = ga.game_state._turns_remaining + 5
                                    elif (item.name == "Magic Mushroom"):
                                        ga.game_state._turns_remaining = ga.game_state._turns_remaining - 10
                                        item_remains = False
                                    elif (item.name == "Lotto Ticket"):
                                        ga.add_to_obtained_clues(2, "The lotto ticket had '23 57 12' on it")
                                    
                                    if (item_remains == True):
                                        ga.add_to_inventory(item)
                                    informScreen(action.response)
                                    screen_refresh = True
                                    itemsInCityList = this_district._district_items
                                    checkForItem(this_district._district_items, itemsInCityList, item.name)
                                else:
                                    print("You can't carry anymore.  Max inventory is %s."%gamestate.MAX_INVENTORY)
                                    sys.stdout.write("\033[K")  # clear line
                if screen_refresh == True:
                    break
            if screen_refresh == True:
                break

            sys.stdout.write("\033[F")      # go up one line
            go_up_and_clear()
            the_input = str(input(">>> ")).lower()
            continue

        # Check for district-specific action, characters
        if the_input in district_characters_action:
            for character in this_district._characters:
                for action in character._action:
                    if the_input in action.commands:
                        if action.response_type == ActionType.DISPLAY:
                            sys.stdout.write("\033[K")  # clear line
                            print(action.response)
                        if action.response_type == ActionType.EVENT:
                            character.play_char_puzzle(ga)
                            if(character._short_description == "Daniel Webster Jr. Jr."):
                                ga.add_to_obtained_clues(1, "These cities are on the same horizon. Bay Rock - Greenland - City Hall - Oak Square - Northtown")
                            return ""
            sys.stdout.write("\033[F")      # go up one line
            go_up_and_clear()
            the_input = str(input(">>> ")).lower()
            continue

        # Check for user's item action
        if the_input in user_items_action:
            for item in ga.current_inventory:
                for action in item.action:
                    if the_input in action.commands:

                        # Only respond to userItem-to-districtItem interactions
                        if action.response_type == ActionType.TRIGGER:
                            target_item_to_interact_with = action.response.lower()

                            # search for target_item in district
                            itemInDistrict = None
                            for d_item in this_district._district_items:
                                if d_item.name.lower() == target_item_to_interact_with:
                                    itemInDistrict = d_item
                                    break

                            if itemInDistrict:
                                # TODO: All control flows for possible item interactions here
                                if itemInDistrict.name.lower() == "red chest":
                                    informScreen("You've opened the Red Chest.")
                                    if ga.space_in_inventory():
                                        # informScreen()
                                        itemInDistrict.description = "An opened Red Chest."
                                    else:
                                        informScreen("You don't have enough space in your inventory to acquire the item in it.")


                                # TODO: more here ...
                                return
                            else:
                                sys.stdout.write("\033[K")  # clear line
                                print(target_item_to_interact_with.title() + " cannot be found.")
                        else:
                            sys.stdout.write("\033[K")  # clear line
                            print("Use inventory menu to directly interact with items in your possession.")
            sys.stdout.write("\033[F")      # go up one line
            go_up_and_clear()
            the_input = str(input(">>> ")).lower()
            continue


        # Else, bad action
        if screen_refresh == True:
            screen_refresh = False
            continue
        else:
            if selection == None:
                if len(the_input) > 99:
                    sys.stdout.write("\033[K")  # clear line
                    write_over("Your input is too long.")
                sys.stdout.write("\033[K")  # clear line
                write_over("Invalid Input.  Try again.")
                go_up_and_clear()
                the_input = str(input(">>> ")).lower()

    return selection
