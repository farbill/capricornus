import json

import gamestate
from typing import List, Dict


class GameAction(gamestate.GameState):
    def __init__(self, game_state: gamestate.GameState):
        self.game_state = game_state

    @property
    def current_location(self) -> str:
        return self.game_state._current_location

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
    def current_inventory(self) -> List[str]:
        return self.game_state._current_inventory

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

    def remove_from_inventory(self, item_to_remove: str) -> int:
        if item_to_remove in self.game_state._current_inventory:
            self.game_state._current_inventory.remove(item_to_remove)
            return 0
        else:
            return 1

    @property
    # Return puzzles in an ascending order
    def solved_puzzles(self) -> Dict[int, str]:
        # return self.game_state._solved_puzzles
        return dict(sorted(self.game_state._solved_puzzles.items()))

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

    @property
    # Return clues in an ascending order
    def obtained_clues(self) -> Dict[int, str]:
        return dict(sorted(self.game_state._obtained_clues.items()))

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


# if __name__ == "__main__":
#     game_state = GameState.GameState()
#     game_action = GameAction(game_state)
