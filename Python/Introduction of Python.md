# **Introduction of Python**

## 1. Python Basic

> [python 공식 tutorial](https://docs.python.org/3.6/tutorial/index.html)

- #### 식별자

- #### 기초문법



## [3. Python 기본 자료형](https://docs.python.org/3.6/tutorial/introduction.html)

1. #### 숫자

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

   

2. #### 문자열

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

   

3. #### 리스트

   문자열과 다른 모든 내장 [시퀀스](https://docs.python.org/ko/3.6/glossary.html#term-sequence) 형들처럼 리스트는 인덱싱하고 슬라이싱할 수 있다.

   ```python
   >>> squares = [1, 4, 9, 16, 25]
   >>> squares
   [1, 4, 9, 16, 25]
   >>> squares[0]  # indexing returns the item
   1
   >>> squares[-1]
   25
   >>> squares[-3:]  # slicing returns a new list
   [9, 16, 25]
   ```

   모든 슬라이스 연산은 요청한 항목들을 포함하는 새 리스트를 돌려준다. 이는 다음과 같은 슬라이스가 리스트의 새로운 (얕은) 복사본을 돌려준다는 뜻.

   ```python
   >>> squares[:]
   [1, 4, 9, 16, 25]
   >>> squares + [36, 49, 64, 81, 100]
   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
   ```

   슬라이스에 대입하는 것도 가능한데, 리스트의 길이를 변경할 수 있고, 모든 항목을 삭제할 수도 있다.

   ```python
   >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
   >>> letters
   ['a', 'b', 'c', 'd', 'e', 'f', 'g']
   >>> # replace some values
   >>> letters[2:5] = ['C', 'D', 'E']
   >>> letters
   ['a', 'b', 'C', 'D', 'E', 'f', 'g']
   >>> # now remove them
   >>> letters[2:5] = []
   >>> letters
   ['a', 'b', 'f', 'g']
   >>> # clear the list by replacing all the elements with an empty list
   >>> letters[:] = []
   >>> letters
   []
   ```

1. ### 

## 9. 클래스

