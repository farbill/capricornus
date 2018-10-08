from enum import Enum


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

