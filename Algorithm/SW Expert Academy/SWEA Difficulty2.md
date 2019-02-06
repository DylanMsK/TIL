# SWEA Difficulty2

### [1204. 최빈수 구하기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE)

```python
for _ in range(int(input())):
    T = int(input())
    lst = list(map(int, input().split()))
    score = max(lst, key=lst.count)

    print(f'#{T} {score}')
```

### [1284. 수도 요금 경쟁](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV189xUaI8UCFAZN&categoryId=AV189xUaI8UCFAZN&categoryType=CODE)
```python
for _ in range(int(input())):
    P,Q,R,S,W=map(int,input().split())
    A,B=P*W,max(Q,Q+max(W-R,0)*S)

    print(f'#{_+1} {min(A,B)}')
```

### [1285. 아름이의 돌 던지기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18-stqI8oCFAZN&categoryId=AV18-stqI8oCFAZN&categoryType=CODE)
```python
for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    lst = [abs(i) for i in lst]
    min_ = min(lst)
    cnt = lst.count(min_)

    print('#{} {} {}'.format(_+1, min_, cnt))
```

### [1288. 새로운 불면증 치료법](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18_yw6I9MCFAZN&categoryId=AV18_yw6I9MCFAZN&categoryType=CODE)
```python
for _ in range(int(input())):
    N = int(input())
    lst = list(str(i) for i in range(10))
    cnt = 0
    while len(lst):
        cnt += 1
        for i in str(N*cnt):
            if i in lst:
                lst.remove(i)
                
    print(f'#{_+1} {N*cnt}')
```