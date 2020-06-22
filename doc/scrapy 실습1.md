# scrapy 실습 - 1

> 간단한 spider 를 만들어 크롤링을 해보자

먼저, 프로젝트를 생성하고 spider 를 만들어 준다.



**`scrapy startproject section_02_1`**

**`scrapy genspider class02-1 blog.scrapinghub.com`**



### 디렉터리 구조

```
scrapyEx
	|- section02_1 
		|- section02_1
        |- spider
        	|- __init__.py
        	|- class02_1.py
        |- __init__.py
        |- items.py
        |- middlewares.py
        |- pipelines.py
        |- settins.py
	|- scrapy.cfg
```



### `class02_1.py`

```python
# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        pass
```





### spider 만들어서 blog.scrapinghub.com 의 글 title 크롤링하기

- parse 메소드의 인자 response 를 이용해 글의 title 들을 크롤링 해 올수 있다.

```python
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

        for text in response.css('div.post-header h2 a::text').getall():
            # return Type : Request, BaseItem, Dict, None 필수!
            yield {
                'title': text,
            }
```



  위의 코드처럼 css 선택자나 xpath를 이용해 원하는 내용만 크롤링 해올 수 있다.



### parse  메소드의 return 값

 parse 메소드는 **반드시** 밑의 4가지 값 중 하나를 return 해야 한다. 스크래피에서는 일반적으로 yield 를 이용한다.

1. Request (scrapy에 구현되어 있다)
2. BaseItem
3. Dict 형 (파이썬 기본형)
4. None



### 크롤링한 데이터를 저장하기

 CLI 명령어를 이용해서 크롤링한 데이터를 저장할 수 있다.



**`scrapy crawl 명령어 option `** 

```shell
scrapy crawl --help                    
Usage
=====
  scrapy crawl [options] <spider>

Run a spider

Options
=======
--help, -h              show this help message and exit
-a NAME=VALUE           set spider argument (may be repeated)
--output=FILE, -o FILE  dump scraped items into FILE (use - for stdout)
--output-format=FORMAT, -t FORMAT
                        format to use for dumping items with -o

Global Options
--------------
--logfile=FILE          log file. if omitted stderr will be used
--loglevel=LEVEL, -L LEVEL
                        log level (default: DEBUG)
--nolog                 disable logging completely
--profile=FILE          write python cProfile stats to FILE
--pidfile=FILE          write process ID to FILE
--set=NAME=VALUE, -s NAME=VALUE
                        set/override setting (may be repeated)
--pdb                   enable pdb on failure

```



위의 명령어들을 보면, **-o** (output) 옵션과 **-t** (format) 옵션을 이용하면 결과물을 파일로 저장할 수 있다.

**`scrapy crawl test2 -o result.jl jsonlines`** -> jsonlines 포멧으로 저장

**`scrapy crawl test2 -o result.csv csv`** -> csv 포멧으로 저장



- 이용가능한 포멧들은 다음과 같다.

```shell
...from the supported list ('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')
```




- **Code**

```python
...
for text in response.css('div.post-header h2 a::text').getall():
            # return Type : Request, BaseItem, Dict, None 필수!
            yield {
                'title': text,
            }
...
```



**`scrapy crawl test2 -o result.jl jsonlines`**

- Output file

```json
{"title": "Price Gouging or Economics at Work: Price Intelligence to Track Consumer Sentiment"}
{"title": "A Practical Guide to Web Data QA Part III: Holistic Data Validation Techniques"}
{"title": "Product Reviews API (Beta): Extract Product Reviews at Scale"}
{"title": "Custom crawling & News API: designing a web scraping solution"}
{"title": "Vehicle API (Beta): Extract Automotive Data at Scale"}
{"title": "A Practical Guide to Web Data Extraction QA Part II: Common validation pitfalls"}
{"title": "Transitioning to Remote Working as a Company"}
{"title": "A Practical Guide to Web Data QA Part I: Validation Techniques"}
{"title": "COVID-19: Handling the Situation as a Fully Remote Company"}
{"title": "Extracting clean article HTML with News API"}
```

