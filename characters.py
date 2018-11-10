from enum import Enum
from typing import List

from items import Item, Action
from main_menu import GAME_WIDTH, dotted_line, empty_line, print_in_the_middle, yes_no_selection, clear_screen, \
    informScreen
from puzzles import Puzzle, PuzzleState

from narration import narration, left_narration


class CharacterState(Enum):
    UNSPOKEN = 0
    SPOKEN = 1

# Enum value corresponds to index of `dialogs` array
class DialogCategory(Enum):
    INITIAL = 0
    RETRY = 1
    FAIL = 2
    SUCCESS = 3
    ALREADY_SOLVED = 4


class Character(object):
    def __init__(self,
                 short_description: str,
                 long_description: str):
        self._short_description = short_description
        self._long_description = long_description
        super().__init__()

    def short_description(self) -> str:
        return self._short_description

    def long_description(self) -> str:
        return self._long_description

    def __str__(self):
        return self._short_description


class AgentDope(Character):
    def __init__(self,
                 short_description: str,
                 long_description: str):
        # Mr. Dope starts with an empty set of items
        self._items = []
        super().__init__(short_description=short_description,
                         long_description=long_description)

    def add_item(self, item) -> None:
        self._items.append(item)

    def remove_item(self, remove_item) -> None:
        self._items = [item for item in self._items if remove_item != item]


class DrCrime(Character):
    def __init__(self,
                 short_description: str,
                 long_description: str,
                 puzzle,
                 dialogs: List):
        self._puzzle = puzzle
        self._dialogs = dialogs

        super().__init__(short_description=short_description,
                         long_description=long_description)


class NonPlayableCharacter(Character):
    def __init__(self,
                 short_description: str,
                 long_description: str,
                 narration: str,
                 puzzle: Puzzle,
                 dialogs: List[str],
                 item: Item,
                 action: List[Action]):
        self._puzzle = puzzle
        self._dialogs = dialogs
        self._item = item
        self._narration = narration
        self._action = action
        self._character_state = CharacterState.UNSPOKEN

        super().__init__(short_description=short_description,
                         long_description=long_description)

    def get_greeting(self) -> str:
        r_str = None
        if self._character_state == CharacterState.UNSPOKEN:
            r_str = self._dialogs[DialogCategory.INITIAL.value]
        elif self._character_state == CharacterState.SPOKEN and self._puzzle.state != PuzzleState.SOLVED:
            r_str = self._dialogs[DialogCategory.RETRY.value]
        elif self._character_state == CharacterState.SPOKEN and self._puzzle.state == PuzzleState.SOLVED:
            r_str = self._dialogs[DialogCategory.ALREADY_SOLVED.value]
        return r_str

    def play_char_puzzle(self, ga, this_district):
        clear_screen()
        msg = self.get_greeting()
        dotted_line_length = GAME_WIDTH
        dotted_line(dotted_line_length)
        empty_line(2)
        narration(msg, dotted_line_length)
        empty_line(2)
        dotted_line(dotted_line_length)

        if self._puzzle.state == PuzzleState.SOLVED :
            input("Press [Enter] to continue...")
        else:
            selection = yes_no_selection(input("Yes/No >>> "))
            if selection == 1:  #yes
                clear_screen()
                self._character_state = CharacterState.SPOKEN
                if self._puzzle.play_puzzle(self._dialogs[DialogCategory.FAIL.value], ga) is True:
                    informScreen(self._dialogs[DialogCategory.SUCCESS.value])
                    if self._item:
                        if ga.space_in_inventory():
                            ga.add_to_inventory(self._item)
                            informScreen(self._item.name + " added to inventory.")
                        else:
                            this_district._dropped_items.append(self._item)
                            informScreen("You don't have space for " + self._item.name + ". It is dropped in the district instead.")

                        self._item = None

