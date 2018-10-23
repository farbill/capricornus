import json
from typing import List, Dict
import string
import random
from enum import Enum
import itertools
import sys
import os


RANDOM_DISTRICT_LOWER_LIMIT = 12
RANDOM_DISTRICT_UPPER_LIMIT = 15

INITIAL_NUMBER_OF_TURNS = 80
MAX_INVENTORY = 8


# Enumerate the Districts
# https://www.notinventedhere.org/articles/python/how-to-use-strings-as-name-aliases-in-python-enums.html
_DISTRICTS = {
    1: ["City Hall", "city hall", "city_hall", "cityhall"],
    2: ["Hawkins", "hawkins"],
    3: ["Washington Heights", "washington heights", "washington_heights", "washingtonheights"],
    4: ["Greenland Grove", "greenland grove", "greenland_grove", "greenlandgrove"],
    5: ["Oak Square", "oak square", "oak_square", "oaksquare"],
    6: ["Northtown", "northtown"],
    7: ["River Gardens", "river gardens", "river_gardens", "rivergardens"],
    8: ["Bayrock", "bayrock"],
    9: ["Sunset Hills", "sunset hills", "sunset_hills", "sunsethills"],
    10: ["Lemon Field", "lemon field"],
    11: ["Gato Springs", "gato springs", "gato_springs", "gatosprings"],
    12: ["Webster Mountain", "webster mountain", "webster_mountain", "webstermountain"],
    13: ["Paradise Creek", "paradise creek" ,"paradise_creek", "paradisecreek"],
    14: ["Coltwood", "coltwood"],
    15: ["Lake Cypress", "lake cypress", "lake_cypress", "lakecypress"],
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


    # Save game state - takes save slot as input (1, 2, 3)
    def save_game_state(self, save_slot: int) -> int:
        if save_slot < 1 or save_slot > 3:
            return 1

        # Build save path
        dirname = os.path.join(os.path.realpath('.'), "savedgames")
        filename = "savedgame_" + str(save_slot)
        fullpath = os.path.join(dirname, filename)

        # Check savedgame folder exists, if not, make it
        try:
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        except OSError:
            return 2

        try:
            with open(fullpath, 'w') as outputfile:
                json.dump(self.__dict__, outputfile)
        except IOError:
            return 2
        return 0

    # Load game state - takes load slot as input (1, 2, 3)
    def load_game_state(self, load_slot: int) -> int:
        if load_slot < 1 or load_slot > 3:
            return 1

        # Build load path
        dirname = os.path.join(os.path.realpath('.'), "savedgames")
        filename = "savedgame_" + str(load_slot)
        fullpath = os.path.join(dirname, filename)

        # Check savedgame folder exists,
        if not os.path.exists(dirname):
            return 2

        # Load savedgame file
        try:
            with open(fullpath, 'r') as inputfile:
                self.__dict__ = json.load(inputfile)
        except IOError:
            return 2

        # Adjust dictionary variables from "str":"str" to int:"str"
        # https://stackoverflow.com/questions/21193682/convert-a-string-key-to-int-in-a-dictionary
        self._solved_puzzles = {int(k): v for k, v in self._solved_puzzles.items()}
        self._obtained_clues = {int(k): v for k, v in self._obtained_clues.items()}

        return 0



if __name__ == "__main__":
    mygame = GameState()

    mygame.save_game_state(int(sys.argv[1]))

    # mygame.save_game_state(1)

    # mygame.load_game_state(1)

    # print("city hall" in District.__dict__)
    # print(District["City Hall"].value)
    # print("City Hall" in District.__dict__)
    # print("cityhall" in District.__dict__)
    # print(District(3).name)

    # district_name = "cIty hAll"
    # district_name = district_name.lower()
    # print(district_name in District.__dict__)
    #
    # rname = District[district_name].name
    # print(mygame._visited[rname])


