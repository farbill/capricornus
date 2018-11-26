from unittest import TestCase
from nlp import NLP

class TestNLP(TestCase):
    def setUp(self):
        self.NLP = NLP()

    def test_translate_whitespace(self):
        original = '   look    hobo    '
        test = 'look hobo'
        translated = self.NLP.translate(original)
        self.assertEqual(test, translated)

    def test_eat_mushroom(self):
        original = 'eat mushroom'
        translated = self.NLP.translate(original)
        self.assertEqual(translated, translated)

    def test_translate_whitespace_2(self):
        original = 'look  hobo'
        test = 'look hobo'
        translated = self.NLP.translate(original)
        self.assertEqual(test, translated)

    def test_translate_verbs(self):
        original = '   view    hobo    '
        test = 'look hobo'
        translated = self.NLP.translate(original)
        self.assertEqual(test, translated)

    def test_translate_verbs_2(self):
        original = 'view dog'
        test = 'look dog'
        translated = self.NLP.translate(original)
        self.assertEqual(test, translated)

    def test_translate_2(self):
        original = 'eat hobo'
        test = 'eat hobo'
        translated = self.NLP.translate(original)
        self.assertEqual(test, translated)

    def test_remove_preps(self):
        original = '   view the about    hobo    '
        test = 'look hobo'
        translated = self.NLP.translate(original)
        self.assertEqual(test, translated)

    def test_remove_articles(self):
        original = '   view a albatross    '
        test = 'look albatross'
        translated = self.NLP.translate(original)
        self.assertEqual(test, translated)
