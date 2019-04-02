# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-Un3G64SUDFAXr&categoryId=AV-Un3G64SUDFAXr&categoryType=CODE'

for tc in range(int(input())):
    N, M = map(int, input().split())
    lst1 = input().split()
    lst2 = input().split()
    lst1.sort()
    lst2_length = {}
    for idx, s in enumerate(lst2):
        if len(s) not in lst2_length:
            lst2_length[len(s)] = [idx, idx]
        else:
            if idx < lst2_length[len(s)][0]:
                lst2_length[len(s)][0] = idx
            elif idx > lst2_length[len(s)][0]:
                lst2_length[len(s)][1] = idx
    
    cnt = 0
    for s in lst1:
        if len(s) in lst2_length:
            if s in lst2[lst2_length[len(s)][0]:lst2_length[len(s)][1]+1]:
                cnt += 1

    print(f'#{tc+1} {cnt}')