import json
import city
from characters import AgentDope, NonPlayableCharacter
from clues import Clue
from puzzles import PuzzleData, Puzzle
from city import District, DistrictId, DistrictExits
from items import Item, ItemType, Action, ActionType


class CityLoader(object):
    @staticmethod
    def parse_json(filename):
        with open(filename, 'r') as f:
            config = json.load(f)
        map_arr = list(map(DistrictLoader.parse_json, config['districts']))
        city.assign_street_name(map_arr, config['street_names'])
        legendary_items = list(map(ItemLoader.parse_json, config['legendary_items']))
        boss_puzzles = list(map(PuzzleLoader.parse_json, config['boss_puzzles']))
        return map_arr, legendary_items, boss_puzzles


class CharacterDataLoader(object):
    @staticmethod
    def parse_json(filename, agent_dope=False):
        with open(filename, 'r') as f:
            config = json.load(f)
        if 'puzzle' in config.keys():
            puzzle = PuzzleLoader.parse_json(config['puzzle'])
        else:
            puzzle = None

        if 'item' in config.keys():
            item = ItemLoader.parse_json(config['item'])

        else:
            item = None

        if 'action' in config.keys():
            action = list(map(ActionLoader.parse_json, config['action']))
        else:
            action = None

        if agent_dope:
            return AgentDope(short_description=config['short_description'],
                             long_description=config['long_description'])
        else:
            return NonPlayableCharacter(short_description=config['short_description'],
                                        long_description=config['long_description'],
                                        narration=config['narration'],
                                        puzzle=puzzle,
                                        item=item,
                                        dialogs=config['dialogs'],
                                        action=action)


class DistrictLoader(object):
    @staticmethod
    def parse_json(filename) -> District:
        with open(filename, 'r') as f:
            config = json.load(f)
        id = DistrictId(x=config['x'],
                        y=config['y'])
        characters = list(map(CharacterDataLoader.parse_json, config['characters']))
        items = list(map(ItemLoader.parse_json, config['district_items']))

        return District(id=id,
                        district_name=config['name'],
                        district_items=items,
                        dropped_items=[],
                        clues=config['clues'],
                        characters=characters,
                        short_description=config['short_description'],
                        long_description=config['long_description'],
                        district_exits = DistrictExits()
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
            item_type = ItemType.LEGENDARY
        elif item_type == 'FEATURE':
            item_type = ItemType.FEATURE
        else:
            error_message = "Encountered incorrect value in ItemLoader while loading json file{filename}"\
                            "item_type:{item_type}, item_type should be CRITICAL, LEGENDARY, FEATURE or NONCRITICAL"\
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


class PuzzleLoader(object):

    @staticmethod
    def parse_json(filename) -> Puzzle:
        with open(filename, 'r') as f:
            config = json.load(f)
        return Puzzle(data=PuzzleData(question=config['question'],
                                      answers=config['answers']))


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
        elif response_type == 'take_item':
            return ActionType.TAKE_ITEM
        elif response_type == 'eat':
            return ActionType.EAT
        elif response_type == 'hit':
            return ActionType.HIT
        elif response_type == 'climb':
            return ActionType.CLIMB
        elif response_type == 'move':
            return ActionType.MOVE
        elif response_type == 'touch':
            return ActionType.TOUCH
        elif response_type == 'steal':
            return ActionType.STEAL
        elif response_type == 'FEED':
            return ActionType.FEED
