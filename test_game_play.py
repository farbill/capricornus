from unittest import TestCase

import gamestate
import gameaction
import game_play
import city
import os


class GamePlayTestCase(TestCase):
    def setUp(self):
        self.game_state = gamestate.GameState()
        self.game_action = gameaction.GameAction(self.game_state)
        pass

    # def tearDown(self):
    #     print("teardown -- ")

    # Test gametext_output
    def test_gametext_output(self):
        city_hall = city.District(city.DistrictId(2, 3),
                                  "City Hall",
                                  ["an item - key1"],
                                  ["a clue - the eagle has landed1"],
                                  [],  # character list
                                  "City Hall short description",
                                  "City Hall long description")
        hawkins = city.District(city.DistrictId(2, 4),
                                "Hawkins",
                                ["an item - key2"],
                                ["a clue - the eagle has landed2"],
                                [],  # character list
                                "Hawkins short description",
                                "Hawkins long description")
        greenland_grove = city.District(city.DistrictId(1, 3),
                                        "Greenland Grove",
                                        ["an item - key3"],
                                        ["a clue - the eagle has landed3"],
                                        [],  # character list
                                        "Greenland Grove short description",
                                        "Greenland Grove long description")
        oak_square = city.District(city.DistrictId(3, 3),
                                   "Oak Square",
                                   ["an item - key4"],
                                   ["a clue - the eagle has landed4"],
                                   [],  # character list
                                   "Oak Square short description",
                                   "Oak Square long description")
        map_arr = [city_hall, hawkins, greenland_grove, oak_square]

        game_play.gametext_output(self.game_action, map_arr)

        pass