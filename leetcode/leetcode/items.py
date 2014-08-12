# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Question(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    add_date = scrapy.Field()
    ac_rates = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()

class Submission(scrapy.Item):
    code = scrapy.Field()
    language = scrapy.Field()
