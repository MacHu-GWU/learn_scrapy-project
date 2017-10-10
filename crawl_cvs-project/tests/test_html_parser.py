#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from crawlib import requests_spider as spider
from crawl_cvs.html_parser import htmlparser


# def test_get_state_url():
#     url = "https://www.cvs.com/store-locator/cvs-pharmacy-locations"
#     html = spider.get_html(url, encoding="utf8", timeout=5)
#     for state_url in htmlparser.get_state_url(html)[:3]:
#         print(state_url)
#
#
# def test_get_city_url():
#     url = "https://www.cvs.com/store-locator/cvs-pharmacy-locations/California"
#     html = spider.get_html(url, encoding="utf8", timeout=5)
#     for city_url in htmlparser.get_city_url(html)[:3]:
#         print(city_url)


def test_get_store_url():
    url = "https://www.cvs.com/store-locator/cvs-pharmacy-locations/California/Los-Angeles"
    html = spider.get_html(url, encoding="utf8", timeout=5)
    print(html)
    # for store_url in htmlparser.get_store_url(html)[:3]:
    #     print(store_url)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
