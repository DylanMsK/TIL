# url = 'https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWkIdD46A5EDFAXC&categoryId=AWkIdD46A5EDFAXC&categoryType=CODE'


for _ in range(int(input())):

    N = int(input())
    lst = []
    for i in range(N):
        lst.append(input())
    alp = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}
    for s in lst:
        alp[s[0]] += 1
    
    cnt = 0
    for i in alp:
        if alp[i]:
            cnt += 1
        else:
            break
    
    print(f'#{_+1} {cnt}')