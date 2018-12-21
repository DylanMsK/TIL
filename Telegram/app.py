from flask import Flask, request
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import os
from cmd import Command


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
    date = datetime.fromtimestamp(res['message']['date']).strftime('%m/%d/%Y %H:%M:%S')
    print('[{}]\t{}\t{}'.format(date, chat_id, msg))
    url = TELEGRAM_URL + '/bot{}/sendMessage'.format(TELEGRAM_TOKEN)
    cmd = Command()
    
    if msg == '안녕':
        text = cmd.hello()
    
    elif msg == '환율':
        text = cmd.exchange_rate()
    
    elif msg.startswith('마스터키'):
        if len(msg.split()) == 1:
            text = "지점명으로 예약여부를 확인하세요.\nex) 마스터키 잠실점\n\n" + cmd.masterkey(True)
        else:
            cafe_name = msg.split()[-1]
            text = cmd.masterkey(False, cafe_name)
            
    elif msg.startswith('서이룸'):
        if len(msg.split()) == 1:
            text = "지점명으로 예약여부를 확인하세요.\nex) 서이룸 홍대1호점\n\n" + cmd.escape(True)
        elif len(msg.split()) == 3:
            cafe_name = " ".join(msg.split()[-2:])
            text = cmd.escape(False, cafe_name)
        else:
            cafe_name = msg.split()[-1]
            text = cmd.escape(False, cafe_name)
            
    else:
        text = '없는 명령어 입니다.'
    
    requests.get(url, params={'chat_id': chat_id, 'text': text})
    return '', 200
    
@app.route('/set_webhook')
def set_webhook():
    url = TELEGRAM_URL + '/bot' + TELEGRAM_TOKEN + '/setWebhook'
    params = {
        'url': 'https://ssafy-week2-dylankang.c9users.io/{}'.format(TELEGRAM_TOKEN)
    }
    res = requests.get(url, params=params).text
    return res


