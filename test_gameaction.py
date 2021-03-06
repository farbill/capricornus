from unittest import TestCase

import gamestate
import gameaction


class GameActionTestCase(TestCase):
    def setUp(self):
        self.game_state = gamestate.GameState()
        self.game_action = gameaction.GameAction(self.game_state)

    # def tearDown(self):
    #     print("teardown -- ")

    # Test turns remains (getter and decrementer functions)
    def test_turns_remaining(self):
        self.assertEqual(self.game_action.turns_remaining, gamestate.INITIAL_NUMBER_OF_TURNS)
        self.game_action.decrement_turns_remaining()
        self.assertEqual(self.game_action.turns_remaining, gamestate.INITIAL_NUMBER_OF_TURNS - 1)
        self.game_action.decrement_turns_remaining()
        self.game_action.decrement_turns_remaining()
        self.assertEqual(self.game_action.turns_remaining, gamestate.INITIAL_NUMBER_OF_TURNS - 3)
        self.game_action.decrement_turns_remaining()
        self.assertEqual(self.game_action.turns_remaining, gamestate.INITIAL_NUMBER_OF_TURNS - 4)

    # Test single location change to valid location
    def test_change_location(self):
        self.game_action.change_location("River Gardens")
        self.assertEqual(self.game_action.current_location, "River Gardens")

    # Test single location change to invalid location
    def test_change_location(self):
        self.assertEqual(self.game_action.change_location("not-a-location"), 1)

    # Test adding 1 valid item, "key"
    def test_add_to_inventory(self):
        number_of_items = len(self.game_action.current_inventory)
        item = "key"
        self.assertFalse(item in self.game_action.current_inventory)
        ret = self.game_action.add_to_inventory(item)
        self.assertEqual(len(self.game_action.current_inventory), number_of_items + 1)
        self.assertTrue(item in self.game_action.current_inventory)
        self.assertEqual(ret, 0)

    # Test removing non-existent item
    def test_remove_invalid_item_from_inventory(self):
        invalid_item = "item_does_not_exist"
        self.assertFalse(invalid_item in self.game_action.current_inventory)
        ret = self.game_action.remove_from_inventory(invalid_item)
        self.assertFalse(invalid_item in self.game_action.current_inventory)
        self.assertEqual(ret, 1)

    # Test removing valid item
    def test_remove_valid_item_from_inventory(self):
        valid_item = "key"
        self.assertFalse(valid_item in self.game_action.current_inventory)
        self.game_action.add_to_inventory(valid_item)
        self.assertTrue(valid_item in self.game_action.current_inventory)
        ret = self.game_action.remove_from_inventory(valid_item)
        self.assertEqual(ret, 0)
        self.assertFalse(valid_item in self.game_action.current_inventory)

    # Test check inventory
    def test_check_inventory(self):
        self.assertEqual(self.game_action.check_inventory("foobar"), False)
        self.assertEqual(self.game_action.check_inventory("key"), False)
        self.game_action.add_to_inventory("key")
        self.assertEqual(self.game_action.check_inventory("key"), True)
        self.assertEqual(self.game_action.check_inventory("foobar"), False)

    # Test maximum limit of inventory
    def test_maximum_limit_of_inventory(self):
        for i in range(0, gamestate.MAX_INVENTORY):
            self.assertEqual(self.game_action.add_to_inventory("rock" + str(i)), 0)
        self.assertEqual(len(self.game_action.current_inventory), gamestate.MAX_INVENTORY)
        self.assertEqual(self.game_action.add_to_inventory("bad rock"), 1)
        self.assertEqual(self.game_action.add_to_inventory("bad rock"), 1)
        self.assertEqual(self.game_action.add_to_inventory("bad rock"), 1)

    # Test adding a valid puzzle
    def test_add_to_solved_puzzles(self):
        number_of_puzzles = len(self.game_action.solved_puzzles)
        puzzle_id = 2
        puzzle_name = "Cipher"
        self.assertFalse(puzzle_id in self.game_action.solved_puzzles)
        ret = self.game_action.add_to_solved_puzzles(puzzle_id, puzzle_name)
        self.assertEqual(len(self.game_action.solved_puzzles), number_of_puzzles + 1)
        self.assertTrue(puzzle_id in self.game_action.solved_puzzles)
        self.assertEqual(self.game_action.solved_puzzles[puzzle_id], puzzle_name)
        self.assertEqual(ret, 0)

    # Test valid return of puzzle dictionary
    def test_order_of_puzzle(self):
        self.game_action.add_to_solved_puzzles(5, "puzzle five")
        self.game_action.add_to_solved_puzzles(1, "puzzle one")
        self.game_action.add_to_solved_puzzles(2, "puzzle two")
        self.assertEqual(self.game_action.solved_puzzles, {1: 'puzzle one', 2: 'puzzle two', 5: 'puzzle five'})

    # Test for solved puzzle
    def test_check_for_solved_puzzle(self):
        self.game_action.add_to_solved_puzzles(5, "puzzle five")
        self.game_action.add_to_solved_puzzles(1, "puzzle one")
        self.game_action.add_to_solved_puzzles(2, "puzzle two")
        self.assertEqual(self.game_action.check_for_solved_puzzle(1), True)
        self.assertEqual(self.game_action.check_for_solved_puzzle(2), True)
        self.assertEqual(self.game_action.check_for_solved_puzzle(3), False)
        self.assertEqual(self.game_action.check_for_solved_puzzle(4), False)
        self.assertEqual(self.game_action.check_for_solved_puzzle(5), True)
        self.assertEqual(self.game_action.check_for_solved_puzzle(100), False)

    # Test adding a valid clue
    def test_add_to_obtained_clues(self):
        number_of_clues = len(self.game_action.obtained_clues)
        clue_id = 5
        clue_text = "A glow radiates from the lake - blinding you."
        self.assertFalse(clue_id in self.game_action.obtained_clues)
        ret = self.game_action.add_to_obtained_clues(clue_id, clue_text)
        self.assertEqual(len(self.game_action.obtained_clues), number_of_clues + 1)
        self.assertTrue(clue_id in self.game_action.obtained_clues)
        self.assertEqual(self.game_action.obtained_clues[clue_id], clue_text)
        self.assertEqual(ret, 0)

    # Test valid return of clue dictionary
    def test_order_of_clues(self):
        self.game_action.add_to_obtained_clues(5, "clue five")
        self.game_action.add_to_obtained_clues(1, "clue one")
        self.game_action.add_to_obtained_clues(2, "clue two")
        self.assertEqual(self.game_action.obtained_clues, {1: 'clue one', 2: 'clue two', 5: 'clue five'})

    # Test for obtained clue
    def test_check_for_obtained_clue(self):
        self.game_action.add_to_obtained_clues(5, "clue five")
        self.game_action.add_to_obtained_clues(1, "clue one")
        self.game_action.add_to_obtained_clues(2, "clue two")
        self.assertEqual(self.game_action.check_for_obtained_clue(1), True)
        self.assertEqual(self.game_action.check_for_obtained_clue(2), True)
        self.assertEqual(self.game_action.check_for_obtained_clue(3), False)
        self.assertEqual(self.game_action.check_for_obtained_clue(4), False)
        self.assertEqual(self.game_action.check_for_obtained_clue(5), True)
        self.assertEqual(self.game_action.check_for_obtained_clue(100), False)


    # Test check_visited with invalid district_names
    def test_invalid_check_visited(self):
        with self.assertRaises(ValueError):
            self.game_action.check_visited("abc")
        with self.assertRaises(ValueError):
            self.game_action.check_visited("c i t y h a l l")   # spacing
        with self.assertRaises(ValueError):
            self.game_action.check_visited("123")               # not letters
        with self.assertRaises(ValueError):
            self.game_action.check_visited("not_a_location")    # not a location
        with self.assertRaises(ValueError):
            self.game_action.check_visited("paradise crek")     # misspelling
        with self.assertRaises(ValueError):
            self.game_action.check_visited("")                  # empty
        with self.assertRaises(ValueError):
            self.game_action.check_visited(" ")                 # space


    # Test check_visited with valid district_names
    def test_valid_check_visited(self):
        test_data =["City Hall", "city hall", "city_hall", "cityhall",
                    "Hawkins", "hawkins",
                    "Washington Heights", "washington heights", "washington_heights", "washingtonheights",
                    "Greenland Grove", "greenland grove", "greenland_grove", "greenlandgrove",
                    "Oak Square", "oak square", "oak_square", "oaksquare",
                    "Northtown", "northtown",
                    "River Gardens", "river gardens", "river_gardens", "rivergardens",
                    "Bayrock", "bayrock",
                    "Sunset Hills", "sunset hills", "sunset_hills", "sunsethills",
                    "Lemonfield", "lemonfield",
                    "Gato Springs", "gato springs", "gato_springs", "gatosprings",
                    "Webster Mountain", "webster mountain", "webster_mountain", "webstermountain",
                    "Paradise Creek", "paradise creek" ,"paradise_creek", "paradisecreek",
                    "Coltwood", "coltwood",
                    "Lake Cypress", "lake cypress", "lake_cypress", "lakecypress"]
        for d_name in test_data:
            self.assertEqual(self.game_action.check_visited(d_name), False)

        # FOR TEST ONLY: Access _visited dict directly and change all values to True for testing
        for k, v in self.game_state._visited.items():
            self.game_state._visited[k] = True

        for d_name in test_data:
            self.assertEqual(self.game_action.check_visited(d_name), True)

    # Test change_visited with valid district names
    def test_valid_check_visited(self):
        test_data =["City Hall", "city hall", "city_hall", "cityhall",
                    "Hawkins", "hawkins",
                    "Washington Heights", "washington heights", "washington_heights", "washingtonheights",
                    "Greenland Grove", "greenland grove", "greenland_grove", "greenlandgrove",
                    "Oak Square", "oak square", "oak_square", "oaksquare",
                    "Northtown", "northtown",
                    "River Gardens", "river gardens", "river_gardens", "rivergardens",
                    "Bayrock", "bayrock",
                    "Sunset Hills", "sunset hills", "sunset_hills", "sunsethills",
                    "Lemonfield", "lemonfield",
                    "Gato Springs", "gato springs", "gato_springs", "gatosprings",
                    "Webster Mountain", "webster mountain", "webster_mountain", "webstermountain",
                    "Paradise Creek", "paradise creek" ,"paradise_creek", "paradisecreek",
                    "Coltwood", "coltwood",
                    "Lake Cypress", "lake cypress", "lake_cypress", "lakecypress"]
        for d_name in test_data:
            self.assertEqual(self.game_action.check_visited(d_name), False)
            self.assertEqual(self.game_action.change_visited(d_name), 0)
            self.assertEqual(self.game_action.check_visited(d_name), True)
            # FOR TEST ONLY: Change back _visited to False
            self.game_state._visited[gamestate.District[d_name].name] = False

    # Test change_visited with invalid names
    def test_invalid_change_visited(self):
        self.assertEqual(self.game_action.change_visited("abc"), 1)
        self.assertEqual(self.game_action.change_visited("c i t y h a l l"), 1)   # spacing
        self.assertEqual(self.game_action.change_visited("123"), 1)               # not letters
        self.assertEqual(self.game_action.change_visited("not_a_location"), 1)    # not a location
        self.assertEqual(self.game_action.change_visited("paradise crek"), 1)     # misspelling
        self.assertEqual(self.game_action.change_visited(""), 1)                  # empty
        self.assertEqual(self.game_action.change_visited(" ") , 1)                # space
