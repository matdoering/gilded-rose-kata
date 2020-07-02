# -*- coding: utf-8 -*-
import unittest

from module.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        """Name of item as expected."""
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_quality_is_positive(self):
        """Quality does not go below 0."""
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_degrades(self):
        """Quality must degrade by one 1 for every passing day."""
        items = [Item("foo", 2, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_sell_in_degrades(self):
        """Quality must degrade by one 1 for every passing day."""
        items = [Item("foo", 2, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)

    def test_selldate_passed_quality_degrades(self):
        """Quality degrades twice as fast once the sell_in date has passed."""
        pass


if __name__ == '__main__':
    unittest.main()
