#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import mongoengine

username = "admin"
password = "s8njgtFSqul3"
uri = "mongodb://{username}:{password}@ds161304.mlab.com:61304/cvs".format(
    username=username,
    password=password,
)
dbname = "cvs"

connect = mongoengine.connect(
    db=dbname, alias="default",
    host=uri,
)
db = connect.get_database(dbname)
c_url = db.get_collection("url")