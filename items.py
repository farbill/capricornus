from enum import Enum
from functools import reduce

class ItemType(Enum):
    LEGENDARY = 1       # Critical to storyline, CANNOT be dropped. Once acquired, the corresponding boolean value is permenantly changed
    CRITICAL = 2        # Critical to storyline, can be dropped, i.e. the user must need it for main quests
    NONCRITICAL = 3     # Non-critical to storyline, can be dropped, i.e. the user can use it for optional side quests
    FEATURE = 4         # Part of district, cannot be placed into inventory


class Item(object):
    def __init__(self,
                 name: str,
                 item_type: ItemType,
                 narration):
        self.name = name
        self.item_type = item_type
        self.narration = narration

    def __eq__(self, other):
        properties = [self.name == other.name,
                      self.item_type == other.item_type,
                      self.narration == other.narration]
        return reduce(lambda x, y: x and y, properties)

                            

