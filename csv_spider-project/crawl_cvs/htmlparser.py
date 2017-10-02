#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bs4
from crawlib.htmlparser import BaseHtmlParser
from sfm.nameddict import Base

class StateUrl(Base):
    pass

class CityUrl(Base):
    pass

class StoreUrl(Base):
    pass

class HtmlParser(BaseHtmlParser):
    def get_state_url(self, html):
        state_list = list()
        
        soup = self.get_soup(html)
        for div in soup.find_all("div", class_="states"):
            for a in div.find_all("a"):
                state = StateUrl(
                    href=a["href"],
                    name=a.text.strip(),
                )
                state_list.append(state)
        
        return state_list
    
    def get_city_url(self, html):
        city_list = list()
        
        soup = self.get_soup(html)
        for div in soup.find_all("div", class_="states"):
            for a in div.find_all("a"):
                city = CityUrl(
                    href=a["href"],
                    name=a.text.strip().split("(")[0].strip(),
                )
                city_list.append(city)
        
        return city_list
        
    
htmlparser = HtmlParser()

if __name__ == "__main__":
    from dataIO.textfile import read, write
    from pathlib_mate import Path
    from crawlib.spider import spider
    from superjson import json
    from pprint import pprint
    
#     def pprint(data):
#         print(json.dumps(data, pretty=True))
    
    _dir = "testhtml"
    
    def get_test_data():
        url_file_list = [
            ("https://www.cvs.com/store-locator/cvs-pharmacy-locations", "state_list.html"),
            ("https://www.cvs.com/store-locator/cvs-pharmacy-locations/California", "city_list.html"),
            ("https://www.cvs.com/store-locator/cvs-pharmacy-locations/California/Los-Angeles", "store_list.html"),
        ]
        for url, file in url_file_list:
            p = Path(_dir, file)
            if not p.exists():
                html = spider.get_html(url)
                write(html, p.abspath)
        
    get_test_data()
    
#     html = read(Path(_dir, "state_list.html").abspath)
#     pprint(htmlparser.get_state_url(html))
    
    html = read(Path(_dir, "city_list.html").abspath)
    pprint(htmlparser.get_city_url(html))
    