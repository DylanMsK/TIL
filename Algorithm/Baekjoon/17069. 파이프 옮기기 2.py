# url = 'https://www.acmicpc.net/problem/17069'
import collections


def horizontal(x, y, visited):
    global N, arr, q
    if x+1 < N and not arr[y][x+1]:
        visited.append((x+1, y))
        q.append((x+1, y, 1, visited))

def vertical(x, y, visited):
    global N, arr, q
    if y+1 < N and not arr[y+1][x]:
        visited.append((x, y+1))
        q.append((x, y+1, 2, visited))

def cross(x, y, visited):
    global N, arr, q
    if x+1 < N and y+1 < N and not arr[y+1][x+1] and not arr[y+1][x] and not arr[y][x+1]:
        visited.append((x+1, y+1))
        q.append((x+1, y+1, 3, visited))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
# position) 1: 가로, 2: 세로, 3: 대각선
q = collections.deque([(1, 0, 1, [(0, 1)])])
# q = [(1, 0, 1, [(0, 1)])]
while q:
    x, y, position, visited = q.popleft()
    if (x, y) == (N-1, N-1):
        cnt += 1
        continue

    if position == 1:
        horizontal(x, y, visited[:])
    elif position == 2:
        vertical(x, y, visited[:])
    else:
        horizontal(x, y, visited[:])
        vertical(x, y, visited[:])
    cross(x, y, visited[:])
print(cnt)



import sys

n = int(sys.stdin.readline())

num_lists=[0]*n

for a in range(n):
    num_lists[a] = list(map(int,sys.stdin.readline().split()))

cnt_lists=[[[0]*3 for b in range(n)] for a in range(n)]
cnt_lists[0][1][2]=1

for a in range(1,n*2-1):
    for b in range(a+1):
        if 0<=b<n and 0<=a-b<n:
            if num_lists[b][a-b]==0:
                if 0 <= b - 1 < n and 0 <= a - b < n:
                    if num_lists[b-1][a - b] == 0:
                        cnt_lists[b][a-b][0] += (cnt_lists[b-1][a-b][0] + cnt_lists[b-1][a-b][1])
                if 0 <= b - 1 < n and 0 <= a - b - 1 < n:
                    if num_lists[b-1][a-b]==0 and num_lists[b][a-b-1]==0:
                        cnt_lists[b][a-b][1] += (cnt_lists[b-1][a-b-1][0] + cnt_lists[b-1][a-b-1][1] + cnt_lists[b-1][a-b-1][2])
                if 0 <= b < n and 0 <= a - b - 1 < n:
                    if num_lists[b][a-b-1]==0:
                        cnt_lists[b][a-b][2] += (cnt_lists[b][a-b-1][2] + cnt_lists[b][a-b-1][1])
print(sum(cnt_lists[n-1][n-1]))



import sys

n = int(sys.stdin.readline())

num_lists=[0]*n

#num_lists에는 벽에 대한 정보가 저장
for a in range(n):
    num_lists[a] = list(map(int,sys.stdin.readline().split()))

#각 지점에서 파이프가 옮겨질수 있는 경우의 수를 저장할 리스트
cnt_lists=[[[0]*3 for b in range(n)] for a in range(n)]
cnt_lists[0][1][2]=1
#cnt_lists에는 그 지점에서 3방향으로 올 수 있는 방향의 값이 저장
#[아래쪽 방향 , 대각선 방향, 오른쪽 방향]
for a in range(1,n*2-1):
    for b in range(a+1):
        if 0<=b<n and 0<=a-b<n:
            if num_lists[b][a-b]==0:
                if 0 <= b - 1 < n and 0 <= a - b < n:#현재 지점에서 한칸 위가 범위내인지 검사
                    if num_lists[b-1][a - b] == 0:#현재 지점에서 한칸 위가 벽이 아님
                        #현재지점에 더해질수 있는 값은 한칸위의 값중 대각선으로 들어온 값과 같은 방향(아래쪽)으로 들어온 값
                        cnt_lists[b][a-b][0] += (cnt_lists[b-1][a-b][0] + cnt_lists[b-1][a-b][1])
                if 0 <= b - 1 < n and 0 <= a - b - 1 < n:#현재 지점에서 왼쪽대각선 위가 범위내인지 검사
                    if num_lists[b-1][a-b]==0 and num_lists[b][a-b-1]==0:#현재 지점에서 왼쪽대각선 위가 벽이 아님
                        #현재지점에서 더해질수 있는 값은 왼쪽대각선의 값중 모든방향으로 더해진 값
                        cnt_lists[b][a-b][1] += (cnt_lists[b-1][a-b-1][0] + cnt_lists[b-1][a-b-1][1] + cnt_lists[b-1][a-b-1][2])
                if 0 <= b < n and 0 <= a - b - 1 < n:#현재 지점에서 왼쪽이 범위 내인지 검사
                    if num_lists[b][a-b-1]==0:#현재 지점에서 왼쪽이 벽이 아님
                        #현재지점에서 더해질수 있는 값은 왼쪽 값중 대각선으로 들어온 값과 같은 방향(오른쪽)으로 들어온 값
                        cnt_lists[b][a-b][2] += (cnt_lists[b][a-b-1][2] + cnt_lists[b][a-b-1][1])

# cnt_lists의 맨마지막 배열에는 그 지점에서 [아래쪽방향,대각선방향,오른쪽방향] 으로 구해진 값들이 있으므로 모두 더하면 전체의 경우의 수                       
print(sum(cnt_lists[n-1][n-1]))