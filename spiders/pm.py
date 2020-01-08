# -*- coding: utf-8 -*-
# from scrapy_redis.spiders import RedisSpider

import scrapy
from pollution.items import PollutionItem


class PmSpider(scrapy.Spider):
    name = 'pm'

    def start_requests(self):

       url = 'https://www.aqistudy.cn/historydata/'
       yield scrapy.Request(url=url, callback=self.parse_cities_url)

    def parse_cities_url(self,response):

        cities = response.xpath("//div[@class='all']//a/text()").extract()

        for city in cities:
            self.logger.info('Parse cities function called on %s', response.url)

            city_url = "https://www.aqistudy.cn/historydata/monthdata.php?city=" + city

            yield scrapy.Request(url=city_url, meta={"CityName":city},callback=self.parse_cities_month)
            self.logger.info('Parse city function called on %s', city)
            self.logger.info('Parse City_url called on %s',city_url)


    def parse_cities_month(self,response):
        # self.logger.info('Parse month function called on %s', response.url)

        # 传递CityName
        city = response.meta.get("CityName")
        self.logger.info('Parse month function called on %s', city)

        city_months = response.xpath("//tbody//td//a/@href").extract()
        for city_month in city_months:
            self.logger.info('Parse function called on %s', city_month)
            city_month_url = "https://www.aqistudy.cn/historydata/" + city_month
            yield scrapy.Request(url =city_month_url,meta={"CityName":city},callback=self.parse_day)



    def parse_day(self, response):

        information = response.xpath("//tbody//tr[position()>1]")
        CityName = response.meta.get("CityName")
        for detail in information:
            item = PollutionItem()
            item["CityName"] = CityName
            item["Day"] = detail.xpath(".//td//text()").extract()[0].strip()
            item["AQI"] = detail.xpath(".//td//text()").extract()[1].strip()

            item["PM2_5"] = detail.xpath(".//td//text()").extract()[3].strip()
            item["PM10"] = detail.xpath(".//td//text()").extract()[4].strip()
            item["SO2"] = detail.xpath(".//td//text()").extract()[5].strip()
            item["CO"] = detail.xpath(".//td//text()").extract()[6].strip()
            item["NO2"] = detail.xpath(".//td//text()").extract()[7].strip()
            item["O3"] = detail.xpath(".//td//text()").extract()[8].strip()
            yield item



