from unittest import TestCase

import GameState


class GameStateTestCase(TestCase):
    def setUp(self):
        self.game_state = GameState.GameState()      # initialize instance of GameState class

    # def tearDown(self):
    #     print("teardown -- ")

    def test_initial(self):
        self.assertEqual(self.game_state.turns_remaining, GameState.INITIAL_NUMBER_OF_TURNS)
        self.assertEqual(self.game_state.current_location, "city_hall")

    def test_direct_input(self):
        self.game_state.current_location = "gato_springs"
        self.assertEqual(self.game_state.current_location, "gato_springs")

