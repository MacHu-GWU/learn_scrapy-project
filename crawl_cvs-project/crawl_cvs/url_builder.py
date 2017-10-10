#!/usr/bin/env python
# -*- coding: utf-8 -*-

import crawlib


class CvsUrlBuilder(crawlib.BaseUrlBuilder):
    domain = "https://www.cvs.com/"


urlbuilder = CvsUrlBuilder()
