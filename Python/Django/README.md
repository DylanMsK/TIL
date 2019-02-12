# Django

[django document](https://docs.djangoproject.com/en/2.1/)

## Environment Setting

- Install pyenv

  ```bash
  $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  ```

- Set pyenv environment variable

  ```bash
  $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  
  $ source ~/.bashrc
  ```

- Install pyenv virtualenv

  ```bash
  $ git clone https://github.com/pyenv/pyenv-virtualenv.git $PYENV_ROOT/plugins/pyenv-virtualenv
  ```

- Set pyenv-virtualenv environment variable

  ```bash
  $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
  $ source ~/.bashrc
  ```

- Install Python

  ```bash
  $ pyenv install --list
  $ pyenv install <python version>
  $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  $ source ~/.bashrc
  ```

- Make virtual environment

  ```bash
  # 전역에서 <python version> 사용
  $ pyenv global <python version>
  $ python -V
  Python <python version>
  # 특정 폴더를 가상환경으로 사용
  $ pyenv virtualenv <python version> <virtual environment name for setting>
  $ pyenv local tele
  $ pyenv activate <virtual environment name for setting>
  $ pyenv deactivate
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
$ django-admin startproject <name for project>
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

  