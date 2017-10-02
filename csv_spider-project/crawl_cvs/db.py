#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

client = pymongo.MongoClient()
db = client.get_database("cvs")
c_url = db.get_collection("url")
c_store = db.get_collection("store")