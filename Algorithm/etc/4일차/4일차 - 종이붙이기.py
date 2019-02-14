import sys
sys.stdin = open('종이붙이기_input.txt', 'r')


for _ in range(int(input())):
    n = int(input()) // 10
    tot = 1
    cnt = 1
    while cnt < n:
        cnt += 1
        if cnt % 2 == 0:
            tot = (tot*2) + 1
        else:
            tot = (tot*2) - 1
    print(f'#{_+1} {tot}')