from functools import reduce
from enum import Enum
from typing import List
import time
from command_parsing import command_parsing
from main_menu import GAME_WIDTH, dotted_line, empty_line, print_in_the_middle, print_left_indented, write_over, \
    go_up_and_clear, yes_no_selection, clear_screen


class PuzzleType(Enum):
    RIDDLE = 1
    MATH = 2
    SCIENCE = 3
    WORD = 4


class PuzzleDifficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class PuzzleState(Enum):
    NEW = 1
    FOUND = 2
    SOLVED = 3


class PuzzleData(object):
    def __init__(self,
                 question: str,
                 # puzzle_type: PuzzleType,
                 # difficulty: PuzzleDifficulty,
                 answers: [str]):
        self.question = question
        self.answers = []
        for x in answers:
            self.answers.append(x)
        # self.puzzle_type = puzzle_type
        # self.difficulty = difficulty


    def __eq__(self, other):
        properties = [self.question == other.question]
                      # self.puzzle_type == other.puzzle_type,
                      # self.difficulty == other.difficulty,
        return reduce(lambda x, y: x and y, properties)


class Puzzle(object):
    def __init__(self,
                 data: PuzzleData,
                 state: PuzzleState = PuzzleState.NEW):
        self._data = data
        self.state = state
        self.attempted = 0

    def play_puzzle(self, failed_msg: str) -> bool:
        self.state = PuzzleState.FOUND
        clear_screen()
        msg1 = self._data.question
        msg2 = "Type \"back\" to exit puzzle."
        dotted_line_length = GAME_WIDTH
        dotted_line(dotted_line_length)
        empty_line(1)
        print_in_the_middle(dotted_line_length, msg1)
        empty_line(1)
        print_in_the_middle(dotted_line_length, msg2)
        empty_line(1)
        dotted_line(dotted_line_length)

        # for x in self._data.answers:
        #     print(x)

        selection = self.puzzle_selection(input(">>> "), self._data.answers, failed_msg)
        if selection == 1:  #puzzle solved
            self.state = PuzzleState.SOLVED
            return True
        else:
            return False

    def puzzle_selection(self, the_input: str, possible_answers: [str], failed_msg: str):

        # inputs to be recognized as valid
        list_answers =  possible_answers
        list_exit = ["exit", "quit", "back", "go back"]

        selection = 0
        lowered_input = str(the_input).lower()  # to make the input case insensitive

        while True:

            if command_parsing(lowered_input, list_answers):
                selection = 1
                break

            if command_parsing(lowered_input, list_exit):
                selection = 2
                break

            if len(the_input) > 99:
                write_over("Your input is too long.")
            write_over(failed_msg)
            go_up_and_clear()
            lowered_input = str(input(">>> ")).lower()

        return int(selection)
