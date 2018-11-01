from functools import reduce
from enum import Enum
from typing import List


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
                 answers: List[str]):
        self.question = question
        # self.puzzle_type = puzzle_type
        # self.difficulty = difficulty
        # self.answer = answer.lower()
        self.answers = map(lambda x: x.lower(), answers)

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

    def get_question(self):
        return self._data.question

    def attempt_answer(self, answer: str) -> bool:
        self.attempted += 1
        answer = answer.lower()
        if answer in self._data.answers:
            self.state = PuzzleState.SOLVED
            return True
        else:
            self.state = PuzzleState.FOUND
            return False




