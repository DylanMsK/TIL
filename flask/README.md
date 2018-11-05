# day2

## flask

- 파이썬 환경설정

  ```bash
  $ pyenv virtualenv 3.6.1 flask
  $ pyenv activate flask
  ```

- flask 설치

  `pip install flask`

- `app.py`

  ```python
  from flask import Flask
  app = Flask(__name__)
  
  @app.route('/')
  def hello():
      return 'Hello World!'
      
  @app.route('/welcome')
  def welcome():
      return 'Welcome flask!'
      
  @app.route('/html_tag')
  def html_tag():
      return '<h1>안녕하세요!!</h1>'
      
  @app.route('/html_line')
  def html_line():
      return """
      <h1>여러줄을 보내봅시다.</h1>
      <ul>
          <li>1번</li>
          <li>2번</li>
      </ul>
      """
  ```

- 서버 실행

  `flask run --host 0.0.0.0 --port 8080`
 