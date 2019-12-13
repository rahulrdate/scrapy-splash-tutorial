# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JetbrainsItem(scrapy.Item):
    linkText = scrapy.Field()
    linkUrl = scrapy.Field()
    isExpandable = scrapy.Field()