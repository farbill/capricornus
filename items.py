from enum import Enum
from functools import reduce
from typing import Dict, List

class ItemType(Enum):
    LEGENDARY = 1       # Critical to storyline, can be dropped. Needed for final game sequence
    CRITICAL = 2        # Critical to storyline, can be dropped. Needed it for main quests
    NONCRITICAL = 3     # Non-critical to storyline, can be dropped, i.e. the user can use it for optional side quests
    FEATURE = 4         # Part of district (includes landscape), cannot be placed into inventory

class ActionType(Enum):
    NONE = 0
    DISPLAY = 1         # Display some text
    ACTION = 2          # Single item interaction, combines with Enum 5 onwards
    TRIGGER = 3         # Item-item interaction
    EVENT = 4           # Talk to character

    TAKE_ITEM = 6       # Pick up critical or non-critical item
    EAT = 7
    HIT = 8
    CLIMB = 9
    MOVE = 10
    SWIM = 11
    LIFT = 12
    FEED = 13



class Action(object):
    def __init__(self,
                commands: List[str],
                response_type: ActionType,
                response: str,
                more_response_type: ActionType = ActionType.NONE,   # Optional, more response
                more_response: str = "",                            # Optional, more response
                more_action = None):                                # Optional additional actions

        self.commands = commands
        self.response_type = response_type
        self.response = response
        self.more_response_type = more_response_type
        self.more_response = more_response
        self.more_action = more_action

class Item(object):
    def __init__(self,
                 name: str,
                 item_type: ItemType,
                 narration: str,
                 description: str,
                 action: List[Action]):
        self.name = name
        self.item_type = item_type
        self.narration = narration
        self.description = description
        self.action = action

    def __eq__(self, other):
        properties = [self.name == other.name,
                      self.item_type == other.item_type,
                      self.narration == other.narration]
        return reduce(lambda x, y: x and y, properties)
