# url = 'https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWhVVhNaS8EDFAW_&contestProbId=AV18NaZqIt8CFAZN&probBoxId=AWh9aYhq23kDFAXp&type=PROBLEM&problemBoxTitle=1%EC%9B%9424%EC%9D%BC&problemBoxCnt=1'

import sys
sys.stdin = open('금속막대_input.txt', 'r')

def combine(key, cnt):
    if key in bolts.keys():
        keys.append(key)
        cnt += 1
        return combine(bolts[key], cnt)
    return cnt

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    bolts = {lst[i]: lst[i+1] for i in range(0, 2*n, 2)}
    for key in bolts.keys():
        keys = []
        cnt = combine(key, 0)
        if cnt == n:
            break
    result = []
    for i in keys:
        result.append(i)
        result.append(bolts[i])

    print(f'#{_+1} {" ".join([str(i) for i in result])}')