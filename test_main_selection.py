from unittest import TestCase
from main_menu import *


class TestMainSelection(TestCase):
    def test_main_selection(self):

        # inputs to be recognized as valid
        list_one = [1, "1", "new", "new game", "1. new game", "start", "begin", "go"]
        list_two = [2, "2", "load", "load game", "2. load game", "continue"]
        list_three = [3, "3", "exit", "quit", "exit game", "quit game", "3. exit", "bye"]

        for i in list_one:
            self.assertEqual(main_selection(i), 1, "Inputs for choice 1")

        for j in list_two:
            self.assertEqual(main_selection(j), 2, "Inputs for choice 2")

        for k in list_three:
            self.assertEqual(main_selection(k), 3, "Inputs for choice 3")

