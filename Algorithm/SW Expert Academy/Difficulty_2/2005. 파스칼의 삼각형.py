# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE'


T = int(input())
for _ in range(T):
    N = int(input())
    print(f'#{_+1}')
    print(1)
    init = [1, 1]
    for i in range(N-1):
        print(' '.join([str(__) for __ in init]))
        init = [1] + [sum(init[j:j+2]) for j in range(len(init)-1)] + [1]
