# -*- coding: utf-8 -*-
import scrapy

from ..items import ItArticle

# Scrapy Feed Export 실습

"""
 출력 형식
    JSON, JSON Lines
    CSV
    XML, Pickle, Marshal
    
 저장 위치
    Local File System (My PC)
    FTP - (Server)
    S3 - (AWS)
    기본 콘솔
    
 방법
    1. 커맨드 이용
        ((--output, -o) , (--output-format, -t)) 
        옵션 설정 예 -> --set=FEED_EXPORT_INDENT = 2
        
    2. settings.py 에 설정
        자동으로 저장 (파일명, 형식, 위치)
"""

class TestSpider(scrapy.Spider):
    name = 'test7'
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

        yield item
