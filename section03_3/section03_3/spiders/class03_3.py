# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test5'
    allowed_domains = ['w3schools.com']
    start_urls = ['http://www.w3schools.com/']

    def parse(self, response):
        for n, text in enumerate(response.css('nav#mySidenav').xpath('./div/a/text()').getall()):
            yield {
                'number': n,
                'title': text,
            }
