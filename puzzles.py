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
                 state: PuzzleState):
        self._question = question
        self._puzzle_type = puzzle_type
        self._difficulty = difficulty
        self._state = state

class Puzzle(object):
    def __init__(self,
                 data: PuzzleData):
        self._data = data

    def play(self):
        # takes input, and then alters puzzles state depending on answer
        self._ask_question()
        answer = self._get_answer()
        self._evaluate_answer(answer)
        '''
        BILL: I'm not quite sure what to do here? do we want the puzzle itself
        to ask the question, or should we pass in some sort of output mode?
        if you passed in an output mode we could eventually make the game so
        that it doesn't even depend on text input(could have a GUI for example)
        '''

    def _get_answer(self):
        pass

    def _ask_question(self) -> None:
        pass

    def _evaluate_answer(self, answer) -> bool:
        # TODO: how do we want to evaluate answers?
        # should we make a separate class for evaluating/NLP
        # probably makes sense right?
        return False
