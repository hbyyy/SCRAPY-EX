# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """

        :param response:
        :return: Title Text
        """

        # 2가지 (CSS Selector, Xpath)
        # method
        #  하나만 - 전체
        # get() - getall(), extract() - extract_first()

        # css selector 사용
        print(response.css('div.post-header h2 a::text').getall())

        # xpath 사용
        print(response.xpath('//div[@class="post-header"]/h2/a/text()').extract())

        for i, text in enumerate(response.css('div.post-header h2 a::text').getall()):
            # return Type : Request, BaseItem, Dict, None 필수!
            yield {
                'number': i,
                'title': text,
            }
