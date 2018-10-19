from unittest import TestCase
from puzzles import PuzzleType, Puzzle, PuzzleData, PuzzleState, PuzzleDifficulty


class TestPuzzle(TestCase):
    def setUp(self):
        puzzle_data = PuzzleData(question='Do you like puzzles?',
                                 puzzle_type=PuzzleType.RIDDLE,
                                 difficulty= PuzzleDifficulty.EASY,
                                 answer='yes')
        self.test_puzzle = Puzzle(data=puzzle_data,
                                  state=PuzzleState.UNTAKEN)

    def test_puzzle_states(self):
        self.assertFalse(self.test_puzzle.attempt_answer('No'))
        self.assertEqual(self.test_puzzle.state, PuzzleState.TAKEN)
        self.assertEqual(self.test_puzzle.attempted, 1)
        self.assertFalse(self.test_puzzle.attempt_answer('Maybe'))
        self.assertEqual(self.test_puzzle.state, PuzzleState.TAKEN)
        self.assertEqual(self.test_puzzle.attempted, 2)
        self.assertTrue(self.test_puzzle.attempt_answer('Yes'))
        self.assertEqual(self.test_puzzle.state, PuzzleState.SOLVED)
        self.assertEqual(self.test_puzzle.attempted, 3)