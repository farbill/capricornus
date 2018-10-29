from unittest import TestCase

import load_save_menu
import main_menu
import os


class LoadMenuTestCase(TestCase):
    def setUp(self):
        #self.game_state = gamestate.GameState()      # initialize instance of GameState class
        pass

    # def tearDown(self):
    #     print("teardown -- ")

    def test_1(self):
        load_save_menu.load_menu()
        pass