import sys
sys.stdin = open('/Users/dylan/Desktop/github/TIL/Algorithm/SW Expert Academy/Intermediate/View_input.txt', 'r')

for _ in range(10):
    row = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    idx = 2
    while idx <= row-2:
        temp = buildings[idx-2:idx] + buildings[idx+1:idx+3]
        if buildings[idx] > max(temp):
            cnt += buildings[idx] - max(temp)
            idx += 3
        else:
            idx += 1
            continue

    print(f'#{_+1} {cnt}')