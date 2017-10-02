#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from crawl_cvs import htmlparser
from cvs.items import CvsUrl

class CVSSpider(scrapy.Spider):
    name = "cvs"
    start_urls = [
        "https://www.cvs.com/store-locator/cvs-pharmacy-locations",
    ]
    
    def parse(self, response):
        if response.url.count("/") == 4:
            state_url_list = htmlparser.get_state_url(response.text)
            for state_url in state_url_list:
                yield CvsUrl(_id=state_url.href, name=state_url.name)
            
            for state_url in state_url_list:
                yield scrapy.Request(response.urljoin(state_url.href))
            
        elif response.url.count("/") == 5:
            city_url_list = htmlparser.get_city_url(response.text)
            for state_url in city_url_list:
                yield CvsUrl(_id=state_url.href, name=state_url.name)
        