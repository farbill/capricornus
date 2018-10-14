from unittest import TestCase

import gamestate
import os.path


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

    # Test invalid options for save game function
    def test_invalid_save_game_state(self):
        save_slot = 0
        self.assertEqual(self.game_state.save_game_state(save_slot), 1)
        self.assertEqual(os.path.isfile("savedgame_" + str(save_slot)), False)
        save_slot = 4
        self.assertEqual(self.game_state.save_game_state(save_slot), 1)
        self.assertEqual(os.path.isfile("savedgame_" + str(save_slot)), False)
        save_slot = -1
        self.assertEqual(self.game_state.save_game_state(save_slot), 1)
        self.assertEqual(os.path.isfile("savedgame_" + str(save_slot)), False)
        save_slot = 100
        self.assertEqual(self.game_state.save_game_state(save_slot), 1)
        self.assertEqual(os.path.isfile("savedgame_" + str(save_slot)), False)

    # Test valid save game function
    def test_valid_save_game_state(self):
        # Values to test against
        self.game_state._turns_remaining = 123
        self.game_state._current_location = "Gato Springs"
        self.game_state._current_inventory = ["key", "rock"]
        self.game_state._solved_puzzles = {1: "puzzle one", 5: "puzzle five"}
        self.game_state._obtained_clues = {3: "clue three", 7: "clue seven"}
        self.game_state._lair_location = "Paradise Creek"

        # Test existence of savedgame folder
        dirname = os.path.join(os.path.realpath('.'), "savedgames")
        self.assertEqual(os.path.exists(dirname), True)

        # Test save file exists and saved data to file as expected
        for num in range(3):
            save_slot = num + 1
            self.assertEqual(self.game_state.save_game_state(save_slot), 0)
            filename = "savedgame_" + str(save_slot)
            fullpath = os.path.join(dirname, filename)
            self.assertEqual(os.path.isfile(fullpath), True)
            with open(fullpath, 'r') as inputfile:
                content = inputfile.readlines()
                self.assertEqual(content[0], '{"_turns_remaining": 123, "_current_location": "Gato Springs", "_current_inventory": ["key", "rock"], "_solved_puzzles": {"1": "puzzle one", "5": "puzzle five"}, "_obtained_clues": {"3": "clue three", "7": "clue seven"}, "_vision_orb": false, "_strength_orb": false, "_vitality_orb": false, "_magic_sword": false, "_visited": {"City Hall": false, "Hawkins": false, "Washington Heights": false, "Greenland Grove": false, "Oak Square": false, "Northtown": false, "River Gardens": false, "Bayrock": false, "Sunset Hills": false, "Lemonfield": false, "Gato Springs": false, "Webster Mountain": false, "Paradise Creek": false, "Coltwood": false, "Lake Cypress": false}, "_lair_location": "Paradise Creek"}')

        # Remove saved files for clean up
        for num in range(3):
            filename = "savedgame_" + str(num + 1)
            fullpath = os.path.join(dirname, filename)
            os.remove(fullpath)

    # Test invalid options for load game function
    def test_invalid_load_game_state(self):

        dirname = os.path.join(os.path.realpath('.'), "savedgames")

        load_slot = 0
        self.assertEqual(self.game_state.load_game_state(load_slot), 1)
        filename = "savedgame_" + str(load_slot)
        self.assertEqual(os.path.isfile(os.path.join(dirname, filename)), False)

        load_slot = 4
        self.assertEqual(self.game_state.load_game_state(load_slot), 1)
        filename = "savedgame_" + str(load_slot)
        self.assertEqual(os.path.isfile(os.path.join(dirname, filename)), False)

        load_slot = -1
        self.assertEqual(self.game_state.load_game_state(load_slot), 1)
        filename = "savedgame_" + str(load_slot)
        self.assertEqual(os.path.isfile(os.path.join(dirname, filename)), False)

        load_slot = 100
        self.assertEqual(self.game_state.load_game_state(load_slot), 1)
        filename = "savedgame_" + str(load_slot)
        self.assertEqual(os.path.isfile(os.path.join(dirname, filename)), False)

    # Test valid load game function
    def test_valid_load_game_state(self):
        # Values to test against
        self.game_state._turns_remaining = 123
        self.game_state._current_location = "Gato Springs"
        self.game_state._current_inventory = ["key", "rock"]
        self.game_state._solved_puzzles = {1: "puzzle one", 5: "puzzle five"}
        self.game_state._obtained_clues = {3: "clue three", 7: "clue seven"}
        self.game_state._lair_location = "Paradise Creek"
        self.game_state._visited["Lemonfield"] = True

        # savedgame directory
        dirname = os.path.join(os.path.realpath('.'), "savedgames")

        # Create save file, and load back save file and verify data
        for num in range(3):
            # Create a saved game file
            save_slot = num + 1
            self.game_state.save_game_state(save_slot)

            # Instantiate new gamestate object and assert initial values
            gs = gamestate.GameState()
            self.assertEqual(gs._turns_remaining, gamestate.INITIAL_NUMBER_OF_TURNS)
            self.assertEqual(gs._current_location, "City Hall")
            self.assertEqual(gs._current_inventory, [])
            self.assertEqual(gs._solved_puzzles, {})
            self.assertEqual(gs._obtained_clues, {})
            self.assertEqual(gs._lair_location in ('Webster Mountain', 'Paradise Creek', 'Coltwood', 'Lake Cypress'), True)
            self.assertEqual(gs._visited["Lemonfield"], False)

            # Load in saved game data and assert expected value
            self.assertEqual(gs.load_game_state(save_slot), 0)
            self.assertEqual(gs._turns_remaining, 123)
            self.assertEqual(gs._current_location, "Gato Springs")
            self.assertEqual(gs._current_inventory, ["key", "rock"])
            self.assertEqual(gs._solved_puzzles, { 1: "puzzle one", 5: "puzzle five"})
            self.assertEqual(gs._obtained_clues, {3: "clue three", 7: "clue seven"})
            self.assertEqual(gs._lair_location, "Paradise Creek")
            self.assertEqual(gs._visited["Lemonfield"], True)

        # Remove saved files for clean up
        for num in range(3):
            filename = "savedgame_" + str(num + 1)
            fullpath = os.path.join(dirname, filename)
            os.remove(fullpath)