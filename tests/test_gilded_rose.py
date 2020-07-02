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

    def test_bar_with_quality(self):
        """Name of item as expected."""
        items = [Item("bar", -1, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("bar", items[0].name)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)

    def test_aged_backstage_passes_to_a_TAFKAL80ETC_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)

    def test_sulfuras_hand_of_ragnaros(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)

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
        items = [Item("foo", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_never_above_50(self):
        """Quality does not increase beyond 50."""
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_never_decreases_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 39)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(39, items[0].quality)

    def test_sulfuras_never_has_to_be_sold(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 39)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)

    def test_backstage_passes_qual_increases(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 39)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreater(items[0].quality, 39)

    def test_backstage_quality_increases_by_two_at_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_backstage_quality_increases_by_three_at_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)

    def test_backstage_quality_is_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_sell_in_can_be_negative(self):
        """sell_in does not go below 0."""
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)

    def test_printout(self):
        print(Item("foo", 0, 0))

    def test_brie_increases_quality(self):
        items = [Item("Aged Brie", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 1)

if __name__ == '__main__':
    unittest.main()
