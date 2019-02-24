# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE'

for _ in range(int(input())):
    mem = input()
    cnt = 0
    temp = '0'
    for i in range(len(mem)):
        if mem[i] != temp:
            cnt += 1
            temp = mem[i]

    print(f'#{_+1} {cnt}')