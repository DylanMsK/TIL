# url = 'https://www.acmicpc.net/problem/2292'

"""
초기값 1, 등비 6인 수열
"""


n = int(input())

cnt, temp = 0, 1
while n > temp:
    temp  += cnt*6
    cnt += 1
    
print(1) if n == 1 else print(cnt)