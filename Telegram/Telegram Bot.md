# Telegram Bot

## 1. Telegram install

- 모바일 telegram app 설치



## 2. Create bot

1. telegram에서 'BotFather' 친추
2. '/newbot' 입력 후 봇이름, 유저이름 생성하고 token 받기



## 3. C9

#### *~/.bashrc*

```bash
...
export $TELEGRAM_TOKEN=<telegram token 입력>	# 마지막줄에 요거 추가
```

`$ source ~/.bashrc` 후에 `$echo $TELEGRAM_TOKEN`으로 확인

#### *app.py*

```python
from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import os
import time
import json

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL = 'https://api.hphk.io/telegram'

@app.route('/')
def index():
    return "<h1>This is Index</h1>"

@app.route('/{}'.format(TELEGRAM_TOKEN), methods=['POST'])
def telegram():
    res = request.get_json()
    chat_id = res['message']['from']['id']
    msg = res['message']['text']
    url = TELEGRAM_URL + '/bot{}/sendMessage'.format(TELEGRAM_TOKEN)
    
    if msg == '안녕':
        text = '첫인사는 존댓말로 해야지'
        requests.get(url, params={'chat_id': chat_id, 'text': text})
    
    if msg == '환율':
        exchange_url = 'https://www.xe.com/currencytables/?from=KRW&date=2018-12-20'
        html = requests.get(exchange_url).text
        soup = BeautifulSoup(html, 'html.parser')
        trs = soup.find('div', class_='historicalRateTable-wrap').tbody.findAll('tr')
        contries = []
        for tr in trs:
            temp = {}
            tds = tr.findAll('td')
            temp['CurrencyName'] = tds[1].text
            temp['CurrencyCode'] = tds[0].a.text
            temp['Rate'] = round(float(tds[-1].text), 2)
            contries.append(temp)   
        us_currency = contries[0]
        requests.get(url, params={'chat_id': chat_id,
                                  'text': "{} ({})\n{}원".format(us_currency['CurrencyName'], 															us_currency['CurrencyCode'], 																us_currency['Rate'])})         
    return '', 200
    
@app.route('/set_webhook')
def set_webhook():
    url = TELEGRAM_URL + '/bot' + TELEGRAM_TOKEN + '/setWebhook'
    params = {
        'url': 'https://ssafy-week2-dylankang.c9users.io/{}'.format(TELEGRAM_TOKEN)
    }
    res = requests.get(url, params=params).text
    return res
```



