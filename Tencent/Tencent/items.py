# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
	positionname=scrapy.Field()
	positiontype=scrapy.Field()
	pepolenum=scrapy.Field()
	city=scrapy.Field()
	publishtime=scrapy.Field()

class MoreTencentItem(scrapy.Item):
	positionname=scrapy.Field()
	positiontype=scrapy.Field()
	pepolenum=scrapy.Field()
	city=scrapy.Field()
	duty=scrapy.Field()
	demand=scrapy.Field()
