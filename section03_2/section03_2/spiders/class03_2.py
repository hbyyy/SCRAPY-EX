# -*- coding: utf-8 -*-

import scrapy


# 파이썬의 로거를 사용할 수도 있다
# 스크래피 프레임워크에 logging이 저으이되어 있는데 굳이 파이썬 패키지를 쓸 필요는 없다.
# logger = logging.getLogger('MyLogger')


class TestSpider(scrapy.Spider):
    name = 'test4'
    allowed_domains = ['blog.scrapinghub.com', 'naver.com', 'daum.net']

    # 실행방법 1 , 멀티 도메인
    start_urls = ['https://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']

    # 설정을 동적으로 설정
    # 여기 설정한 것이 우선으로 적용된다.
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        "COOKIES_ENABLED": True,
    }

    # 실행방법 2 , 각각 처리함수를 따로 지정하고 싶을 때
    # def start_requests(self):
    #     yield scrapy.Request('https://blog.scrapinghub.com/', self.parse1)
    #     yield scrapy.Request('https://naver.com', self.parse2)
    #     yield scrapy.Request('https://daum.net', self.parse3)

    def parse(self, response):
        self.logger.info('Response URL : %s' % response.url)
        self.logger.info('Response Status : %s' % response.status)

        if response.url.find('scrapinghub'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        elif response.url.find('naver'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        else:
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
