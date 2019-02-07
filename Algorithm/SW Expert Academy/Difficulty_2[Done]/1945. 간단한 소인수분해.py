# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq&categoryId=AV5Pl0Q6ANQDFAUq&categoryType=CODE'


for _ in range(int(input())):
    N = int(input())
    temp = {i: 0 for i in [2, 3, 5, 7, 11]}
    for i in temp.keys():
        while N % i == 0:
            N = N // i
            temp[i] += 1

    print(f'#{_+1} {" ".join([str(i) for i in list(temp.values())])}')