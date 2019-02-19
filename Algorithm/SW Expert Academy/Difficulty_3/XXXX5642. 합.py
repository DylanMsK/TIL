# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXQm2SqdxkDFAUo&categoryId=AWXQm2SqdxkDFAUo&categoryType=CODE'

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    sum_ = max(lst)
    cnt = 2
    while cnt <= len(lst):
        for i in range(len(lst)-cnt+1):
            temp = sum(lst[i:i+cnt])
            if temp > sum_:
                sum_ = temp
        cnt += 1

    print(f"#{_+1} {sum_}")