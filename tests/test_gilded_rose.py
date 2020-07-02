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

    def test_increase_quality_by_2_if_name_eq_Backstage_and_sell_in_lt_11_and_quality_lt_50(
            self):
        # Arrange
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=0)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(2, items[0].quality)

    def test_increase_quality_by_3_if_name_eq_Backstage_and_sell_in_lt_6_and_quality_lt_50(
            self):
        # Arrange
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=0)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(3, items[0].quality)

    def test_same_quality_if_name_eq_Backstage_and_quality_gt_49(
            self):
        # Arrange
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(50, items[0].quality)

    def test_decrease_quality_by_2_if_unknown_name_and_sell_in_lt_0_and_quality_gt_1(self):
        # Arrange
        items = [Item(name="my_name", sell_in=-1, quality=2)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(0, items[0].quality)

    def test_dont_decrease_quality_if_name_sulfuras_and_sell_in_lt_0_and_quality_gt_1(self):
        # Arrange
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=2)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(2, items[0].quality)

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

    def test_negative_sell_in_aged_brie(self):
        items = [Item("Aged Brie", -1, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)

    def test_altbier_quality_degrades_twice_as_fast(self):
        items = [Item("Altbier", 20, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

    def test_altbier_degrades_twice_as_fast_after_sell_in(self):
        items = [Item("summoned Altbier", sell_in=-1, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_summoned_altbier_degrades_thrice_as_fast(self):
        items = [Item("summoned Altbier", 20, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(20-6, items[0].quality)

    def test_summoned_blub_degrades_thrice_as_fast(self):
        items = [Item("summoned blub", sell_in=20, quality=15)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(15-(1*3), items[0].quality)


if __name__ == '__main__':
    unittest.main()
