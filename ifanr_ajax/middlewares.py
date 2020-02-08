# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# from scrapy import signals


from fake_useragent import UserAgent
import logging
import random
import time


class UserAgentDownloadMiddleware(object):
    def process_request(self,request,spider):
        user_agent = UserAgent(verify_ssl=False).random
        request.headers['User-Agent'] = user_agent
        logging.warning(request.headers['User-Agent'])


class RandomDelayMiddleware(object):
    def __init__(self, delay):
        self.delay = delay

    @classmethod
    def from_crawler(cls, crawler):
        delay = crawler.spider.settings.get("RANDOM_DELAY", 10)
        if not isinstance(delay, int):
            raise ValueError("RANDOM_DELAY need a int")
        return cls(delay)

    def process_request(self, request, spider):
        delay = random.randint(0, self.delay)
        logging.warning("### 随机延时: %s s ###" % delay)
        time.sleep(delay)
