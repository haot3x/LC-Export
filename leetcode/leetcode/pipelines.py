# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

class QuestionPipeline(object):

    def __init__(self):
        pass
        # self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        # logging.debug("pipeline got an item")
        pass

class SubmissionPipeline(object):

    def __init__(self):
        pass
        # self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        # logging.debug("pipeline got an item")
        pass

    def close_spider(self, spider):
        pass
