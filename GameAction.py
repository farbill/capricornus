import json

import GameState


class GameAction(GameState.GameState):
    def __init__(self, game_state):
        self.game_state = game_state

    @property
    def current_location(self):
        return self.game_state.current_location

    def change_location(self, new_location):
        valid_location = True

        # TODO: validate location
        if (True):
            pass

        if valid_location:
            self.game_state.current_location = new_location
            return 0
        else:
            return 1

    @property
    def current_inventory(self):
        return self.game_state.current_inventory

    def add_to_inventory(self, new_item):
        valid_item = True

        if len(self.game_state.current_inventory) >= GameState.MAX_INVENTORY:
            valid_item = False
        elif (True):  # TODO: validate item
            pass

        if valid_item:
            self.game_state.current_inventory.append(new_item)
            return 0
        else:
            return 1

    def remove_from_inventory(self, item_to_remove):
        if item_to_remove in self.game_state.current_inventory:
            self.game_state.current_inventory.remove(item_to_remove)
            return 0
        else:
            return 1

    @property
    # Return puzzles in an ascending order
    def solved_puzzles(self):
        # return self.game_state.solved_puzzles
        return dict(sorted(self.game_state.solved_puzzles.items()))

    def add_to_solved_puzzles(self, puzzle_id, puzzle_name):
        valid_puzzle = True

        # TODO: validate puzzle_id and puzzle_name
        if (True):
            pass

        if valid_puzzle:
            self.game_state.solved_puzzles[puzzle_id] = puzzle_name
            return 0
        else:
            return 1

    @property
    # Return clues in an ascending order
    def obtained_clues(self):
        return dict(sorted(self.game_state.obtained_clues.items()))

    def add_to_obtained_clues(self, clue_id, clue_text):
        valid_clue = True

        # TODO: validate clue_id and clue_text
        if (True):
            pass

        if valid_clue:
            self.game_state.obtained_clues[clue_id] = clue_text
            return 0
        else:
            return 1


# if __name__ == "__main__":
#     game_state = GameState.GameState()
#     game_action = GameAction(game_state)
