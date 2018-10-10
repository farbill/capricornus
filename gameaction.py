import json

import gamestate
from typing import List, Dict


class GameAction(gamestate.GameState):
    def __init__(self, game_state: gamestate.GameState):
        self.game_state = game_state

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
        valid_location = True

        # TODO: validate location
        if (True):
            pass

        if valid_location:
            self.game_state._current_location = new_location
            return 0
        else:
            return 1

    @property
    # Return inventory
    def current_inventory(self) -> List[str]:
        return self.game_state._current_inventory

    # Add item to inventory
    def add_to_inventory(self, new_item: str) -> int:
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
    def remove_from_inventory(self, item_to_remove: str) -> int:
        if item_to_remove in self.game_state._current_inventory:
            self.game_state._current_inventory.remove(item_to_remove)
            return 0
        else:
            return 1

    # Check if item exists in inventory
    def check_inventory(self, item) -> bool:
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

# if __name__ == "__main__":
#     game_state = GameState.GameState()
#     game_action = GameAction(game_state)
