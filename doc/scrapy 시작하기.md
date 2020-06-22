# Scrapy Framework

## Scrapy의 장점

- 빠르고 안정적이다
- 프레임워크이다
  - 장점인가?
    - 내장된 기능이 많다, 좀더 획일적인 코드가 나올 것이다



## Scrapy 시작하기

### Scrapy package install

**`pip install Scrapy`**

> 앞의 S가 대문자이다!



### Scrapy 프로젝트 시작하기

**`scrapy startproject <패키지명>`**

#### 디렉토리 구조

**`scrapy startproject tutorial`**

- **`$HOME/projects/scrapyEX/`** -> 시작 디렉토리

```
scrapyEx
	|- tutorial 
		|- tutorial
        |- spider
        	|- __init__.py
        |- __init__.py
        |- items.py
        |- middlewares.py
        |- pipelines.py
        |- settins.py
	|- scrapy.cfg
```

startproject를 실행하면, 위와 같은 구조로 프로젝트가 생성된다.

> 위와 같이 tutorial - tutorial 디렉토리 구조가 생기지 않게 하려면 **`scrapy startproject tutorial .`** 처럼 뒤에 .을 이용해 현재 디렉토리에 구성하게 하는 방법도 있다.



### spider 만들기

**`scrapy genspider test scrapinghub.com`**

 위의 커맨드를 실행하면 스파이더를 만들어 준다!

```
scrapyEx
	|- tutorial 
		|- tutorial
        |- spider
        	|- __init__.py
        	|- testspider.py
        ...
	|- scrapy.cfg
```

> spider 디렉토리에서 직접 만들어도 무방하다.



- 초기 구현되어있는 코드

```python
# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['http://scrapinghub.com/']

    def parse(self, response):
        pass

```



### Runspider, Crawl

#### Runspider

- spider.py 파일이 있는 디렉토리에서 실행해야 한다.
- 단위 테스트나 구현중 테스트시 하나의 스파이더만 돌려보고 싶을 때 유용하다.



**`scrapy runspider testspider.py`**

#### crawl

- 완성 후 테스트나 운영 시에는 crawl이 좋다
- `scrapy.cfg`가 있는 디렉토리에서 실행해야 한다.



**`scrapy crawl testspider`**





### 참고 사이트

- [scrapinghub.com](scrapinghub.com/)

