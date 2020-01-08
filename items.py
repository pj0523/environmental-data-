# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PollutionItem(scrapy.Item):
    Day = scrapy.Field()
    AQI = scrapy.Field()
    Range = scrapy.Field()
    Quantity = scrapy.Field()
    PM2_5 = scrapy.Field()
    PM10 = scrapy.Field()
    SO2 = scrapy.Field()
    CO = scrapy.Field()
    NO2 = scrapy.Field()
    O3 = scrapy.Field()
    CityName = scrapy.Field()



