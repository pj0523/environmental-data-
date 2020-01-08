# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class PollutionSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class PollutionDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)





from selenium import webdriver
from scrapy.http import HtmlResponse

options = webdriver.ChromeOptions()

options.binary_location = "/Applications/Browsers/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# Disable image loading and CSS

prefs = {
              'profile.default_content_setting_values': {
                'images': 2,
                'css': 2
                }
}

options.add_experimental_option('prefs', prefs)



from selenium.webdriver.support.ui import WebDriverWait


class SeleniumMiddleware(object):

   def __init__(self):
        self.browser = webdriver.Chrome(chrome_driver_binary, options=options)
        super(SeleniumMiddleware,self).__init__()



    def process_request(self, request, spider):
        if request.url != 'https://www.aqistudy.cn/historydata/':

            self.browser.get(request.url)

            try:
                # Making WebDriver  wait for a certain condition to occur
                WebDriverWait(self.browser,3).until(lambda driver: driver.find_element_by_xpath("//tbody//tr[last()]/td"))
            except:
                print(request.url)

            return HtmlResponse(url = request.url, body =self.browser.page_source,request=request, encoding='utf-8')


# in order to prevent the server for limiting oue visits, ip and request header can be changed.


# Ip change example:
# class Proxy(object):
#     def process_request(self, request, spider):
#         #对拦截到请求的url进行判断（协议头到底是http还是https）
#         #request.url返回值：http://www.xxx.com
#         h = request.url.split(':')[0]  #请求的协议头
#         if h == 'https':
#             ip = random.choice(PROXY_https)
#             request.meta['proxy'] = 'https://'+ip
#         else:
#             ip = random.choice(PROXY_http)
#             request.meta['proxy'] = 'http://' + ip
#
#
#PROXY_http = [
#     '153.180.102.104:80',
#     '119.254.94.93:56055',
# ]
# IPPOOL = [
#       '123.180.71.232: 808',
#       '59.37.18.243:3128',
#       '58.247.127.145: 53218'
#
# ]




