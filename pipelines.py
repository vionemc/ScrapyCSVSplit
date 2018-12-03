# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter

import datetime

class SplitPipeline(object):

    def __init__(self, stats):
    	self.stats = stats
    	self.base_filename = "result/amazon_{}.csv"
    	self.next_split = self.split_limit = 50000
    	self.create_exporter()  

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def create_exporter(self):
		now = datetime.datetime.now()
		datetime_stamp = now.strftime("%Y%m%d%H%M")
		self.file = open(self.base_filename.format(datetime_stamp),'w+b')
		self.exporter = CsvItemExporter(self.file)
		self.exporter.start_exporting()       

    def process_item(self, item, spider):    	
    	if (self.stats.get_value('item_scraped_count') >= self.next_split):
    		self.next_split += self.split_limit
    		self.exporter.finish_exporting()
    		self.file.close()
    		self.create_exporter()
        self.exporter.export_item(item)
        return item