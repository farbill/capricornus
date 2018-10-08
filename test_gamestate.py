from unittest import TestCase

import gamestate


class GameStateTestCase(TestCase):
    def setUp(self):
        self.game_state = gamestate.GameState()      # initialize instance of GameState class

    # def tearDown(self):
    #     print("teardown -- ")

    def test_initial(self):
        self.assertEqual(self.game_state._turns_remaining, gamestate.INITIAL_NUMBER_OF_TURNS)
        self.assertEqual(self.game_state._current_location, "city_hall")

    def test_direct_input(self):
        self.game_state._current_location = "gato_springs"
        self.assertEqual(self.game_state._current_location, "gato_springs")

