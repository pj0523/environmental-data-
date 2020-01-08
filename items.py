# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Day = scrapy.Field()
    AQL = scrapy.Field()
    Quality = scrapy.Field()
    PM25 = scrapy.Field()
    PM10 = scrapy.Field()
    SO2 = scrapy.Field()
    CO = scrapy.Field()
    NO2 = scrapy.Field()
    O3_8h = scrapy.Field()
