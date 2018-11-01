from typing import List
from enum import Enum
from puzzles import Puzzle, PuzzleState
from items import Item, Action
import time
from main_menu import GAME_WIDTH, dotted_line, empty_line, print_in_the_middle, print_left_indented, write_over, \
    go_up_and_clear, yes_no_selection, clear_screen, informScreen

import load_save_menu

class CharacterState(Enum):
    UNSPOKEN = 0
    SPOKEN = 1

class DialogCategory(Enum): #corresponds to index of dialogs list
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
                 dialogs: [str],
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
            # self._character_state = CharacterState.SPOKEN
        elif self._character_state == CharacterState.SPOKEN and self._puzzle.state != PuzzleState.SOLVED:
            r_str = self._dialogs[DialogCategory.RETRY.value]
        elif self._character_state == CharacterState.SPOKEN and self._puzzle.state == PuzzleState.SOLVED:
            r_str = self._dialogs[DialogCategory.ALREADY_SOLVED.value]
        return r_str

    def get_success_fail_msg(self, msg_type:str) -> str:
        if msg_type == "success":
            return self._dialogs[DialogCategory.SUCCESS.value]
        elif msg_type == "fail":
            return self._dialogs[DialogCategory.FAIL.value]

    def play_char_puzzle(self, ga):
        clear_screen()
        msg = self.get_greeting()

        dotted_line_length = GAME_WIDTH
        dotted_line(dotted_line_length)
        empty_line(1)
        print_in_the_middle(dotted_line_length, msg)
        empty_line(1)
        dotted_line(dotted_line_length)

        if(self._puzzle.state == PuzzleState.SOLVED):
            empty_line(1)
            input("Press [Enter] to continue...")
        else:
            selection = yes_no_selection(input("Yes/No >>> "))
            if selection == 1:  #yes
                clear_screen()
                self._character_state = CharacterState.SPOKEN
                if self._puzzle.play_puzzle(self._dialogs[DialogCategory.FAIL.value]) is True:
                    self.success_screen()
                    ga.add_to_inventory(self._item)
                    informScreen(self._item.name + " added to inventory.")
                    self._item = None


    def success_screen(self):
        clear_screen()
        msg = self._dialogs[DialogCategory.SUCCESS.value]

        dotted_line_length = GAME_WIDTH
        dotted_line(dotted_line_length)
        empty_line(1)
        print_in_the_middle(dotted_line_length, msg)
        empty_line(1)
        dotted_line(dotted_line_length)
        input("Press [Enter] to continue...")