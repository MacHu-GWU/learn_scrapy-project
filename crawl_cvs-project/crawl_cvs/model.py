#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mongoengine
import mongoengine_mate

try:
    from .db import connect
except:
    from crawl_cvs.db import connect


class Type(object):
    root_url = 0
    state_url = 1
    city_url = 2
    store_url = 3


class Cols(object):
    state_url = "url"
    city_url = "url"
    store_url = "url"


class BaseUrlDocument(mongoengine_mate.ExtendedDocument):
    href = mongoengine.StringField(primary_key=True)
    finished = mongoengine.BooleanField(default=False)

    meta = {
        "abstract": True,
    }

    @classmethod
    def col_name(cls):
        return cls.col().name


class StateUrl(BaseUrlDocument):
    """

    Example: https://www.cvs.com/store-locator/cvs-pharmacy-locations/California
    """
    name = mongoengine.StringField()
    type = mongoengine.IntField(default=Type.state_url)

    meta = {
        "collection": Cols.state_url,
    }

    @property
    def key(self):
        return self.href.split("/")[-1]


class CityUrl(BaseUrlDocument):
    """
    Example: https://www.cvs.com/store-locator/cvs-pharmacy-locations/California/Los-Angeles
    """
    name = mongoengine.StringField()
    type = mongoengine.IntField(default=Type.city_url)

    meta = {
        "collection": Cols.city_url,
    }

    @property
    def key(self):
        return self.href.split("/")[-1]


class StoreUrl(BaseUrlDocument):
    """
    Example: https://www.cvs.com/store-locator/cvs-pharmacy-address/8000+West+Sunset+Boulevard-Los+Angeles-CA-90046/storeid=10791
    """
    address = mongoengine.StringField()
    phone = mongoengine.StringField()
    store_id = mongoengine.StringField()
    type = mongoengine.IntField(default=Type.store_url)

    meta = {
        "collection": Cols.store_url,
    }
