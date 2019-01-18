# **Introduction of Python**

## 1. Python Basic

> [python 공식 tutorial](https://docs.python.org/3.6/tutorial/index.html)

- #### 식별자

- #### 기초문법



## [3. Python 기본 자료형](https://docs.python.org/3.6/tutorial/introduction.html)

1. ### 숫자

   ```python
   >>> 17 / 3		# '/'는 무조건 float만 리턴
   5.66666666666667
   >>> 17 // 3		# '//'는 소수점 버림 한 정수만 리턴
   5
   >>> 17 % 3		# '%'는 나머지 리턴
   2
   >>> 5 * 3 + 2	# (5 * 3) + 2
   17
   >>> 2 ** 7		# '**'는 거듭제곱을 리턴
   128
   ```

   

2. ### 문자열

   ```python
   >>> 'doesn\'t'		# 동일한 따옴표를 쓸때는 이스케이프 문자(￦)로 사용 가능
   "doesn't"
   >>> "doesn't"
   "doesn't"
   >>> "\"Yes,\" they said."
   '"Yes," they said.'
   >>>'"Isn\'t," they said.'
   '"Isn\'t," they said.'
   ```

   문자열 안에 '￦'를 문자로 취급되게 하고 싶지 않다면,

   ```python
   >>> print('C:\some\name')
   C:\some
   ame
   >>> print(r'C:\some\name')		# 'r'을 문자열 앞에 붙혀 raw string도 가능
   C:\some\name
   >>> print('C:\\some\\name')		# '\'를 한 번 더 써줌
   C:\some\name
   ```

   삼중 따옴표로 여러줄 한번에 리턴하기(삼중 따옴표는 **자동 줄바꿈에 포함**되어있음!)

   ```python
   >>> print("""\
   ...			Usage: thingy [OPTIONS]
   ...			     -h                        Display this usage message
   ...			     -H hostname               Hostname to connect to
   ...			""")
   Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
   # 첫 번째 개행문자가 포함되지 않음
   ```

   문자열 더하기

   ```python
   >>> 3 * 'un' + 'ium'
   'unununium'
   >>> 'Py' 'thon'
   'Python'
   >>> text = ('Put several strings within parentheses '
   ...         'to have them joined together.')
   >>> text		# 이 기능은 오직 두 개의 문자열에만 적용됨
   'Put several strings within parentheses to have them joined together.'
   >>> prefix = 'Py'
   >>> prefix 'thon'  # can't concatenate a variable and a string literal
     ...
   SyntaxError: invalid syntax
   >>> ('un' * 3) 'ium'
     ...
   SyntaxError: invalid syntax
   ```

### 3. 리스트

```

```

