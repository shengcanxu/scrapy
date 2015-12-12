# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WoshipmItem(scrapy.Item):
    title = scrapy.Field()
    updateTime = scrapy.Field()
    reads = scrapy.Field()
