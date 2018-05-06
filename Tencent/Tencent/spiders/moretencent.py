# -*- coding: utf-8 -*-
import scrapy
from ..items import MoreTencentItem
import re


class TencentSpider(scrapy.Spider):
	name = 'moretencent'
	allowed_domains = ['tencent.com']
	start_urls = ['http://hr.tencent.com/position.php?&start=0#a/']

	def parse(self, response):
		sel_list=response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
		for url in sel_list:
			url=url.xpath('./td[1]/a/@href').extract_first()
			main_url="http://hr.tencent.com/"
			link_url=main_url+url
			yield scrapy.Request(link_url,callback=self.parse_more)

		if len(response.xpath('//a[@class="noactive" and @id="next"]' )) == 0:
			url=response.xpath('//a[@id="next"]/@href').extract_first()
			main_url="http://hr.tencent.com/"
			next_url=main_url+url

			yield scrapy.Request(next_url,callback=self.parse)


	def parse_more(self,response):
		job=MoreTencentItem()
		job['positionname']=response.xpath('//td[@id="sharetitle"]/text()').extract_first()
		job['positiontype']=response.xpath('//tr[@class="c bottomline"]/td[2]/text()').extract_first()
		job['pepolenum']=response.xpath('//tr[@class="c bottomline"]/td[3]/text()').extract_first()
		job['city']=response.xpath('//tr[@class="c bottomline"]/td[1]/text()').extract_first()
		job['duty']=response.xpath('//tr[3]//ul').extract_first()
		job['demand']=response.xpath('//tr[4]//ul').extract_first()
		yield job