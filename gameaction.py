import json

import gamestate
from enum import Enum
from typing import List, Dict
import city
import items

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

    # Check lengendary items collected
    def check_legendary(self) -> list:
        legendary_list = [None] * 4
        legendary_list[0] = self.game_state._vision_orb
        legendary_list[1] = self.game_state._strength_orb
        legendary_list[2] = self.game_state._vitality_orb
        legendary_list[3] = self.game_state._magic_sword
        return legendary_list

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
        item_exists = False
        if item in self.game_state._current_inventory:
            item_exists = True
        return item_exists

    @property
    # Return solved puzzles in an ascending order by puzzle_id
    def solved_puzzles(self) -> Dict[int, str]:
        # return self.game_state._solved_puzzles
        return dict(sorted(self.game_state._solved_puzzles.items()))

    # Add puzzle to solved puzzle
    def add_to_solved_puzzles(self, puzzle_id: int, puzzle_name: str) -> int:
        valid_puzzle = True

        # TODO: validate puzzle_id and puzzle_name
        if (True):
            pass

        if valid_puzzle:
            self.game_state._solved_puzzles[puzzle_id] = puzzle_name
            return 0
        else:
            return 1

    # Check if puzzle is solved
    def check_for_solved_puzzle(self, puzzle_id: int) -> bool:
        solved_puzzle = False
        if int(puzzle_id) in self.game_state._solved_puzzles:
            solved_puzzle = True
        return solved_puzzle

    @property
    # Return obtained clues in an ascending order by clue_id
    def obtained_clues(self) -> Dict[int, str]:
        return dict(sorted(self.game_state._obtained_clues.items()))

    # Add clue to obtained clues
    def add_to_obtained_clues(self, clue_id: int, clue_text: str) -> int:
        valid_clue = True

        # TODO: validate clue_id and clue_text
        if (True):
            pass

        if valid_clue:
            self.game_state._obtained_clues[clue_id] = clue_text
            return 0
        else:
            return 1

    # Check if clue has been obtained
    def check_for_obtained_clue(self, clue_id: int) -> bool:
        obtained_clue = False
        if int(clue_id) in self.game_state._obtained_clues:
            obtained_clue = True
        return obtained_clue

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

if __name__ == "__main__":
    game_state = gamestate.GameState()
    game_action = GameAction(game_state)

    # game_action.check_visited("hAWKINs")
