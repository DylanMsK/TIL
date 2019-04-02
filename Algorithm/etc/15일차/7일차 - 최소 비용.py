for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [[0]*N for _ in range(N)]
    q = [(0, 0)]
    while 1:
        nxt = []
        while q:
            now = q.pop(0)



    print('#{}'.format(tc+1))