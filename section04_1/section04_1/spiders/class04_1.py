# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test8'
    allowed_domains = ['globalvoices.org']
    start_urls = ['https://globalvoices.org/']

    def parse(self, response):
        for i, title in enumerate(
                response.css('div.post-summary-content').xpath('.//h3[@class="post-title"]/a/@title').getall(),
                start=1):
            yield {
                'number': i,
                'title': title,
            }
