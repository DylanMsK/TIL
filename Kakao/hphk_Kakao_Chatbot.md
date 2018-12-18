# Kakao Chatbot

[멋사 kako link](https://s3.py.hphk.io)
kakao 검색어: **ssafy 파이썬 챗봇 서울 #3**

#### *환율*

```python
from bs4 import BeautifulSoup
import requests

url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser').tbody
tr = soup.findAll('tr')

countries = []
for country in tr:
  temp = []
  td = country.findAll('td')
  temp.append(td[0].text.strip())
  temp.append(td[1].text)
  temp.append(td[2].text)
  temp.append(td[3].text)
  countries.append(temp)
  
for co in countries:
  print('** {} **\n매매기준: {}\n살때: {}\n팔때: {}\n'.format(co[0], co[1], co[2], co[3]))
```



##### *네이버웹툰*

```python
from bs4 import BeautifulSoup as bs
import requests
import datetime

day = datetime.datetime.today().strftime('%a').lower()
url_base = 'https://comic.naver.com'
url_sub = '/webtoon/weekdayList.nhn?week={}'.format(day)
html = requests.get(url_base + url_sub).text
lis = bs(html, 'html.parser').find('div', class_='list_area daily_img').ul.findAll('li')

webtoons = []
for li in lis:
    webtoon = {}
    webtoon['title'] = li.find('div', class_='thumb').a['title']
    webtoon['href'] = url_base + li.find('div', class_='thumb').a['href']
    webtoon['rating'] = li.find('div', class_='rating_type').strong.text
    webtoons.append(webtoon)
    
for webtoon in webtoons:
    print("{}({})\n{}\n".format(webtoon['title'], webtoon['rating'], webtoon['href']))
```



#### *다음웹툰*

```python
import json
import requests
import time

url = 'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{}'.format(time.strftime('%a').lower())
doc = requests.get(url).text
res = json.loads(doc)

webtoons = []
url_base = 'http://webtoon.daum.net/webtoon/view/'
for el in res['data']:
    webtoon = {}
    webtoon['title'] = el['title']
    nickname = el['nickname']
    webtoon['url'] = url_base + nickname
    webtoons.append(webtoon)
    
for i in webtoons:
    print('{}\n{}'.format(i['title'], i['url']))
```





### 꿀팁

1. 크롬 앱 JSON Viewer로 json양식 보기좋게 정리
2. 네이버는 모바일 버전으로 크롤링하면 sleep 필요x
3. 개발자 도구에 2번째줄 맨 오른쪽 화살표 내리면 slow 3G모드 적용 가능