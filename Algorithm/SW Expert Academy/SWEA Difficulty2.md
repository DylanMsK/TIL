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

### [1859. 백만 장자 프로젝트](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE)
```python
for _ in range(int(input())):
    days = int(input())
    lst = list(map(int, input().split()))
    
    sum_ = 0
    cnt = 0
    while lst:
        cnt += 1
        max_ = lst.index(max(lst))
        temp = sum(lst[:max_])
        sum_ += lst[max_] * max_ - temp
        lst = lst[max_+1:]

    print("#{} {}".format(_+1, sum_))
```

### [1926. 간단한 369게임](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE)
```python
n = input()
for i in range(1, int(n)+1):
    cnt = 0
    if ('3' in str(i)) or ('6' in str(i)) or ('9' in str(i)):
        cnt += str(i).count('3') + str(i).count('6') + str(i).count('9')
    if cnt == 0:
        print(i, end=' ')
    else:
        print('-'*cnt, end=' ')
```

### [1928. Base64 Decoder](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PR4DKAG0DFAUq&categoryId=AV5PR4DKAG0DFAUq&categoryType=CODE)
```python
base64 = [chr(i) for i in range(ord('A'), ord('Z')+1)]
base64 += [chr(i) for i in range(ord('a'), ord('z')+1)]
base64 += [str(i) for i in range(10)]
base64 += ['+', '/']

def incoding(num):
    lst = [0]*6
    for i in range(5, -1, -1):
        if not num:
            break
        if num >= 2**i:
            num -= 2**i
            lst[5-i] += 1
    s = ''.join([str(i) for i in lst])
    return s

def decoding(bit):
    num = 0
    for i in range(7, -1, -1):
        if int(bit[7-i]):
            num += 2**i
    return num

for _ in range(int(input())):
    s = input()
    raw = ''
    for i in range(0, len(s), 4):
        for j in s[i:i+4]:
            raw += incoding(base64.index(j))
    result = ''
    for i in range(0, len(raw), 8):
        num = decoding(raw[i:i+8])
        result += chr(num)

    print(f'#{_+1} {result}')
```

### [1940. 가랏! RC카!](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjMgaALgDFAUq&categoryId=AV5PjMgaALgDFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    N = int(input())
    x = v = 0
    for i in range(N):
        state = list(map(int, input().split()))

        if state[0] == 0:
            x += v
        else:
            if state[0] == 1:
                v += state[1]
                x += v
            else:
                v = max(0, v-state[1])
                x += v

    print(f'#{_+1} {x}')
```

### [1945. 간단한 소인수분해](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq&categoryId=AV5Pl0Q6ANQDFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    N = int(input())
    temp = {i: 0 for i in [2, 3, 5, 7, 11]}
    for i in temp.keys():
        while N % i == 0:
            N = N // i
            temp[i] += 1

    print(f'#{_+1} {" ".join([str(i) for i in list(temp.values())])}')
```

### [1946. 간단한 압축 풀기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PmkDKAOMDFAUq&categoryId=AV5PmkDKAOMDFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    lst = [input() for i in range(int(input()))]
    s = ''
    for i in lst:
        temp = i.split()
        s += temp[0] * int(temp[1])

    print(f'#{_+1}')
    for i in range(0, len(s), 10):
        print(s[i:i+10])
```

### [1948. 날짜 계산기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PnnU6AOsDFAUq&categoryId=AV5PnnU6AOsDFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    sm, sd, em, ed = map(int, input().split())
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = (sum(days[:em-1])+ed) - (sum(days[:sm-1])+sd) + 1

    print('#'+str(_+1), result)
```

### [1954. 달팽이 숫자](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    N = int(input())
    arr = [i for i in range(1, N**2+1)]
    te, be, re, le = -1, N, N, -1
    x, y = -1, 0
    dx, dy = 1, 0
    brr = [[0]*N for i in range(N)]
    for i in arr:
        y, x = y+dy, x+dx
        brr[y][x] = i
        nxt_y, nxt_x = y, x
        if nxt_x + dx == re:
            dx, dy = 0, 1
            te += 1
        if nxt_y + dy == be:
            dx, dy = -1, 0
            re -= 1
        if nxt_x + dx == le:
            dx, dy = 0, -1
            be -= 1
        if nxt_y + dy == te:
            dx, dy = 1, 0
            le += 1

    print(f'#{_+1}')
    for i in brr:
        print(' '.join([str(j) for j in i]))
```

### [1959. 두 개의 숫자열](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if N > M:
        a, b = b, a
        N, M = M, N

    max_ = 0
    for i in range(M-N+1):
        sum_ = 0
        for j in range(N):
            sum_ += a[j] * b[i+j]
        if sum_ > max_:
            max_ = sum_

    print(f'#{_+1} {max_}')
```

### [1961. 숫자 배열 회전](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE)
```python
def lotation(arr):
    brr = [[0]*N for i in range(N)]
    for y in range(N):
        for x in range(N):
            brr[y][N-1-x] = arr[x][y]
    return brr

for _ in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    brr = lotation(arr)
    crr = lotation(brr)
    drr = lotation(crr)
    
    print(f'#{_+1}')
    for i in range(N):
        print(f'{"".join([str(x) for x in brr[i]])} {"".join([str(x) for x in crr[i]])} {"".join([str(x) for x in drr[i]])}')
```

### [1966. 숫자를 정렬하자](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PrmyKAWEDFAUq&categoryId=AV5PrmyKAWEDFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N):
        min_ = i
        for j in range(i+1, N):
            if nums[j] < nums[min_]:
                min_ = j
        nums[i], nums[min_] = nums[min_], nums[i]

    print(f'#{_+1} {" ".join([str(i) for i in nums])}')
```

### [1970. 쉬운 거스름돈](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    N = int(input())
    change = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}
    for m in change.keys():
        quotient = N // m
        if quotient:
            N = N - (quotient) * m
            change[m] += quotient

    print(f'#{_+1}\n{" ".join([str(i) for i in change.values()])}')
```

### [1974. 스도쿠 검증](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]

    flag = 1
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            row.append(arr[i][j])
            col.append(arr[j][i])
        if (len(set(row)) != 9) | (len(set(col)) != 9):
            flag = 0
            break
    
    if flag:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if len(set(arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3])) != 9:
                    flag = 0
                    break
            if not flag:
                break

    print(f'#{_+1} {flag}')
```

### [1976. 시각 덧셈](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PttaaAZIDFAUq&categoryId=AV5PttaaAZIDFAUq&categoryType=CODE)
```python
n = int(input())
for idx, i in enumerate(range(n)):
    time = list(map(int, input().split()))

    hour = time[0] + time[2]
    minute = time[1] + time[-1]
    if minute >= 60:
        minute -= 60
        hour += 1
    if hour > 12:
        hour -= 12

    print(f'#{idx+1} {hour} {minute}')
```

### [1979. 어디에 단어가 들어갈 수 있을까](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE)
```python
def check_K(arr):
    cnt = 0
    for i in arr:
        if sum(i) < K:
            continue
        sum_ = 0
        for j in i:
            if j:
                sum_ += j
            else:
                if sum_ == K:
                    cnt += 1
                sum_ = 0
        if sum_ == K:
            cnt += 1
    return cnt
        
for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    cnt = 0
    cnt += check_K(arr)
    for y in range(N):
        for x in range(N):
            if x > y:
                arr[y][x], arr[x][y] = arr[x][y], arr[y][x]
    cnt += check_K(arr)

    print(f'#{_+1} {cnt}')
```

### [1983. 조교의 성적 매기기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PwGK6AcIDFAUq&categoryId=AV5PwGK6AcIDFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    N, K = map(int, input().split())
    scores = []
    for i in range(N):
        M, F, A = map(int, input().split())
        score = (M * 0.35) + (F * 0.45) + (A * 0.2)
        scores.append(score)
    K = scores[K-1]
    K = (sorted(scores, reverse=True).index(K)) // (N // 10)
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    
    print(f'#{_+1} {grade[K]}')
```

### [1984. 중간 평균값 구하기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pw_-KAdcDFAUq&categoryId=AV5Pw_-KAdcDFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    lst = list(map(int, input().split()))
    med_lst = sorted(lst)[1:-1]
    avg = sum(med_lst) / len(med_lst)

    print(f'#{_+1} {round(avg)}')
```

### [1986. 지그재그 숫자](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PxmBqAe8DFAUq&categoryId=AV5PxmBqAe8DFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    print(f'#{_+1} {sum([i if i % 2 else -i for i in range(1, int(input())+1)])}')
```

### [1989. 초심자의 회문 검사](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PyTLqAf4DFAUq&categoryId=AV5PyTLqAf4DFAUq&categoryType=CODE)
```python
T = int(input())
for _ in range(T):
    s = input().strip()
    if s == s[::-1]:
        result = 1
    else:
        result = 0

    print(f'#{_+1} {result}')
```

### [2001. 파리 퇴치](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE)
```python
T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for m in range(M)]
    temp = []
    for i in range(M-N+1):
        for j in range(M-N+1):
            sum_ = 0
            for k in arr[i:i+N]:
                sum_ += sum(k[j:j+N])
            temp.append(sum_)

    print(f'#{_+1} {max(temp)}')
```

### [2005. 파스칼의 삼각형](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE)
```python
T = int(input())
for _ in range(T):
    N = int(input())
    print(f'#{_+1}')
    print(1)
    init = [1, 1]
    for i in range(N-1):
        print(' '.join([str(__) for __ in init]))
        init = [1] + [sum(init[j:j+2]) for j in range(len(init)-1)] + [1]
```

### [2007. 패턴 마디의 길이](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE)
```python
for _ in range(int(input())):
    s = input()
    l = 0
    for i in range(1, 11):
        if s[:i] == s[i:2*i]:
            l = i
            break
            
    print(f'#{_+1} {l}')
```