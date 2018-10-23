from characters import Character
from typing import Tuple, List


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

    def get_exits(self) -> Tuple[str, str, str, str]:
        return [self._north_exit, self._south_exit,
                self._west_exit, self._east_exit]

class District(object):
    def __init__(self,
                 id: DistrictId,
                 district_name: str,
                 items: List,
                 clues: List,
                 characters: List[Character],
                 short_description,
                 long_description,
                 district_exits: DistrictExits = DistrictExits()):
        self._id = id
        self._district_name = district_name
        self._items = items
        self._clues = clues
        self._characters = characters
        self._short_description = short_description
        self._long_description = long_description
        self._district_exits = district_exits