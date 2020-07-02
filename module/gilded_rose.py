# -*- coding: utf-8 -*-
from enum import Enum

class SpecialItem(Enum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

class GildedRose(object):

    def __init__(self, items):
        self.items = items


    def update_quality_non_special_item(self, item):
        if item.quality > 0:
            self.decrement_quality(item)

    def decrement_quality(self, item):
        item.quality -= 1

    def increment_quality(self, item):
        item.quality += 1

    def decrement_sell_in(self, item):
        item.sell_in -= 1

    def update_quality(self):
        for item in self.items:
            if item.name == SpecialItem.AGED_BRIE.value or item.name == SpecialItem.BACKSTAGE_PASS.value:
                self.update_quality_brie_or_backstage(item)
            elif item.name != SpecialItem.SULFURAS.value:
                self.update_quality_non_special_item(item)

            if item.name != SpecialItem.SULFURAS.value:
                self.decrement_sell_in(item)

            self.update_quality_for_negative_sell_in(item)

    def update_quality_brie_or_backstage(self, item):
        if item.quality < 50:
            self.increment_quality(item)
            if item.name == SpecialItem.BACKSTAGE_PASS.value and item.quality < 50:
                if item.sell_in < 11:
                    self.increment_quality(item)
                if item.sell_in < 6:
                    self.increment_quality(item)

    def update_quality_for_negative_sell_in(self, item):
        if item.sell_in < 0:
            if item.name != SpecialItem.AGED_BRIE.value :
                if item.name != SpecialItem.BACKSTAGE_PASS.value:
                    if item.quality > 0:
                        if item.name != SpecialItem.SULFURAS.value:
                            self.decrement_quality(item)
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
