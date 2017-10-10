# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from crawl_cvs.model import (
    StateUrl, CityUrl, StoreUrl,
)


class BaseUrlItem(scrapy.Item):
    href = scrapy.Field()
    type = scrapy.Field()
    finished = scrapy.Field()

    document = None

    def to_doc(self):
        return self.document(**dict(self))


class StateUrlItem(BaseUrlItem):
    name = scrapy.Field()

    document = StateUrl


class CityUrlItem(BaseUrlItem):
    name = scrapy.Field()

    document = CityUrl


class StoreUrlItem(BaseUrlItem):
    address = scrapy.Field()
    phone = scrapy.Field()
    store_id = scrapy.Field()

    document = StoreUrl
