# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE'




for _ in range(int(input())):
    N = int(input())
    change = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}
    for m in change.keys():
        quotient = N // m
        if quotient:
            N = N - (quotient) * m
            change[m] += quotient

    print(f'#{_+1}\n{" ".join([str(i) for i in change.values()])}')