import sys
import time

import main_menu
from command_parsing import command_parsing
from main_menu import clear_screen, go_up_and_clear, informScreen, write_over
from narration import standard_title_display, inventory_open, narration

def clues_screen(ga):
    clear_screen()
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    if (len(ga.obtained_clues) == 0):
        nothing_string = "There are no clues obtained."
        narration(nothing_string, main_menu.GAME_WIDTH)
    else:
        narration_clues = "These are following clues obtained:"
        narration(narration_clues, main_menu.GAME_WIDTH)
        main_menu.empty_line(2)
        for clue in ga.obtained_clues:
            clueString = "- " + clue
            narration(clueString, main_menu.GAME_WIDTH)

    main_menu.empty_line(2)
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    input("Press [Enter] to continue...")


def print_inventory_item(ga):
    clear_screen()
    main_menu.dotted_line(main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    if len(ga.current_inventory) == 0:
        narration("There are no items obtained.", main_menu.GAME_WIDTH)
    else:
        narration("These are following items obtained:", main_menu.GAME_WIDTH)
        narration("(Type 'view' or 'drop' followed by the item name to see its description or drop it from the inventory, or 'back' to go back.)", main_menu.GAME_WIDTH)
        main_menu.empty_line(2)
        for item in ga.current_inventory:
            narration("- " + item.name, main_menu.GAME_WIDTH)
    main_menu.empty_line(2)
    main_menu.dotted_line(main_menu.GAME_WIDTH)

def cline_print_up_cline(msg: str):
    sys.stdout.write("\033[K")  # clear line
    write_over(msg)
    go_up_and_clear()

def view_drop_inventory_item(ga, map_arr, this_district):
    while True:
        print_inventory_item(ga)

        if len(ga.current_inventory) == 0:
            input("Press [Enter] to continue...")
            return

        while True:
            selection = input(">>> ").lower()
            if selection in ["exit", "return", "back", "resume", "resume game", "go back", "q", "quit"]:
                return
            elif len(selection.split(" ", 1)) >= 2:
                parsed_selection = selection.split(" ", 1)
                action_word = parsed_selection[0]
                item_name = parsed_selection[1]

                retrieved_item = ga.get_item_from_inventory_by_name(item_name)

                if action_word == "view":
                    if retrieved_item is not None:
                        informScreen(retrieved_item.description)
                        break
                    else:
                        cline_print_up_cline("That item is not in your inventory.")

                elif action_word == "drop":
                    if retrieved_item is not None:
                        ga.remove_item_from_inventory(retrieved_item)
                        this_district._dropped_items.append(retrieved_item)
                        informScreen(retrieved_item.name + " has been dropped from your inventory.")
                        break
                    else:
                        cline_print_up_cline("That item is not in your inventory.")

                else:
                    cline_print_up_cline("Invalid Input. Try again.")
            else:
                cline_print_up_cline("Invalid Input. Try again.")


def inventory_menu_screen(ga, map_arr, this_district):
    while True:
        clear_screen()
        standard_title_display("Inventory")
        inventory_open(main_menu.GAME_WIDTH)
        main_menu.empty_line(2)
        main_menu.dotted_line(main_menu.GAME_WIDTH)

        list_clues = ["1", "clue", "clues", "gameclue", "hints", "hint", "1. clues"]
        list_items = ["2", "item", "items", "about items", "2. items"]
        list_back = ["3", "exit", "return", "back", "resume", "resume game", "3. resume game", "q", "quit"]

        while True:
            selection = input(">>> ").lower()

            if command_parsing(selection, list_clues):  # Clues
                clues_screen(ga)
                break
            if command_parsing(selection, list_items):  # Items
                view_drop_inventory_item(ga, map_arr, this_district)
                break
            if command_parsing(selection, list_back):   # Back to the game
                return

            cline_print_up_cline("Invalid Input. Try again.")
