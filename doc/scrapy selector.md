# Scrapy selector



## xpath 선택자 도움 사이트

- [Xpath 이야기](http://www.nextree.co.kr/p6278/)
- [scrapy 문서 Selectors > working with Xpath 부분](https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths)



### Xpath Selectors

- nodename : 이름이 nodename인 노드 선택
- text() : 노드의 텍스트만 추출
  - `//div//h2//text()`
- / : 루트부터 시작
- // : 현재 node부터 문서상의 모든 노드 조회
- . : 현재 노드
- .. : 현재 노드의 부모 노드
- @ : 속성 선택자
  - `//div/a/@href`
  - `//div[@class="myclass"]/a/@href`





## CSS 선택자 도움 사이트

- [scrapy 문서 Selectors > Using selectors > Extensions to CSS Selectors 부분](https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors) 



### CSS Selectors

- A B : 자손 선택
- A > B : 자식 선택
- ::text : 노드의 텍스트만 추출
- ::attr(name) : 노드의 속성값(name) 추출





## 그 외

- get(), getall(), extract(), extract_first() 네가지 숙지하기
- get(default='') 설정해서 값이 없을 경우 처리





## 연습 코드

- https://docs.scrapy.org/en/latest/index.html 에서 왼쪽 navbar 의 메뉴들을 가져와 보자!

### Code

```python
#scrapy shell에서 실행
fetch('https://docs.scrapy.org/en/latest/index.html')

tmp_title = '' 
menu = dict() 
for contents in response.css('nav.wy-nav-side div.wy-menu').xpath('./*'): 
	if contents.xpath('./span'): 
         title = contents.xpath('./span//text()').get() 
         tmp_title = title 
         menu[title] = [] 
    else: 
         for submenu in contents.xpath('.//li'): 
             menu[tmp_title].append(submenu.xpath('.//a//text()').get())
```



### 결과 (menu dict)

```python
{'All the rest': ['Release notes',
                  'Contributing to Scrapy',
                  'Versioning and API Stability'],
 
 'Basic concepts': ['Command line tool',
                    'Spiders',
                    'Selectors',
                    'Items',
                    'Item Loaders',
                    'Scrapy shell',
                    'Item Pipeline',
                    'Feed exports',
                    'Requests and Responses',
                    'Link Extractors',
                    'Settings',
                    'Exceptions'],
 
 'Built-in services': ['Logging',
                       'Stats Collection',
                       'Sending e-mail',
                       'Telnet Console',
                       'Web Service'],
 
 'Extending Scrapy': ['Architecture overview',
                      'Downloader Middleware',
                      'Spider Middleware',
                      'Extensions',
                      'Core API',
                      'Signals',
                      'Item Exporters'],
 
 'First steps': 	['Scrapy at a glance',
                 	'Installation guide',
                 	'Scrapy Tutorial',
                 	'Examples'],
 
 'Solving specific problems': ['Frequently Asked Questions',
                               'Debugging Spiders',
                               'Spiders Contracts',
                               'Common Practices',
                               'Broad Crawls',
                               'Using your browser’s Developer Tools for '
                               'scraping',
                               'Selecting dynamically-loaded content',
                               'Debugging memory leaks',
                               'Downloading and processing files and images',
                               'Deploying Spiders',
                               'AutoThrottle extension',
                               'Benchmarking',
                               'Jobs: pausing and resuming crawls',
                               'Coroutines',
                               'asyncio']}

```

