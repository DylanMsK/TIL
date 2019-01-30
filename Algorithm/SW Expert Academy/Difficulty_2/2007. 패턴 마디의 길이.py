# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE'



for _ in range(int(input())):
    s = input()
    l = 0
    for i in range(1, 11):
        if s[:i] == s[i:2*i]:
            l = i
            break
    print(f'#{_+1} {l}')