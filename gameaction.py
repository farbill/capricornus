import json

import gamestate
from enum import Enum
from typing import List, Dict
import city
import items
import time
from main_menu import GAME_WIDTH, dotted_line, empty_line, print_in_the_middle, print_left_indented, write_over, \
    go_up_and_clear, yes_no_selection, clear_screen, informScreen
from narration import narration, left_narration
import puzzles

class GameAction(gamestate.GameState):
    def __init__(self, game_state: gamestate.GameState):
        self.game_state = game_state

    @property
    # Get map_arr
    def map_arr(self) -> [city.District]:
        return self.game_state._map_arr

    # Set map_arr
    def set_map_arr(self, map_arr: [city.District]):
        self.game_state._map_arr = map_arr

    @property
    # Return turns remaining
    def turns_remaining(self) -> int:
        return self.game_state._turns_remaining

    # Decrement turns remaining
    def decrement_turns_remaining(self) -> None:
        self.game_state._turns_remaining -= 1

    @property
    # Return current location
    def current_location(self) -> str:
        return self.game_state._current_location

    # Check if lair has been discovered
    def lair_discovered(self) -> bool:
        return self.game_state._current_location == self.game_state._lair_location and self.game_state._vision_orb == True

    # Change location
    def change_location(self, new_location: str) -> int:
        valid_location = False

        new_location = new_location.lower()
        if new_location in gamestate.District.__members__:
            valid_location = True

        if valid_location:
            self.game_state._current_location = gamestate.District[new_location].name
            return 0
        else:
            return 1

    # Check legendary items collected
    def check_legendary(self) -> [str]:

        legendary_status = [None] * 4

        legend_list = [ (self.game_state._vision_orb, "Vision Orb"),
                        (self.game_state._strength_orb, "Strength Orb"),
                        (self.game_state._vitality_orb, "Vitality Orb"),
                        (self.game_state._magic_sword, "Magic Sword")       ]

        for i in range(len(legend_list)):
            if legend_list[i][0]:
                if self.check_inventory_by_name(legend_list[i][1]):
                    legendary_status[i] =   "On Hand"
                else:
                    legendary_status[i] =   "Found  "
            else:
                legendary_status[i] =       "Unknown"

        return legendary_status

    @property
    # Return inventory
    def current_inventory(self) -> List[items.Item]:
        return self.game_state._current_inventory

    # Check if there's space in inventory
    def space_in_inventory(self) -> bool:
        return len(self.current_inventory) < gamestate.MAX_INVENTORY

    # Add item to inventory
    def add_to_inventory(self, new_item: items.Item) -> int:
        valid_item = True

        if len(self.game_state._current_inventory) >= gamestate.MAX_INVENTORY:
            valid_item = False
        elif (True):  # TODO: validate item
            pass

        if valid_item:
            self.game_state._current_inventory.append(new_item)
            return 0
        else:
            return 1

    # Remove item from inventory
    def remove_from_inventory(self, item_to_remove: items.Item) -> int:
        if item_to_remove in self.game_state._current_inventory:
            self.game_state._current_inventory.remove(item_to_remove)
            return 0
        else:
            return 1

    # Check if item exists in inventory
    def check_inventory(self, item: items.Item) -> bool:
        if item in self.game_state._current_inventory:
            return True
        return False

    # Check if item exists in inventory by name
    def check_inventory_by_name(self, item_name: str) -> bool:
        for i in range(len(self.game_state._current_inventory)):
            if item_name == self.game_state._current_inventory[i].name:
                return True
        return False

    # Get item from inventory by name
    def get_item_from_inventory_by_name(self, item_name: str) -> items.Item:
        for item in self.game_state._current_inventory:
            if item.name.lower() == item_name.lower():
                return item

    # Remove item from inventory
    def remove_item_from_inventory(self, item: items.Item):
        self.game_state._current_inventory.remove(item)

    # Remove item from inventory by name
    def remove_item_from_inventory_by_name(self, item_name: str):
        item_index = None
        for i in range(len(self.game_state._current_inventory)):
            if self.game_state._current_inventory[i].name.lower() == item_name.lower():
                item_index = i
                break
        del self.game_state._current_inventory[item_index]


    # Get item from uncollected_legendary_items array by name
    def get_item_from_uncollected_legendary_items(self, item_name: str) -> items.Item:
        for item in self.game_state.uncollected_legendary_items:
            if item.name == item_name:
                return item

    # Remove item from uncollected_legendary_items array by name
    def remove_item_from_uncollected_legendary_items(self, item_name: str):
        item_index = None
        for i in range(len(self.game_state.uncollected_legendary_items)):
            if self.game_state.uncollected_legendary_items[i].name == item_name:
                item_index = i
                break
        del self.game_state.uncollected_legendary_items[item_index]

    # @property
    # # Return solved puzzles in an ascending order by puzzle_id
    # def solved_puzzles(self) -> Dict[int, str]:
    #     # return self.game_state._solved_puzzles
    #     return dict(sorted(self.game_state._solved_puzzles.items()))

    # # Add puzzle to solved puzzle
    # def add_to_solved_puzzles(self, puzzle_id: int, puzzle_name: str) -> int:
    #     valid_puzzle = True
    #
    #     # TODO: validate puzzle_id and puzzle_name
    #     if (True):
    #         pass
    #
    #     if valid_puzzle:
    #         self.game_state._solved_puzzles[puzzle_id] = puzzle_name
    #         return 0
    #     else:
    #         return 1
    #
    # # Check if puzzle is solved
    # def check_for_solved_puzzle(self, puzzle_id: int) -> bool:
    #     solved_puzzle = False
    #     if int(puzzle_id) in self.game_state._solved_puzzles:
    #         solved_puzzle = True
    #     return solved_puzzle

    @property
    # Return obtained clues in an ascending order by clue_id
    def obtained_clues(self) -> [str]:
        return self.game_state._obtained_clues

    # Add clue to obtained clues
    def add_to_obtained_clues(self, clue_text: str):
        self.game_state._obtained_clues.append(clue_text)

    # # Check if clue has been obtained
    # def check_for_obtained_clue(self, clue_id: int) -> bool:
    #     obtained_clue = False
    #     if int(clue_id) in self.game_state._obtained_clues:
    #         obtained_clue = True
    #     return obtained_clue

    # Check if district has been visited
    def check_visited(self, district_name: str) -> bool:
        district_name = district_name.lower()

        if district_name in gamestate.District.__members__:
            proper_name = gamestate.District[district_name].name

            return self.game_state._visited[proper_name]
        else:
            raise ValueError("A bad district_name was supplied.")

    # Change district to visited
    def change_visited(self, district_name: str) -> int:
        district_name = district_name.lower()
        if district_name in gamestate.District.__members__:
            proper_name = gamestate.District[district_name].name
            self.game_state._visited[proper_name] = True
            return 0
        else:
            return 1

    def enter_lair_confirmation(self) -> int:
        msg1 = "Are you sure you want to continue into the Lair?"
        msg2 = "Once you've entered, there's no going back!"

        clear_screen()
        dotted_line(GAME_WIDTH)
        empty_line(1)
        print_in_the_middle(GAME_WIDTH, msg1)
        print_in_the_middle(GAME_WIDTH, msg2)
        empty_line(1)
        dotted_line(GAME_WIDTH)

        selection = yes_no_selection(input("Yes/No >>> "))
        return selection

    def narration_screen(self, narr):
        clear_screen()
        dotted_line(GAME_WIDTH)
        empty_line(2)
        narration(narr, GAME_WIDTH)
        empty_line(2)
        dotted_line(GAME_WIDTH)
        input("Press [Enter] to continue...")
        clear_screen()

    # Dr. Crime's lair final game sequence
    def final_game_sequence(self) -> str:
        number_of_tries = 8
        story1 = "You've entered the lair and encountered Dr. Crime. There are " + str(len(self.game_state.boss_puzzles))+ " puzzles " \
                    "you must solve. You must answer all puzzles correctly in order to defeat Dr. Crime and win the game. " \
                    "And you are only be allowed " + str(number_of_tries) + " wrong answer tries."
        wrong_narr = "Dr. Crime says, 'You are foolish to think you can outsmart me.'"

        right1 = "Dr. Crime says, 'That was a lucky guess. Let's see how you do on this next one.'"
        right2 = "Dr. Crime says, 'Well, you're smarter than you look. Fine, you won't be able to solve this next one.'"
        right3 = "Dr. Crime says, 'Arghhhh, who do you think you are?! You most definitely will not get this next one.'"
        right4 = "As you raise up your Magic Sword, Dr. Crime's eyes glisten with fear. You quickly drop the sword, letting" \
                 " the weight cut Dr. Crime. You rest easy knowing Dr. Crime can no longer poison the city."


        # Check all legendary items are in user's inventory to allow user to proceed
        legendary_items_status = self.check_legendary()
        for status in legendary_items_status:
            if status != "On Hand":
                informScreen("You need all 4 Legendary items in your inventory to proceed!")
                return ""

        # Check if user wishes to proceed
        if self.enter_lair_confirmation() == 2: # User chooses 'no'
            return ""

        # working here......
        self.narration_screen(story1)
        status, number_of_tries = self.game_state.boss_puzzles[0].play_boss_puzzle(number_of_tries)
        if status == False:
            self.narration_screen(wrong_narr)
            return "losegame"

        self.narration_screen(right1)
        status, number_of_tries = self.game_state.boss_puzzles[1].play_boss_puzzle(number_of_tries)
        if status == False:
            self.narration_screen(wrong_narr)
            return "losegame"

        self.narration_screen(right2)
        status, number_of_tries = self.game_state.boss_puzzles[2].play_boss_puzzle(number_of_tries)
        if status == False:
            self.narration_screen(wrong_narr)
            return "losegame"

        self.narration_screen(right3)
        status, number_of_tries = self.game_state.boss_puzzles[3].play_boss_puzzle(number_of_tries)
        if status == False:
            self.narration_screen(wrong_narr)
            return "losegame"

        self.narration_screen(right4)
        return "wingame"

if __name__ == "__main__":
    game_state = gamestate.GameState()
    game_action = GameAction(game_state)

    # game_action.check_visited("hAWKINs")
