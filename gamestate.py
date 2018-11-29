import json
from typing import List, Dict
import string
import random
from enum import Enum
import itertools
import sys
import os

import pickle


RANDOM_DISTRICT_LOWER_LIMIT = 7
RANDOM_DISTRICT_UPPER_LIMIT = 12

INITIAL_NUMBER_OF_TURNS = 20
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
    10: ["Lemonfield", "lemonfield"],
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
        self._current_inventory = []                     # type: List[items.Item]
        # self._solved_puzzles = {}                        # type: Dict[int, str]
        self._obtained_clues = []                        # type:[str]

        # Legendary items
        self._vision_orb =      False
        self._strength_orb =    False
        self._vitality_orb =    False
        self._magic_sword =     False

        # Track game status
        self._visited = self._initialize_visited()
        self._lair_location = self._randomly_select_lair_location()

        # Data to load in
        self.uncollected_legendary_items = []
        self._map_arr = []
        self.boss_puzzles = []

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

    # Assign to self._lair_location: [7:'River Gardens', 12:'Webster Mountain']
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
            with open(fullpath, 'wb') as outputfile:
                pickle.dump(self.__dict__, outputfile)
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
            with open(fullpath, 'rb') as inputfile:
                self.__dict__ = pickle.load(inputfile)
        except IOError:
            return 2

        return 0
