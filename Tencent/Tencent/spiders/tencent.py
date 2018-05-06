# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem
from scrapy.linkextractors import LinkExtractor


class TencentSpider(scrapy.Spider):
	name = 'tencent'
	allowed_domains = ['tencent.com']
	start_urls = ['http://hr.tencent.com/position.php?&start=0#a/']

	def parse(self, response):
		sel_list=response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
		for sel in sel_list:
			job=TencentItem()
			job['positionname']=sel.xpath('./td[1]/a/text()').extract_first()
			job['positiontype']=sel.xpath('./td[2]/text()').extract_first()
			job['pepolenum']=sel.xpath('./td[3]/text()').extract_first()
			job['city']=sel.xpath('./td[4]/text()').extract_first()
			job['publishtime']=sel.xpath('./td[5]/text()').extract_first()
			yield job

		if len(response.xpath('//a[@class="noactive" and @id="next"]' )) == 0:
			url=response.xpath('//a[@id="next"]/@href').extract_first()
			main_url="http://hr.tencent.com/"
			next_url=main_url+url

			yield scrapy.Request(next_url,callback=self.parse)
