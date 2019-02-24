# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE'

def first_num(s_num):
    pass

for _ in range(int(input())):
    s_num, n = input().split()
    max_num = max(int(s_num))
    idx = 0
    for i in range(len(s_num)):
        if s_num[i] != max_num:
            continue
        

    print(f'#{_+1} ')