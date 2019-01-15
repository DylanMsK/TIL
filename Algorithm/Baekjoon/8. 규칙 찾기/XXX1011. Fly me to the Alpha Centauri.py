# url = 'https://www.acmicpc.net/problem/1011'

n = int(input())

for i in range(n):
    x = input().split()
    a, b = int(x[0]), int(x[-1])

    
    
    cnt = 1
    if b-a == cnt:
        print(cnt)
        continue
        
    while 1:
        if cnt*(cnt+1)/2 > b-a:
            if b-a > cnt*(cnt-1)/2+1:
                break
            else:
                cnt -= 1
                break
        cnt += 1

    print(cnt+1)