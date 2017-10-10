#!/usr/bin/env python
# -*- coding: utf-8 -*-

import crawlib
try:
    from . import model
except: # pragma: no cover
    from crawl_cvs import model


class CvsHtmlParser(crawlib.BaseHtmlParser):
    domain = "https://www.cvs.com/"

    def get_state_url(self, html):
        """
        Example url: https://www.cvs.com/store-locator/cvs-pharmacy-locations

        :param html:
        :return:
        """
        state_url_list = list()

        soup = self.to_soup(html)
        for div in soup.find_all("div", class_="states"):
            for a in div.find_all("a"):
                state_url = model.StateUrl(
                    href=a["href"],
                    name=a.text.strip(),
                )
                state_url_list.append(state_url)

        return state_url_list

    def get_city_url(self, html):
        """
        Example url: https://www.cvs.com/store-locator/cvs-pharmacy-locations/California

        :param html:
        :return:
        """
        city_url_list = list()

        soup = self.to_soup(html)
        for div in soup.find_all("div", class_="states"):
            for a in div.find_all("a"):
                city_url = model.CityUrl(
                    href=a["href"],
                    name=a.text.strip().split("(")[0].strip(),
                )
                city_url_list.append(city_url)

        return city_url_list

    def get_store_url(self, html):
        """
        Example url: https://www.cvs.com/store-locator/cvs-pharmacy-locations/California/Los-Angeles

        :param html:
        :return:
        """
        store_url_list = list()

        soup = self.to_soup(html)
        for div in soup.find_all("div"):
            try:
                print(div.attrs)
            except:
                pass
        # for div in soup.find_all("div", class_=["stores", "wrap"]):
        #     print(div)
        return list()

htmlparser = CvsHtmlParser()
