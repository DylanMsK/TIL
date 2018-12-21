"""
Telegram Command List
hello : 인사
exchange_rate : 환율
masterkey : 마스터키
escape : 서이룸
"""

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json


class Command():
    def __init__(self):
        pass
    
    def hello(self):
        text = "첫인사는 존댓말로 해야지"
        return text
        
    def exchange_rate(self):
        date = datetime.today().strftime('%Y-%m-%d')
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
        text = "{} ({})\n{}원".format(us_currency['CurrencyName'], us_currency['CurrencyCode'], us_currency['Rate'])
        return text
    
    def masterkey(self, boolean, cafe_name=None):
        base_url = 'http://www.master-key.co.kr'
        office_url = '/home/office'
        html = requests.get(base_url + office_url).text
        soup = BeautifulSoup(html, 'html.parser')
        lis = soup.select('.escape_list .escape_view')
        
        lst = []
        for li in lis:
            temp = {}
            escape_text = li.find('div', class_='escape_text')
            name = escape_text.p.text
            if name.endswith('NEW'):
                name = name[:-3]
            temp['name'] = name
            temp['address'] = escape_text.findAll('dl')[0].dd.span.text.strip()
            temp['phone'] = escape_text.findAll('dl')[1].dd.span.text
            temp['link'] = base_url + li.a['href']
            lst.append(temp)
            
        code_name = {i['name']: i['link'].split('?bid=')[-1] for i in lst}
    
        if boolean:
            text = "\n".join([str(name) for name in code_name.keys()])
            return text
            
        if cafe_name in code_name.keys():
            url_detail = 'http://www.master-key.co.kr/booking/booking_list_new'
            params = {'date': datetime.today().strftime('%Y-%m-%d'), 
                      'store': code_name[cafe_name]}
            html = requests.post(url_detail, params=params).text
            soup = BeautifulSoup(html, 'html.parser')
            
            time_lst = []
            lis = soup.findAll('li', class_='escape_view')
            for li in lis:
                temp = {}
                
                base = li.find('div', class_='escape_text clearfix').findAll('p')
                temp['title'] = base[0].text
                temp['type'] = base[-1].findAll('span')[0].text.split(' : ')[-1]
                temp['difficulty'] = '★' * len(base[-1].findAll('span')[1].findAll('i'))
                temp['num'] = base[-1].findAll('span')[-1].text.split(':  ')[-1]
                temp['desc'] = li.find('div', class_='escape_Img')['data-text']
                
                reservations = []
                divs = li.find('div', class_='col_wrap clearfix').findAll('div')
                for div in divs:
                    reservation = {}
                    p = div.findAll('p')
                    reservation['time'] = p[0].text
                    reservation['state'] = p[-1].text
                    reservations.append(reservation)
                temp['reservation'] = reservations
                
                time_lst.append(temp)
            
            text = "\n\n".join([i['title'] + '\n테마 유형: ' + i['type'] + '\n난이도: ' + i['difficulty'] + '\n인원: ' + i['num'] + '\n[예약상태]\n' + '\n'.join([str(j['time']) + '\t' + str(j['state']) for j in i['reservation']]) for i in time_lst])
            return text
        else:
            text ='지점이 없습니다.'
            return text
    
    def escape(self, boolean, branch_name=None):
        branch = {'홍대1호점': 1, '홍대2호점': 10, '강남1호점': 3, '강남2호점': 11, '인천 부평점': 4, '부산 서면점': 5}
        
        if boolean:
            text = "\n".join(branch.keys())
            return text
        
        url = 'http://www.seoul-escape.com/reservation/change_date/'
        params = {'current_date': datetime.now().strftime('%Y/%m/%d')}
        txt = requests.get(url, params = params).text
        res = json.loads(txt)
        
        lst = []
        for i in res['bookList']:
            if i['branch_id'] == branch[branch_name]:
                temp = {}
                temp['room'] = i['room']
                temp['hour'] = i['hour']
                if i['booked']:
                    temp['booked'] = '풀방ㅠㅠ'
                else:
                    temp['booked'] = '예약가능!!'
                lst.append(temp)
    
        room_name = []
        for i in lst:
            room_name.append(i['room'])
        room_name = {i: [] for i in set(room_name)}
        
        for j in room_name:
            for i in lst:
                time = {}
                if i['room'] == j:
                    time['hour'] = i['hour']
                    time['booked'] = i['booked']
                    room_name[j].append(time)
        
        text = "\n\n".join([str(i) + '\n' + '\n'.join([str(j['hour']) + '\t' + str(j['booked']) for j in room_name[i]]) for i in room_name])
        return text