# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PmkDKAOMDFAUq&categoryId=AV5PmkDKAOMDFAUq&categoryType=CODE'

for _ in range(int(input())):
    lst = [input() for i in range(int(input()))]
    s = ''
    for i in lst:
        temp = i.split()
        s += temp[0] * int(temp[1])

    print(f'#{_+1}')
    for i in range(0, len(s), 10):
        print(s[i:i+10])