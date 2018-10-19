import json
from items import Item, ItemType
from loaders import ItemLoader, PuzzleDataLoader
from unittest import TestCase
from puzzles import PuzzleType, PuzzleDifficulty, PuzzleData


class TestLoaders(TestCase):
    def test_item_parse_json(self):
        filename = 'test_item.json'
        name_value = "TesterItem"
        narration = "Once, upon a time, there was a critical test item"
        data = {"name": name_value,
                "item_type": "CRITICAL",
                "narration": narration
                }
        with open(filename, 'w') as fo:
            json.dump(data, fo)

        item = ItemLoader.parse_json(filename)
        test_item = Item(name=name_value,
                         item_type=ItemType.CRITICAL,
                         narration=narration)
        self.assertEqual(item, test_item)

    def test_puzzle_data_parse_json(self):
        filename = 'test_puzzle_data.json'
        question = 'Do you like the loaders?'
        answer = 'no'
        puzzle_type = PuzzleType.RIDDLE
        difficulty = PuzzleDifficulty.HARD
        data = {'question': question,
                'puzzle_type': 'riddle',
                'difficulty': 'hard',
                'answer': 'no'
                }
        with open(filename, 'w') as fo:
            json.dump(data, fo)
        puzzle_data = PuzzleDataLoader.parse_json(filename)
        test_puzzle_data = PuzzleData(question=question,
                                      puzzle_type=puzzle_type,
                                      difficulty=difficulty,
                                      answer=answer)
        self.assertEqual(puzzle_data, test_puzzle_data)




