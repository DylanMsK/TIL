# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PyTLqAf4DFAUq&categoryId=AV5PyTLqAf4DFAUq&categoryType=CODE'

T = int(input())
for _ in range(T):
    s = input().strip()
    if s == s[::-1]:
        result = 1
    else:
        result = 0
    print(f'#{_+1} {result}')