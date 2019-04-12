# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 导入
import scrapy
from scrapy.pipelines.images import ImagesPipeline
# class SotuPipeline(object):
#     def process_item(self, item, spider):
#         return item

class SotuPipeline(ImagesPipeline):
    # 重写ImagesPipeline中的方法
    def get_media_requests(self, item, info):
        #图片连接交给调度器
        yield scrapy.Request(item['img_link'])

    # def process_item(self, item, spider):
    #     return item
