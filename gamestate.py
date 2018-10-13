import json
from typing import List, Dict
import string
import random
from enum import Enum
import itertools


RANDOM_DISTRICT_LOWER_LIMIT = 12
RANDOM_DISTRICT_UPPER_LIMIT = 15

INITIAL_NUMBER_OF_TURNS = 80
MAX_INVENTORY = 8


# Enumerate the Districts
# https://www.notinventedhere.org/articles/python/how-to-use-strings-as-name-aliases-in-python-enums.html
_DISTRICTS = {
    1: ["City Hall", "city hall"],
    2: ["Hawkins", "hawkins"],
    3: ["Washington Heights", "washington heights"],
    4: ["Greenland Grove", "greenland grove"],
    5: ["Oak Square", "oak square"],
    6: ["Northtown", "northtown"],
    7: ["River Gardens", "river gardens"],
    8: ["Bayrock", "bayrock"],
    9: ["Sunset Hills", "sunset hills"],
    10: ["Lemonfield", "lemonfield"],
    11: ["Gato Springs", "gato springs"],
    12: ["Webster Mountain", "webster mountain"],
    13: ["Paradise Creek", "paradise creek"],
    14: ["Coltwood", "coltwood"],
    15: ["Lake Cypress", "lake cypress"],
}
District = Enum(
    value='District',
    names=itertools.chain.from_iterable(
        itertools.product(v, [k]) for k, v in _DISTRICTS.items()
    )
)


class GameState(object):

    # Initialize game state
    def __init__(self):
        # Track user status
        self._turns_remaining = INITIAL_NUMBER_OF_TURNS  # type: int
        self._current_location = "City Hall"             # type: str
        self._current_inventory = []                     # type: List[str] # or perhaps Dict[int, str] so each item has an item_id??
        self._solved_puzzles = {}                        # type: Dict[int, str]
        self._obtained_clues = {}                        # type: Dict[int, str]

        # Legendary items
        self._vision_orb =      False
        self._strength_orb =    False
        self._vitality_orb =    False
        self._magic_sword =     False

        #Track game status
        self._visited = self._initialize_visited()
        self._lair_location = self._randomly_select_lair_location()

        self._savename = ""

    # Assign to self._visited =
    #  {'City Hall': False, 'Hawkins': False, 'Washington Heights': False, 'Greenland Grove': False,
    #  'Oak Square': False, 'Northtown': False, 'River Gardens': False, 'Bayrock': False, 'Sunset Hills': False,
    #  'Lemonfield': False, 'Gato Springs': False, 'Webster Mountain': False, 'Paradise Creek': False,
    #  'Coltwood': False, 'Lake Cypress': False}
    def _initialize_visited(self) -> dict:
        visited = {}
        for district in District:
            visited[district.name] = False
        return visited

    # Assign to self._lair_location one of the following: 'Webster Mountain', 'Paradise Creek', 'Coltwood', or 'Lake Cypress'
    def _randomly_select_lair_location(self) -> str:
        return District(random.randint(RANDOM_DISTRICT_LOWER_LIMIT, RANDOM_DISTRICT_UPPER_LIMIT)).name


    # Work in progress ...

    # def load_game_state(self, json_string):
    #     json_obj = json.loads(json_string)

    # def save_game_state(self):



# if __name__ == "__main__":
#     mygame = GameState()

    # for district in District:
    #     print(district.name)

    #print(District["City Hall"].value)
    #print(District(5).name)



