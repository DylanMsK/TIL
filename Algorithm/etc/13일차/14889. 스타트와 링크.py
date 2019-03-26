# url = 'https://www.acmicpc.net/problem/14889'
from itertools import combinations

def combi(n, r):
    res = 1
    for i in range(n, n-r, -1):
        res *= i
    for i in range(r, 1, -1):
        res //= i
    return res


N = int(input())
arr = [[0] + list(map(int, input().split())) if i != 0 else [0]*(N+1) for i in range(N+1)]

length = combi(N, N//2) // 2
cnt = 0
diff = N*50
for cnt, i in enumerate(combinations(range(1, N+1), N//2)):
    if cnt == length:
        break
    teamA = i
    teamB = [_ for _ in range(1, N+1) if _ not in teamA]
    scoreA, scoreB = 0, 0
    for x in range(N//2-1):
        for y in range(x+1, N//2):
            scoreA += arr[teamA[x]][teamA[y]] + arr[teamA[y]][teamA[x]]
            scoreB += arr[teamB[x]][teamB[y]] + arr[teamB[y]][teamB[x]]
    if abs(scoreA - scoreB) < diff:
        diff = abs(scoreA - scoreB)
        if diff == 0:
            break

print(diff)