# -*- coding: utf-8 -*-
import scrapy

from ..items import ItArticle


class TestSpider(scrapy.Spider):
    name = 'test6'
    allowed_domains = ['itnews.com']
    start_urls = ['https://itnews.com/']

    def parse(self, response):
        """

        :param response:
        :return: Request
        """
        for url in response.css('section.bodee div.newsfeed').xpath(
                './div[@class="news-item"]/div[@class="hed"]//a/@href').getall():
            yield scrapy.Request(response.urljoin(url), self.parse_article)

    def parse_article(self, response):
        """

        :param response:
        :return: Items
        """
        item = ItArticle()

        item['title'] = response.xpath('//h1[@itemprop="headline"]/text()').get()
        item['image_url'] = response.xpath('//img[@itemprop="contentUrl"]/@data-original').get()
        item['contents'] = ''.join(response.xpath('//div[@itemprop="articleBody"]/p/text()').getall()).strip()

        print(dict(item))
        yield item
