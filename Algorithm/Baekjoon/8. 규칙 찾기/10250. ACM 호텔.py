# url = 'https://www.acmicpc.net/problem/10250'

t = int(input())

for i in range(t):
    x = list(map(int, input().split()))
    h, w, n = x[0], x[1], x[2]

    if n % h:
        floor = n % h
        ho = str((n//h)+1)
    else:
        floor = h
        ho = str(n//h)
    
    if len(ho) == 1:
        ho = '0' + ho

    print(f'{floor}{ho}')


# 다른사람 풀이
T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())
    print(((N-1)%H+1)*100 + (N-1)//H+1)