## Import webbrowser library
```python
import webbrowser
```

## Open URL
```python
webbrowser.open(<url>)
```
### - Practice
```python
import webbrowser

url = "https://search.daum.net/search?q="

momo = ['나윤', '혜빈', '아인', '낸시', '주이', '연우', '제인', '데이지', '태하']
for member in momo:
    webbrowser.open(url + member)
```