# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class PollutionPipeline(object):
#     def process_item(self, item, spider):
#         return item




import codecs
import json
import os
# import MySQLdb


# class ArticlespiderPipelinesobject():
#     def process_item(self, item, spider):
#         return item

# class JsonWithEncodingPipeline(object):
#      def __init__(self):
#          self.file = codecs.open("article.json", "w",  encoding="utf-8")
#      def process_item(self, item, spider):
#          lines = json.dumps(dict(item), ensure_ascii=False)+"\n"
#          self.file.write(lines)
#          return item
#
#      def spider_close(self,spider):
#          self.file.close()

# class JSONPipeline(object):
#     """
#         导出JSON格式
#     """
#     def __init__(self):
#         self.file = None
#         self.csvpath = os.path.dirname(__file__) + '/spiders/output'
#
#     def process_item(self, item, spider):
#         self.file = codecs.open('%s/%s_items.json' % (self.csvpath, spider.name), 'a', encoding='utf-8')
#         line = json.dumps(dict(item), ensure_ascii=False) + '\n'
#         self.file.write(line)
#         # return item
#
#     def spider_closed(self, spider):
#         self.file.close()


import codecs

class JsonWithEncoding(object):

   def __init__(self):
#use codecs to open files avoiding encoding/ decoding problems.
   def process_item(self,item,spider):
       lines = json.dumps(dict(item),ensure_ascii=False)+"\n"
       print(lines)
       self.file.write(lines)

       return item

   def spider_closed(self,spider):
        self.file.close()
