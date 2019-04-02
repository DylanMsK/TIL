# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXQm2SqdxkDFAUo&categoryId=AWXQm2SqdxkDFAUo&categoryType=CODE'

for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))

    sum_ = 0
    for i in range(N):
        for j in range(i+1, N):
            if sum(lst[i:j]) > sum_:
                sum_ = sum(lst[i:j])

    print(f"#{_+1} {sum_}")