from functools import reduce
from enum import Enum


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
    UNTAKEN = 1
    TAKEN = 2
    SOLVED = 3


class PuzzleData(object):
    def __init__(self,
                 question: str,
                 puzzle_type: PuzzleType,
                 difficulty: PuzzleDifficulty,
                 answer: str):
        self.question = question
        self.puzzle_type = puzzle_type
        self.difficulty = difficulty
        self.answer = answer.lower()

    def __eq__(self, other):
        properties = [self.question == other.question,
                      self.puzzle_type == other.puzzle_type,
                      self.difficulty == other.difficulty,
                      self.answer == other.answer]
        return reduce(lambda x, y: x and y, properties)


class Puzzle(object):
    def __init__(self,
                 data: PuzzleData,
                 state: PuzzleState = PuzzleState.UNTAKEN):
        self._data = data
        self.state = state
        self.attempted = 0

    def get_question(self):
        return self._data.question

    def attempt_answer(self, answer: str) -> bool:
        self.attempted += 1
        answer = answer.lower()
        if answer == self._data.answer:
            self.state = PuzzleState.SOLVED
            return True
        else:
            self.state = PuzzleState.TAKEN
            return False




