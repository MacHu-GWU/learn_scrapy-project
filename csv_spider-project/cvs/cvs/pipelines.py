#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from crawl_cvs.db import client, c_url


class CvsMongoDBSaver(object):
    def process_item(self, item, spider):
        try:
            c_url.insert(dict(item))
        except Exception as e:
            print(e)
        return item


class CvsCrawledUrlFilter(RFPDupeFilter):
    def request_seen(self, request):
        href = request.url.replace("https://www.cvs.com", "")
        if c_url.find_one({"_id": href}):
            return True