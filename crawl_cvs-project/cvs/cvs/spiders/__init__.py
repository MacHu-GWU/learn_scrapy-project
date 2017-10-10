#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import scrapy
from crawl_cvs.db import c_url
from crawl_cvs.model import Type
from crawl_cvs.html_parser import htmlparser
from crawl_cvs.url_builder import urlbuilder
from cvs import items


def mark_finished(url):
    href = url.replace("https://www.cvs.com", "", 1)
    c_url.update({"_id": href}, {"$set": {"finished": True}})


class CVSSpider(scrapy.Spider):
    name = "cvs"
    allowed_domains = [
        "cvs.com",
    ]

    def start_requests(self):
        # c_url.remove({})

        doc = {"_id": "/store-locator/cvs-pharmacy-locations",
               "type": Type.root_url,
               "finished": False}
        try:
            c_url.insert(doc)
        except:
            pass

        filters = {"finished": False}
        wanted = {"_id": True}
        for doc in c_url.find(filters, wanted):
            href = doc["_id"]
            url = urlbuilder.join_all(href)
            yield scrapy.Request(url)


    def parse(self, response):
        # it is a state url list page
        if response.url.count("/") == 4:
            state_url_list = htmlparser.get_state_url(response.text)
            for state_url in state_url_list:
                yield items.StateUrlItem(**state_url.to_dict())

            mark_finished(response.url)

            for state_url in state_url_list:
                url = urlbuilder.join_all(state_url.href)
                yield scrapy.Request(url)

        # it is a city url list page
        elif response.url.count("/") == 5:
            city_url_list = htmlparser.get_city_url(response.text)
            for city_url in city_url_list:
                yield items.CityUrlItem(**city_url.to_dict())

            mark_finished(response.url)
