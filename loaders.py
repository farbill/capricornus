import json
from characters import AgentDope, NonPlayableCharacter
from clues import Clue
from puzzles import PuzzleData, PuzzleType, PuzzleDifficulty
from city import District, DistrictId
from items import Item, ItemType, Action, ActionType


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
        with open(filename, 'r') as f:
            config = json.load(f)
        id = DistrictId(x=config['x'],
                        y=config['y'])
        characters = []
        items = []
        for character_file in config['characters']:
            characters.append(CharacterDataLoader.parse_json(character_file))

        for item_file in config['district_items']:
            items.append(ItemLoader.parse_json(item_file))
        return District(id=id,
                        district_name=config['name'],
                        district_items=items,
                        dropped_items=[],
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
        elif item_type == 'LEGENDARY':
            item_type == ItemType.LEGENDARY
        elif item_type == 'FEATURE':
            item_type == ItemType.FEATURE
        else:
            error_message = "Encountered incorrect value in ItemLoader while loading json file{filename}"\
                            "item_type:{item_type}, item_type should be CRITICAL.LEGENDARY, FEATURE or NONCRITICAL"\
                            .format(filename=filename, item_type=item_type)
            raise ValueError(error_message)
        actions = list(map(ActionLoader.parse_json, config['actions']))
        return Item(name=config['name'],
                    item_type=item_type,
                    narration=config['narration'],
                    description=config['description'],
                    action=actions)


class ClueLoader(object):
    @staticmethod
    def parse_json(filename) -> Clue:
        with open(filename, 'r') as f:
            config = json.load(f)
        return Clue(name=config['name'],
                    contents=config['contents'])


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


class ActionLoader(object):

    @staticmethod
    def parse_json(filename) -> Action:
        with open(filename, 'r') as f:
            config = json.load(f)
        response_type = ActionLoader._get_response_type(config['response_type'])
        more_response = config['more_response'] if 'more_response' in config.keys() else None
        if 'more_response_type' in config.keys():
            more_response_type = ActionLoader._get_response_type(config['more_response_type'])
        else:
            more_response_type = None
        if 'more_action' in config.keys():
            more_action = list(map(ActionLoader.parse_json, config['more_action']))
        else:
            more_action = None
        return Action(commands=config['commands'],
                      response_type=response_type,
                      response=config['response'],
                      more_response_type=more_response_type,
                      more_response=more_response,
                      more_action=more_action)

    @staticmethod
    def _get_response_type(response_type: str) -> ActionType:
        response_type = response_type.lower()
        if response_type == 'none':
            return ActionType.NONE
        elif response_type == 'display':
            return ActionType.DISPLAY
        elif response_type == 'action':
            return ActionType.ACTION
        elif response_type == 'trigger':
            return ActionType.TRIGGER
        elif response_type == 'event':
            return ActionType.EVENT
        elif response_type == 'take_legendary':
            return ActionType.TAKE_LEGENDARY
        elif response_type == 'take_item':
            return ActionType.TAKE_ITEM
