# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test3'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        url를 순회해보자
        :param response:
        :return: Request
        """
        # for url in response.css('div.post-item > div > a::attr("href")').getall():
        #     print(url)
        # print('-------------------------------------------------------------------')
        # for url in response.xpath('//div[@class="post-item"]/div/a/@href').getall():
        #     print(url)

        for url in response.css('div.post-item > div > a::attr("href")').getall():
            yield scrapy.Request(response.urljoin(url), callback=self.parse_title)

    def parse_title(self, response):
        """
        상세 페이지 -> 타이틀 추출
        :param response:
        :return: Text
        """
        contents = response.css('div.post-body > span > p::text').getall()[:5]
        yield {
            'contents': ''.join(contents),
        }
