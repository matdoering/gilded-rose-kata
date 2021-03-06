# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

MAX_QUAL = 50
DECREASE_RATE = 1  # base decrease rate

def is_summoned_item(item):
    return item.name.startswith("summoned ")

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality_non_special_item(self, item):
        if item.sell_in < 0:
            self.decrement_quality_of(item, by=DECREASE_RATE*2)
        else:
            self.decrement_quality_of(item)

    def decrement_quality_of(self, item, by=DECREASE_RATE):
        if is_summoned_item(item):
            # summoned items degrade thrice as fast
            by *= 3
        if (item.quality - by) > 0:
            item.quality -= by
        else:
            item.quality = 0

    def increment_quality_of(self, item, by=1):
        if item.quality <= (MAX_QUAL - by):
            item.quality += by
        else:
            item.quality = MAX_QUAL

    def decrement_sell_in_of(self, item):
        item.sell_in -= 1

    def update_quality_sulfuras(self, item):
        # no changes for sulfuras
        pass

    def update_quality_altbier(self, item):
        base_decrement = DECREASE_RATE*2
        if item.sell_in < 0:
            self.decrement_quality_of(item, by=base_decrement*2)
        else:
            self.decrement_quality_of(item, base_decrement)

    def update_quality(self):
        for item in self.items:
            if isinstance(item, AgedBrie):
                self.decrement_sell_in_of(item)
                self.update_quality_brie(item)
            elif isinstance(item, BackstageTicket):
                self.decrement_sell_in_of(item)
                self.update_quality_backstage_pass(item)
            elif isinstance(item, Sulfuras):
                self.update_quality_sulfuras(item)
            elif isinstance(item, Altbier):
                self.decrement_sell_in_of(item)
                self.update_quality_altbier(item)
            else:
                self.decrement_sell_in_of(item)
                self.update_quality_non_special_item(item)

    def update_quality_brie(self, item):
        self.increment_quality_of(item)
        if item.sell_in < 0:
            self.increment_quality_of(item, by=1)

    def update_quality_backstage_pass(self, item):
        if item.sell_in < 0:
            # pass reduces value after the concert
            item.quality = 0
        elif item.sell_in > 10:
            self.increment_quality_of(item, by=1)
        elif item.sell_in < 6:
            self.increment_quality_of(item, by=3)
        elif item.sell_in < 11:
            self.increment_quality_of(item, by=2)


class Item(ABC):

    @abstractmethod
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Altbier(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

class AgedBrie(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

class BackstageTicket(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)


class Sulfuras(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)


class DefaultItem(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)