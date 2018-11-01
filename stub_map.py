import characters
import city
from items import Item, ItemType, Action, ActionType
from loaders import DistrictLoader
from typing import List, Dict
import item_instances
import characters
from puzzles import Puzzle, PuzzleData, PuzzleState

def get_map_stub():
    city_hall = DistrictLoader.parse_json('etc/districts/city_hall.json')
    hawkins = DistrictLoader.parse_json('etc/districts/hawkins.json')
    greenland_grove = DistrictLoader.parse_json('etc/districts/greenland_grove.json')
    oak_square = DistrictLoader.parse_json('etc/districts/oak_square.json')
    bayrock = DistrictLoader.parse_json('etc/districts/bayrock.json')
    river_gardens = DistrictLoader.parse_json('etc/districts/river_gardens.json')
    paradise_creek = DistrictLoader.parse_json('etc/districts/paradise_creek.json')
    northtown = DistrictLoader.parse_json('etc/districts/northtown.json')
    lake_cypress = DistrictLoader.parse_json('etc/districts/lake_cypress.json')
    sunset_hills = DistrictLoader.parse_json('etc/districts/sunset_hills.json')
    washington_heights = DistrictLoader.parse_json('etc/districts/washington_heights.json')
    gato_springs = DistrictLoader.parse_json('etc/districts/gato_springs.json')
    webster_mountain = DistrictLoader.parse_json('etc/districts/webster_mountain.json')
    lemon_field = DistrictLoader.parse_json('etc/districts/lemon_field.json')
    colt_wood = DistrictLoader.parse_json('etc/districts/colt_wood.json')

    # TEMPORARY hardcode character and puzzle data for stub

    a_puzzle = Puzzle(
        state = PuzzleState.NEW,
        data = PuzzleData(
            question="What is 1 + 1?",
            answers = [
                "2",
                "two"
            ]
        )
    )

    a_item = Item(
        name = "Red Key",
        item_type = ItemType.CRITICAL,
        narration = "",
        description = "It looks like it can be used to open a door.",
        action = [
            Action(
                commands = [
                    "use red key on red door",
                    "use red key on door"
                ],
                response_type = ActionType.ACTION,
                response = "The Red Door opened."
            )
        ]
    )

    a_npc = characters.NonPlayableCharacter(
        short_description = "npc short description",
        long_description = "npc long description",
        narration = "A Hobo is sitting down.",
        puzzle = a_puzzle,
        item = a_item,
        dialogs = [
            "I got a puzzle for you.",
            "You want another try at it?",
            "Sorry kid, that aint it.",
            "Good job kid, here - you can have this.",
            "You already solved my puzzle. Now scram."
        ],
        action = [
            Action(
                commands = [
                    "talk to hobo",
                    "talk hobo",
                    "speak hobo",
                    "speak to hobo"
                ],
                response_type = ActionType.EVENT,
                response = ""
            )
        ]

    )

    city_hall._characters = [
        a_npc
    ]

    map_arr = [city_hall, hawkins, greenland_grove, bayrock, river_gardens,
               oak_square, paradise_creek, northtown, lake_cypress, sunset_hills,
               washington_heights, gato_springs, webster_mountain, lemon_field, colt_wood]

    map_arr = city.assign_street_name(map_arr)

    return map_arr
