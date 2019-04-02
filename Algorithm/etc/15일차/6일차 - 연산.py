for tc in range(int(input())):
    N, M = map(int, input().split())

    visited = [0] * 1000001
    cnt = 0
    q = [N]
    while 1:
        if M in q:
            break
        
        temp = [-1] * (len(q) * 4)
        idx = 0
        for i in range(len(q)):
            # -1
            if q[i]-1 > 0 and not visited[q[i]-1]:
                visited[q[i]-1] = 1
                temp[idx] = q[i]-1
                idx += 1
            # -10
            if q[i]-10 > 0 and not visited[q[i]-10]:
                visited[q[i]-10] = 1
                temp[idx] = q[i]-10
                idx += 1
            # +1
            if q[i]+1 < 1000001 and not visited[q[i]+1]:
                visited[q[i]+1] = 1
                temp[idx] = q[i]+1
                idx += 1
            # *2
            if q[i]*2 < 1000001 and not visited[q[i]*2]:
                visited[q[i]*2] = 1
                temp[idx] = q[i]*2
                idx += 1
        q = [i for i in temp if i != -1]
        cnt += 1

    print('#{} {}'.format(tc+1, cnt))