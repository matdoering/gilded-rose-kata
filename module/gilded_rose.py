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
                item.quality = item.quality - 1

    def update_quality(self):
        for item in self.items:
            if item.name == SpecialItem.AGED_BRIE.value or item.name == SpecialItem.BACKSTAGE_PASS.value:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == SpecialItem.BACKSTAGE_PASS.value:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            elif item.name != SpecialItem.SULFURAS.value:
                self.update_quality_non_special_item(item)

            if item.name != SpecialItem.SULFURAS.value:
                item.sell_in = item.sell_in - 1

            self.update_quality_for_negative_sell_in(item)

    def update_quality_for_negative_sell_in(self, item):
        if item.sell_in < 0:
            if item.name != SpecialItem.AGED_BRIE.value :
                if item.name != SpecialItem.BACKSTAGE_PASS.value:
                    if item.quality > 0:
                        if item.name != SpecialItem.SULFURAS.value:
                            item.quality = item.quality - 1
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
