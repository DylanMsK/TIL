# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHz7xD6A20DFAVB&categoryId=AWHz7xD6A20DFAVB&categoryType=CODE'

for tc in range(int(input())):
    N = int(input())
    num = ''
    while len(num) != N:
        temp = input().split()
        num += ''.join(temp)
    res = 0
    while 1:
        if str(res) not in num:
            break
        res += 1
    print(f'#{tc+1} {res}')