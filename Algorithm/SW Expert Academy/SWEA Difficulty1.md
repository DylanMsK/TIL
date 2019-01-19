# SWEA Difficulty1

### [1545. 거꾸로 출력해 보아요](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2gbY0qAAQBBAS0&categoryId=AV2gbY0qAAQBBAS0&categoryType=CODE)

```python
n = int(input())
for i in range(n, -1, -1):
    print(i, end=' ')
```



### [1933. 간단한 N의 약수](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PhcWaAKIDFAUq&categoryId=AV5PhcWaAKIDFAUq&categoryType=CODE)

```python
n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')
```



### [1936. 1대1 가위바위보](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE)

```python
x = input().split()
a, b = int(x[0]), int(x[-1])

if a == 1:
    if b == 2:
        print('B')
    else:
        print('A')
elif a == 2:
    if b == 1:
        print('A')
    else:
        print('B')
else:
    if b == 1:
        print('B')
    else:
        print('A')
```



### [1938. 아주 간단한 계산기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjsYKAMIDFAUq&categoryId=AV5PjsYKAMIDFAUq&categoryType=CODE)

```python
x = input().split()
a, b = int(x[0]), int(x[-1])

print(f'{a+b}\n{a-b}\n{a*b}\n{round(a/b)}')
```



### [2019. 더블더블](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QDEX6AqwDFAUq&categoryId=AV5QDEX6AqwDFAUq&categoryType=CODE)

```python
n = int(input())

for i in range(n+1):
    print(2**i, end=' ')
```



### [2025. N줄덧셈](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QFZtaAscDFAUq&categoryId=AV5QFZtaAscDFAUq&categoryType=CODE)

```python
print(sum([i for i in range(1, int(input())+1)]))
```



### [2027. 대각선 출력하기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QFuZ6As0DFAUq&categoryId=AV5QFuZ6As0DFAUq&categoryType=CODE)

```python
for i in range(5):
    result = list('+++++')
    result[i] = '#'
    print("".join(result))
```





### [2029. 몫과 나머지 출력하기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE)

```python
n = int(input())

for i in range(n):
    x = input().split()
    a, b = int(x[0]), int(x[-1])
    print(f'#{i+1} {a//b} {a%b}')
```



### [2043. 서랍의 비밀번호](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QJ_8KAx8DFAUq&categoryId=AV5QJ_8KAx8DFAUq&categoryType=CODE)

```python
p, k = map(int, input().split())

print(p-k+1)
```



### [2046. 스탬프 찍기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QKdT6AyYDFAUq&categoryId=AV5QKdT6AyYDFAUq&categoryType=CODE)

```python
print('#' * int(input()))
```



### [2047. 신문 헤드라인](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QKsLaAy0DFAUq&categoryId=AV5QKsLaAy0DFAUq&categoryType=CODE)

```python
# 1.
print(input().upper())


# 2.
s = input()

for i in s:
    if ord(i) in range(ord('a'), ord('z')+1):
        print(chr(ord(i)-(ord('a')-ord('A'))), end='')
    else:
        print(i, end='')
```



### [2050. 알파벳을 숫자로 변환](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QLGxKAzQDFAUq&categoryId=AV5QLGxKAzQDFAUq&categoryType=CODE)

```python
s = input()
for i in s:
    print(ord(i)-64, end=' ')
```



### [2056. 연월일 달력](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE)

```python
n = int(input())
cal = {1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31}

for idx in range(n):
    date = input()
    year, month, day = date[:4], date[4:6], date[6:]
    if not (float(month) in cal.keys()) or not (float(day) in range(1, cal[float(month)]+1)):
        print(f'#{idx+1} -1')
    else:
        print(f'#{idx+1} {year}/{month}/{day}')
```



### [2058. 자릿수 더하기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPRjqA10DFAUq&categoryId=AV5QPRjqA10DFAUq&categoryType=CODE)

```python
print(sum([int(i) for i in input()]))
```



### [2063. 중간값 찾기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPsXKA2UDFAUq&categoryId=AV5QPsXKA2UDFAUq&categoryType=CODE)

```python
n = int(input())

lst = sorted(list(map(int, input().split())))
print(lst[n//2])
```



### [2068. 최대수 구하기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE)

```python
n = int(input())
 
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
 
for idx, num in enumerate(nums):
    print('#{} {}'.format(idx+1, max(num)))
```



### [2070. 큰 놈, 작은 놈, 같은 놈](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE)

```python
n = int(input())
 
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
     
for idx, num in enumerate(nums):
    if num[0] < num[-1]:
        res = '<'
    elif num[0] == num[-1]:
        res = '='
    else:
        res = '>'
    print('#{} {}'.format(idx+1, res))
```



### [2071. 평균값 구하기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE)

```python
n = int(input())
 
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
 
for idx, num in enumerate(nums):
    print('#{} {}'.format(idx+1, round(sum(num)/len(num))))
```



### [2072. 홀수만 더하기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE)

```python
n = int(input())
 
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
     
for idx, num in enumerate(nums):
    sum = 0
    for i in num:
        if i % 2 == 1:
            sum += i
    print('#{} {}'.format(idx+1, sum))
```

