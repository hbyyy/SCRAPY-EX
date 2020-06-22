# Scrapy 실습 - 2

> 링크를 순회해보자!



### 기본 구조

```
scrapyEx
	|- section02_2
		|- section02_2
        |- spider
        	|- __init__.py
        	|- class02_2.py
        |- __init__.py
        |- items.py
        |- middlewares.py
        |- pipelines.py
        |- settins.py
	|- scrapy.cfg
```



### spider.py

```python
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

        for url in response.css('div.post-item > div > a::attr("href")').getall():
            yield scrapy.Request(url)

```



이 실습 페이지에서는 a 태그의 url 이 절대경로로 되어있지만, **상대경로**로 되어있는 url도 많다.

- 절대경로일 때
  - `https://blog.scrapinghub.com/guide-to-web-data-extraction-qa-validation-techniques`
- 상대경로일 때
  - `/guide-to-web-data-extraction-qa-validation-techniques`



### url이 상대경로일 때

**`response.urljoin`** 메소드를 사용한다! 

```
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

        for url in response.css('div.post-item > div > a::attr("href")').getall():
            yield scrapy.Request(response.urljoin(url))
```





### 크롤링한 링크를 사용해 상세 페이지 크롤링하기

 위의 parse 메소드의 리턴 Request에 **callback** 인자를 넣어준다



```python
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

        for url in response.css('div.post-item > div > a::attr("href")').getall():
        	#callback = 리턴한 링크들을 처리할 메소드 (정의해줘야 한다.) 
            yield scrapy.Request(response.urljoin(url), callback=parse_title)
    
    # 위의 parse 메소드의 callback 메소드, 직접 정의해 주어야 한다.
        def parse_title(self, response):
        """
        상세 페이지 -> 타이틀 추출
        :param response:
        :return: Text
        """
        contents = response.css('div.post-body > span > p::text').getall()
        yield {
            'contents': ''.join(contents),
        }
```



scrapy는 보통 이런 식으로 크롤링을 한다!