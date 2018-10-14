from unittest import TestCase

import main_menu
import os


class LoadMenuTestCase(TestCase):
    def setUp(self):
        #self.game_state = gamestate.GameState()      # initialize instance of GameState class
        pass

    # def tearDown(self):
    #     print("teardown -- ")

    def test_1(self):
        main_menu.load_menu()
        pass