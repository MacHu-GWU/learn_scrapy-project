# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class QuotesbotPipeline(object):
#     def process_item(self, item, spider):
#         return item


from learn_mongodb.db_test import col


class MongoPipeline(object):
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls()
#     
#     def open_spider(self, spider):
#         pass
# 
#     def close_spider(self, spider):
#         pass
    
    def process_item(self, item, spider):
        col.insert(dict(item))
        return item 
