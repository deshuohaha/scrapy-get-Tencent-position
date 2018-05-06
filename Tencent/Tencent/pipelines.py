# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy import Item
from bs4 import BeautifulSoup
class TencentPipeline(object):
	
	def process_item(self, item, spider):
		duty=str(item['duty'])
		duty1=BeautifulSoup(duty,"html.parser")
		duty2=[]
		for link in duty1.find_all('li'):
			duty2.append(link.string)
		duty=str(duty2)
		item['duty']='\n工作职责：\n%s'%duty

		demand=str(item['demand'])
		demand1=BeautifulSoup(demand,"html.parser")
		demand2=[]
		for link in demand1.find_all('li'):
			demand2.append(link.string)
		demand=str(demand2)
		item['demand']='\n工作要求：\n%s'%demand
		return item

class MongoDBPipeline(object):
	def open_spider(self,spider):
		db_uri=spider.settings.get('MONGODB_URI','mongodb://localhost:27017')
		db_name=spider.settings.get('MONGODB_DB_NAME','scrapy_default')

		self.db_client=MongoClient('mongodb://localhost:27017')
		self.db=self.db_client[db_name]

	def close_spider(self,spider):
		self.db_client.close()
	
	def process_item(self,item,spider):
		self.insert_db(item)
		return item

	def insert_db(self,item):
		if isinstance(item,Item):
			item=dict(item)

		self.db.books.insert_one(item)