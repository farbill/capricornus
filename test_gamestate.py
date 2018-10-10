from unittest import TestCase

import gamestate


class GameStateTestCase(TestCase):
    def setUp(self):
        self.game_state = gamestate.GameState()      # initialize instance of GameState class

    # def tearDown(self):
    #     print("teardown -- ")

    # Test initialization
    def test_initial(self):
        self.assertEqual(self.game_state._turns_remaining, gamestate.INITIAL_NUMBER_OF_TURNS)
        self.assertEqual(self.game_state._current_location, "City Hall")

        # Ensure all districts in _visited dictionary is set to False
        for district in gamestate.District:
            self.assertFalse(self.game_state._visited[district.name])

        # Checks _lair_location is correctly selected within range
        num = gamestate.District[self.game_state._lair_location].value
        self.assertTrue(gamestate.RANDOM_DISTRICT_LOWER_LIMIT <= num <= gamestate.RANDOM_DISTRICT_UPPER_LIMIT)

    # Test direct input
    def test_direct_input(self):
        self.game_state._current_location = "Gato Springs"
        self.assertEqual(self.game_state._current_location, "Gato Springs")

