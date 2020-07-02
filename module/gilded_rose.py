# -*- coding: utf-8 -*-
from enum import Enum

def is_special_item(item):
    return (SpecialItem.AGED_BRIE.value == item or
            SpecialItem.BACKSTAGE_PASS.value == item or
            SpecialItem.SULFURAS.value == item)

class SpecialItem(Enum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

MAX_QUAL = 50

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality_non_special_item(self, item):
        if item.quality > 0:
            self.decrement_quality_of(item)

    def decrement_quality_of(self, item):
        item.quality -= 1

    def increment_quality_of(self, item, by=1):
        item.quality += by

    def decrement_sell_in_of(self, item):
        item.sell_in -= 1

    def update_quality(self):
        for item in self.items:
            if item.name == SpecialItem.AGED_BRIE.value:
                self.update_quality_brie(item)
            elif item.name == SpecialItem.BACKSTAGE_PASS.value:
                self.update_quality_backstage_pass(item)
            elif item.name != SpecialItem.SULFURAS.value:
                self.update_quality_non_special_item(item)

            if item.name != SpecialItem.SULFURAS.value:
                # decrement sell in for anything except sulfuras
                self.decrement_sell_in_of(item)

            self.update_quality_for_negative_sell_in(item)

    def update_quality_brie(self, item):
        if item.quality < MAX_QUAL:
            self.increment_quality_of(item)

    def update_quality_backstage_pass(self, item):
        if item.quality < MAX_QUAL:
            if item.sell_in > 10:
                self.increment_quality_of(item, by=1)
            elif item.sell_in < 6:
                self.increment_quality_of(item, by=3)
            elif item.sell_in < 11:
                self.increment_quality_of(item, by=2)

    def update_quality_for_negative_sell_in(self, item):
        if item.sell_in < 0:
            if item.name == SpecialItem.AGED_BRIE.value:
                if item.quality < MAX_QUAL:
                    self.increment_quality_of(item, by=1)
            else:
                if item.name == SpecialItem.BACKSTAGE_PASS.value:
                    item.quality = 0
                elif item.quality > 0:
                    if item.name != SpecialItem.SULFURAS.value:
                        self.decrement_quality_of(item)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
