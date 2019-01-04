## pyenv

[pyenv github](https://github.com/pyenv/pyenv)

- install

  ```bash
  $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  ```

> pyenv github에서 현재 컴퓨터로 파일 복사

- 환경변수 설정

  ```bash
  $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  
  $ source ~/.bashrc	# 환경변수 추가 후 bash_profile 실행 ==> 터미널 새로고침
  ```

- python 3.6.1 installation

  ```bash
  $ pyenv install --list	# pyenv로 설치 가능한 파일들 출력
  $ pyenv install 3.6.1
  $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  $ source ~/.bashrc
  $ pyenv global 3.6.1
  $ python -V		# python 버전확인
  Python 3.6.1
  ```





## pyenv virtualenv

[pyenv virtualenv](https://github.com/pyenv/pyenv-virtualenv)

- Install 

  ```bash
  $ git clone https://github.com/pyenv/pyenv-virtualenv.git $PYENV_ROOT/plugins/pyenv-virtualenv
  ```

- Setting

  ```bash
  $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
  $ source ~/.bashrc
  ```

- 가상환경 만들기

  ```bash
  # $ pyenv virtualenv <python version> <virtual environment name for setting>
  $ pyenv virtualenv 3.6.1 tele	# tele라는 가상환경을 생성
  ```

- 가상환경 실행하기

  ```bash
  # $ pyenv shell <virtual environment name for setting>
  $ pyenv activate tele	# tele라는 가상환경 실행
  $ pyenv deactivate		# tele라는 가상환경 정지
  # $ pyenv shell tele	# tele라는 가상황경 실행 ==> 이렇게 실행하면 deactivate가 안됨
  ```

- 가상환경 라이브러리 설치

  ```bash
  $ pip install bs4 requests	# bs4와 requests 설치
  ```



## Heroku

- Install

  ```bash
  $ heroku login
  $ git init 		# 로컬 git 초기화
  $ git add .		# 로컬 git에 현재 폴더에 있는 모든 파일을 저장
  $ git commit -m 'telegram'		# 임시저장된 파일들을 'telegram' 버전으로 저장
  $ heroku git:remote -a mcd-telegrambot		# heroku에 로컬 git을 전송
  $ pip freeze > requirements.txt		# C9에 있는 pyenv환경을 requirements.txt에 저장
  $ touch runtime.txt		# 현재 python 버전 내용을 포함한 파일 생성
  python-3.6.1
  $ git commit -m 'add requirements&runtime'
  $ git push -u heroku master
  ```





------

## Git 

분산저장 시스템

[git tutorial(easy)](https://backlog.com/git-tutorial/kr/)
[git tutorial(advanced)](https://git-scm.com/)

1. init
   1. 저장소를 만든다
2. add
   1. 임시저장 한다
   2. `git add .`을 사용해서 현재 폴더 및 하위 모든 항목을 추가
   3. `git add text.txt` 를 사용해서 원하는 파일 하나만 추가
3. commit
   1. 새로운 버전을 만든다
   2. `git commit -m <'변경 내용 작성'>`
   3. `git log`로 커밋 이력을 확인
4. remote
   1. 원격 저장소 설정
   2. `git remote add origin <저장소 url>` ==> origin이 아니여도 상관 없지만 통상적으로 origin 사용
5. push
   1. 내가 원하는 원격 저장소에 코드를 올리겠다
   2. `git push origin master`
6. 자주 사용하는 명령어
   1. `git status` ==> 파일/폴더의 변경 내용을 알려줌
   2. `git diff` ==> 몇번째 줄이 어떻게 바뀌었는지 알려줌
   3. `git log` ==> 커밋 이력 확인
   4. `git remote` ==> 현재 프로젝트에 등록된 원격 저장소를 확인



## HTML

> 웹페이지를 만들기 위한 언어, 웹브라우저(크롬, 파이어폭스) 위에서 동작

1. HTML 형식

   ```html
   <태그명 속성='속성값' 속성2='속성값2 속성값2-1'>정보</태그명>
   ```



2. HTML 문서의 구조

   ```html
   <!DOCTYPE html>
   <html>
       <head>
           <meta charset='utf-8'>
           <title>웹페이지 제목</title>
       </head>
       <body>
       </body>
   </html>
   ```

3. 태그
   - `<link>`  : 문서에 필요한 다른 파일을 가져올 때 사용
   - `<h1>` : 문서의 제목
   - `<a>` : 문서와 문서를 연결하는 주소를 포함
   - `<div>` : 여러가지 태그를 하나의 그룹으로 묶음

