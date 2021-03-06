# Scrapy spider



## Spider 의 종류

기본적으로는 scrapy.Spider 클래스를 사용하는데, 이 클래스를 상속받은 4가지 spider도 있다.

- CrawlSpider
- XMLFeedSpider
- CSVFeedSpider
- SitemapSpider

기본적인 Spider 클래스로도 원하는 기능들을 거의 사용 가능하다.



## Attribute

### name

- spider 의 이름을 정해준다
- `scrapy crawl <정해준 이름>` 같이 스파이더를 실행할 때 name 에서 정해준 값으로 실행한다.



### allowed_domain

- 크롤링시 접근할 도메인을 설정해 준다



### custom_settings

- 스파이더 프로젝트의 세팅을 동적으로 정해준다.
- settings.py 에 정의되어있는 설정보다 우선적으로 적용된다,



### start_urls

- 크롤링을 시작할 url을 설정해 준다



### start_request() 메소드

- start_urls 와 비슷한 기능을 한다( start_urls를 정해주는 방법이 이 메소드를 오버라이딩하는 것의 shortcut이다)
- 각각의 url마다 다른 처리 메소드를 정의해주고 싶다면 이 메소드를 오버라이딩해서 설정해 준다.



### Code

```python

import scrapy
# import logging

# 파이썬의 로거를 사용할 수도 있다
# 스크래피 프레임워크에 logging이 정의되어 있는데 굳이 파이썬 패키지를 쓸 필요는 없을듯
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
		
        # url 마다 다르게 처리
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

```

