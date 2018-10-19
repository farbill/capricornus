from unittest import TestCase
from items import Item, ItemType


class TestItem(TestCase):
    def test_eq_true(self):

        itema = Item(name='itema',
                     item_type=ItemType.CRITICAL,
                     narration='Its a beautiful day in the neighborhood')
        itema2 = Item(name='itema',
                      item_type=ItemType.CRITICAL,
                      narration='Its a beautiful day in the neighborhood')
        self.assertTrue(itema == itema2)

    def test_eq_false(self):
        itema = Item(name='itema',
                     item_type=ItemType.CRITICAL,
                     narration='Its a beautiful day in the neighborhood')

        itemb = Item(name='itemb',
                     item_type=ItemType.CRITICAL,
                     narration='Its a beautiful day in the neighborhood')
        self.assertFalse(itema == itemb)
        itema = Item(name='itema',
                     item_type=ItemType.NONCRITICAL,
                     narration='Its a beautiful day in the neighborhood')

        itema2 = Item(name='itema',
                      item_type=ItemType.CRITICAL,
                      narration='Its a beautiful day in the neighborhood')
        self.assertFalse(itema == itema2)


        itema = Item(name='itema',
                     item_type=ItemType.NONCRITICAL,
                     narration='Its a beautiful day in the neighborhood')

        itema2 = Item(name='itema',
                      item_type=ItemType.NONCRITICAL,
                      narration='Im writing this code on an airplane')
        self.assertFalse(itema == itema2)

