#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from crawl_cvs.model import StoreUrl
from scrapy.exceptions import DropItem

col = StoreUrl.col()


class CvsMongoDBSaver(object):
    def __init__(self):
        self.id_seen = set([doc["_id"] for doc in col.find({}, {"_id": True})])

    def process_item(self, item, spider):
        if item["href"] in self.id_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            try:
                item.to_doc().save()
                self.id_seen.add(item["href"])
            except Exception as e:
                print(e)
        return item
