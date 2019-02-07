# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE'

import sys
sys.stdin = open('input.txt', 'r')

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


# 먼소리야??
# for i in range(int(input())):
#     n=int(input())
#     c=[input().split() for j in range(n)]
#     print(f'#{i+1}')
#     z=[]
#     for j in range(3):
#         e=list(zip(*reversed(c)))
#         z+=e
#         c=e
#     p=[''.join(list(i)) for i in z]
#     for k in range(n):
#        print(p[k],p[k+n],p[k+2*n])