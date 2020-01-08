# -*- coding: utf-8 -*-
import scrapy


class PollutionSpider(scrapy.Spider):
    name = 'pollution'
    allowed_domains = ['https://www.aqistudy.cn/historydata/']
    start_urls = ['https://www.aqistudy.cn/historydata//']
    base = "https://www.aqistudy.cn/historydata/"

    def parse(self, response):

        cities_url = cities = response.xpath(
            "//div[@class='bottom']//li/a/@href").extract()

        for city_url in cities_url:
            yield request(url=self.base + city_url, callback=parse_url)

    def parse_url(self, response):
        monthes_url = response.xpath(
            "//tbody//tr/td[@align ='center']/a/@href").extract()
        for month_url in monthes_url:
            yield request(url=self.base + month_url, callback=parse_items)

    def parse_items(self, response):
        pass
