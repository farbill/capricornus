from characters import Character
from typing import Tuple, List
from enum import Enum
import items
import clues

class CARDINAL(Enum):
    NORTH = 0
    SOUTH = 1
    WEST = 2
    EAST = 3

class City(object):
    def __init__(self,
                 name,
                 short_description,
                 long_description,
                 grid_size):
        self.name = name
        self._short_description = short_description
        self._long_description = long_description
        self._grid = [[None for _ in range(len(grid_size))] for _ in range(len(grid_size))]


class DistrictId(object):
    def __init__(self,
                 x: int,
                 y: int):
        self._x = x
        self._y = y

    def get_id(self) -> Tuple[int, int]:
        return self._x, self._y

# Default value is empty string
class DistrictExits(object):
    def __init__(self,
                 north_exit: str = "",
                 south_exit: str = "",
                 west_exit: str = "",
                 east_exit: str = ""):
        self._north_exit = north_exit
        self._south_exit = south_exit
        self._west_exit = west_exit
        self._east_exit = east_exit

    def get_exits(self) -> [str, str, str, str]:
        return [self._north_exit, self._south_exit,
                self._west_exit, self._east_exit]

class District(object):
    def __init__(self,
                 id: DistrictId,
                 district_name: str,
                 district_items: List[items.Item],
                 dropped_items: List[items.Item],
                 clues: List[clues.Clue],
                 characters: List[Character],
                 short_description: str,
                 long_description: str,
                 district_exits: DistrictExits = DistrictExits()):
        self._id = id
        self._district_name = district_name
        self._district_items = district_items
        self._dropped_items = dropped_items
        self._clues = clues
        self._characters = characters
        self._short_description = short_description
        self._long_description = long_description
        self._district_exits = district_exits

def assign_street_name(map_arr: [District], street_names):
    name_arr = street_names

    name_index = 0

    for district in map_arr:

        this_district_xy = district._id.get_id()

        # North, South, West, East -- district info
        relative_coord = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        static_coord = [None, None, None, None]
        nswe_districts_obj = [None, None, None, None]

        # get N, S, W, E districts
        # https://stackoverflow.com/questions/1169725/adding-values-from-tuples-of-same-length
        for i in range(4):
            static_coord[i] = tuple(sum(x) for x in zip(this_district_xy, relative_coord[i]))

        # Assign district obj to NSWE
        for district_obj in map_arr:
            for i in range(4):
                if static_coord[i] == district_obj._id.get_id():
                    nswe_districts_obj[i] = district_obj


        if district._district_exits._north_exit == "" and nswe_districts_obj[CARDINAL.NORTH.value] is not None:
            district._district_exits._north_exit = name_arr[name_index]
            nswe_districts_obj[CARDINAL.NORTH.value]._district_exits._south_exit = name_arr[name_index]
            name_index += 1

        if district._district_exits._south_exit == "" and nswe_districts_obj[CARDINAL.SOUTH.value] is not None:
            district._district_exits._south_exit = name_arr[name_index]
            nswe_districts_obj[CARDINAL.SOUTH.value]._district_exits._north_exit = name_arr[name_index]
            name_index += 1

        if district._district_exits._west_exit == "" and nswe_districts_obj[CARDINAL.WEST.value] is not None:
            district._district_exits._west_exit = name_arr[name_index]
            nswe_districts_obj[CARDINAL.WEST.value]._district_exits._east_exit = name_arr[name_index]
            name_index += 1

        if district._district_exits._east_exit == "" and nswe_districts_obj[CARDINAL.EAST.value] is not None:
            district._district_exits._east_exit = name_arr[name_index]
            nswe_districts_obj[CARDINAL.EAST.value]._district_exits._west_exit = name_arr[name_index]
            name_index += 1

    return map_arr