# Django

## Environment Setting

- Install pyenv

  ```bash
  $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  ```

- Environment variable setting

  ```bash
  $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  
  $ source ~/.bashrc
  ```

- Python Installation

  ```bash
  $ pyenv install --list
  $ pyenv install <python version>
  $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  $ source ~/.bashrc
  $ pyenv global <python version>
  $ python -V
  Python <python version>
  ```

  

## Start Project

```bash
# django-admin startproject <folder name> <path>
django-admin startproject intro .
```

