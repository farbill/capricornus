import json
from typing import List, Dict

INITIAL_NUMBER_OF_TURNS = 80
MAX_INVENTORY = 8


class GameState(object):
    # Initialize game state
    def __init__(self):
        self._turns_remaining = INITIAL_NUMBER_OF_TURNS  # type: int
        self._current_location = "city_hall"             # type: str
        self._current_inventory = []                     # type: List[str]
        self._solved_puzzles = {}                        # type: Dict[int, str]
        self._obtained_clues = {}                        # type: Dict[int, str]

        # Legendary items
        self._vision_orb = False                         # type: bool
        self._strength_orb = False                       # type: bool
        self._vitality_orb = False                       # type: bool
        self._magic_sword = False                        # type: bool

    # Work in progress ...
    # def load_game_state(self, json_string):
    #     json_obj = json.loads(json_string)

# if __name__ == "__main__":
#     mygame = GameState()
#     print(mygame._current_location)

