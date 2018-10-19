import json
from characters import AgentDope, NonPlayableCharacter
from puzzles import PuzzleData, PuzzleType, PuzzleDifficulty
from city import District, DistrictId
from items import Item, ItemType


class CharacterDataLoader(object):
    @staticmethod
    def parse_json(filename, agent_dope=False):
        config = json.load(filename)
        if agent_dope:
            return AgentDope(short_description=config['short_description'],
                             long_description=config['long_description'])
        else:
            return NonPlayableCharacter(short_description=config['short_description'],
                                        long_description=config['long_description'])


class DistrictLoader(object):
    @staticmethod
    def parse_json(filename) -> District:
        config = json.load(filename)
        id = DistrictId(x=config['x'],
                        y=config['y'])
        characters = []
        for character_file in config['characters']:
            characters.append(CharacterDataLoader.parse_json(character_file))

        return District(id=id,
                        items=config['items'],
                        clues=config['clues'],
                        characters=characters,
                        short_description=config['short_description'],
                        long_description=config['long_description']
                        )


class ItemLoader(object):
    @staticmethod
    def parse_json(filename) -> Item:
        with open(filename, 'r') as f:
            config = json.load(f)
        item_type = config['item_type']
        if item_type == 'CRITICAL':
            item_type = ItemType.CRITICAL
        elif item_type == 'NONCRITICAL':
            item_type = ItemType.NONCRITICAL
        else:
            error_message = "Encountered incorrect value in ItemLoader while loading json file{filename}"\
                            "item_type:{item_type}, item_type should be CRITICAL or NONCRITICAL"\
                            .format(filename=filename, item_type=item_type)
            raise ValueError(error_message)
        return Item(name=config['name'],
                    item_type=item_type,
                    narration=config['narration'])


class PuzzleDataLoader(object):

    @staticmethod
    def parse_json(filename) -> PuzzleData:
        with open(filename, 'r') as f:
            config = json.load(f)
        difficulty = PuzzleDataLoader._get_puzzle_difficulty(config['difficulty'])
        puzzle_type = PuzzleDataLoader._get_puzzle_type(config['puzzle_type'])
        return PuzzleData(question=config['question'],
                          puzzle_type=puzzle_type,
                          difficulty=difficulty,
                          answer=config['answer'])

    @staticmethod
    def _get_puzzle_difficulty(puzzle_difficulty: str) -> PuzzleDifficulty:
        puzzle_difficulty = puzzle_difficulty.lower()
        if puzzle_difficulty == 'easy':
            return PuzzleDifficulty.EASY
        elif puzzle_difficulty == 'medium':
            return PuzzleDifficulty.MEDIUM
        elif puzzle_difficulty == 'hard':
            return PuzzleDifficulty.HARD
        
    @staticmethod
    def _get_puzzle_type(puzzle_type: str) -> PuzzleType:
        puzzle_type = puzzle_type.lower()
        if puzzle_type == 'riddle':
            return PuzzleType.RIDDLE
        elif puzzle_type == 'math':
            return PuzzleType.MATH
        elif puzzle_type == 'science':
            return PuzzleType.SCIENCE
        elif puzzle_type == 'word':
            return PuzzleType.WORD

