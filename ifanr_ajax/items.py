# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IfanrAjaxItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    pub_time = scrapy.Field()
    title = scrapy.Field()
    post_url = scrapy.Field()
    cover_image = scrapy.Field()
    category = scrapy.Field()
    content = scrapy.Field()

