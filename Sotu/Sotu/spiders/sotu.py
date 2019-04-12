# -*- coding: utf-8 -*-
import json
from urllib import parse

import scrapy
from Sotu.items import SotuItem

class SotuSpider(scrapy.Spider):
    name = 'sotu'
    allowed_domains = ['image.so.com']
    # start_urls = ['http://image.so.com/']


    # 重写start_request()方法，自定义url地址和解析方法
    # 不一定非要用parse函数
    def start_requests(self):
        # 1拼接url地址
        baseurl = 'http://image.so.com/zj?'
        for i in range(0,91,30):
            params = {
                'ch':'beauty',
                'sn':str(i),
                'listtype':'new',
                'temp':'1'
            }
            url = baseurl+parse.urlencode(params)

        # 构造请求，交给调度器
        yield scrapy.Request(url,callback=self.parse_so)

    # def parse(self, response):
    #     pass


    # 重写parse
    def parse_so(self, response):
        # 获取相应内容
        html = response.text
        # 内容为json,转为python数据类型
        html = json.loads(html)
        for img in html['list']:
            # 获取item对象
            item = SotuItem()
            item['img_link'] = img['qhimg_url']
            yield item


