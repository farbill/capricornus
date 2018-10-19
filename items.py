from enum import Enum
from functools import reduce

class ItemType(Enum):
    CRITICAL = 1
    NONCRITICAL = 2


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

                            

