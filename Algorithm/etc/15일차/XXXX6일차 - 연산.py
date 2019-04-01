for tc in range(int(input())):
    N, M = map(int, input().split())

    q = [N]
    cnt = 0
    calc = []
    while 1:
        if M in q:
            break

        nxt = []
        while q:
            num = q.pop(0)
            
            if num -1 > 0 and num - 1 not in nxt:
                nxt.append(num-1)
            if num - 10 > 0 and num -10 not in nxt:
                nxt.append(num-10)
            if num+1 not in nxt and num+1 <= 1000000:
                nxt.append(num+1)
            if num*2 not in nxt and num*2 <= 1000000:
                nxt.append(num*2)

        cnt += 1
        q = nxt[:]
    print('#{} {}'.format(tc+1, cnt))