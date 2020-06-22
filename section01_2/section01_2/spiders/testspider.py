# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['https://scrapinghub.com/']

    def parse(self, response):
        pass
