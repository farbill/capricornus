from characters import Character
from typing import Tuple, List


class City(object):
    def __init__(self,
                 name,
                 short_description,
                 long_description):
        self.name = name
        self._short_description = short_description
        self._long_description = long_description


class DistrictId(object):
    def __init__(self,
                 x: int,
                 y: int):
        self._x = x
        self._y = y

    def get_id(self) -> Tuple[int, int]:
        return self._x, self._y


class District(object):
    def __init__(self,
                 id: DistrictId,
                 items: List,
                 clues: List,
                 characters: List[Character],
                 short_description,
                 long_description):
        self._id = id
        self._items = items
        self._clues = clues
        self._characters = characters
        self._short_description = short_description
        self._long_description = long_description
