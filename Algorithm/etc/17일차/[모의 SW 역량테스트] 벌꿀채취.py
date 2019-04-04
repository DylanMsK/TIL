import sys
sys.stdin = open('input.txt', 'r')

def get_ggul(tong, C):
    max_ = 0
    for i in range(1 << len(tong)):
        temp, sum_ = [], 0

        for j in range(len(tong)):
            if i & 1 << j:
                sum_ += tong[j]
                if sum_ > C:
                    break
                temp.append(tong[j])
        sum_ = 0
        for ggul in temp:
            sum_ += ggul ** 2
        
        if sum_ > max_:
            max_ = sum_
    
    return max_


for tc in range(int(input())):
    N, M, C = map(int, input().split())

    ggultong = list(map(int, input().split()))
    for _ in range(N-1):
        ggultong += [-1] + list(map(int, input().split()))
    
    max_ = 0
    for i in range(len(ggultong)):
        for j in range(i+M, len(ggultong)):
            if len(ggultong[i:i+M]) == M and -1 not in ggultong[i:i+M]\
                 and len(ggultong[j:j+M]) == M and -1 not in ggultong[j:j+M]:
                sum_ = get_ggul(ggultong[i:i+M], C) + get_ggul(ggultong[j:j+M], C)
                if sum_ > max_:
                    max_ = sum_
            else:
                continue

    print(f'#{tc+1} {max_}')