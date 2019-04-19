# Django

[django document](https://docs.djangoproject.com/en/2.1/)

## Environment Setting

- Install pyenv

  ```bash
  $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  ```

- Set pyenv environment variable

  ```bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  
  source ~/.bashrc
  ```

- Install pyenv virtualenv

  ```bash
  git clone https://github.com/pyenv/pyenv-virtualenv.git $PYENV_ROOT/plugins/pyenv-virtualenv
  ```

- Set pyenv-virtualenv environment variable

  ```bash
  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
  source ~/.bashrc
  ```

- Install Python

  ```bash
  pyenv install --list
  pyenv install <python version>
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  source ~/.bashrc
  ```

- Make virtual environment

  ```bash
  # 전역에서 <python version> 사용
  pyenv global <python version>
  python -V
  Python <python version>
  # 특정 폴더를 가상환경으로 사용
  pyenv virtualenv <python version> <virtual environment name for setting>
  pyenv local tele
  pyenv activate <virtual environment name for setting>
  pyenv deactivate		# 가상환경 종료
  ```




## Make Better Env.

1. ipython

   파이썬 콘솔창을 jupyter 스럽게 만들어줌

   ```bash
   $ pip install ipython		# 파이썬 콘솔창을 jupyter 스럽게
   $ python manage.py shell
   Python 3.6.7 (default, Feb 11 2019, 05:35:49) 
   Type 'copyright', 'credits' or 'license' for more information
   IPython 7.3.0 -- An enhanced Interactive Python. Type '?' for help.
   
   In [1]:
   ```

2. django_extensions

   터미널에 파이썬 콘솔장을 켤때 django에 입력된 모든 정보를 자동을 import 해줌

   ```bash
   $ pip install django_extensions
   ```

   - settings.py

   ```python
   INSTALLED_APPS = [
       ...
       'django_extensions',
   ]
   ```

   ```bash
   $ python manage.py shell_plus
   # Shell Plus Model Imports
   ...
   # Shell Plus Django Imports
   from django.core.cache import cache
   from django.conf import settings
   from django.contrib.auth import get_user_model
   from django.db import transaction
   from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
   from django.utils import timezone
   from django.urls import reverse
   Python 3.6.7 (default, Feb 11 2019, 05:35:49) 
   Type 'copyright', 'credits' or 'license' for more information
   IPython 7.3.0 -- An enhanced Interactive Python. Type '?' for help.
   
   In [1]: 
   ```
3. django-bootstrap4

    django form에 부트스트랩을 적용해줌

       ```bash
   $ pip install django-bootstrap4
   ```

   - settings.py

   ```python
   INSTALLED_APPS = [
       ...
       'bootstrap4',
   ]
   ```
  



## Start Django Project

1. 프로젝트 진행할 폴더 생성 후 해당 폴더로 이동
2. 가상환경 설정
3. Django 설치
4. Django Project [, Django App] 생성

```bash
$ mkdir <name for project>
$ cd <name for project>
$ pyenv virtualenv <python version> <virtual environment name for setting>
$ pyenv local <virtual environment name for setting>
$ pip install django
$ django-admin startproject <name for project> <path for project>
```



## Make Django Application

  ```bash
$ django-admin startapp <application name>
  ```

- `<project name>/<project name>/settings.py`

  ```python
  ...
  INSTALLED_APPS = [
      ...
      '<application>.apps.SolutionConfig'
  ]
  ```




#### ※꿀팁

```bash
# 콘솔창에 파이썬기반 확인
$ python manage.py shell
Python <version> (default, Feb 11 2019, 05:35:49) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 

# 콘솔창에 SQLite기반 SQL 확인
$ python manage.py dbshell
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> 
```

