# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE'

T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for m in range(M)]
    temp = []
    for i in range(M-N+1):
        for j in range(M-N+1):
            sum_ = 0
            for k in arr[i:i+N]:
                sum_ += sum(k[j:j+N])
            temp.append(sum_)
    print(f'#{_+1} {max(temp)}')
