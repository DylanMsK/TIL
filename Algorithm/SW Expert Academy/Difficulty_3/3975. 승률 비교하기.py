# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIX_iFqjg4DFAVH'


res = []
for tc in range(int(input())):
    A, B, C, D = map(int, input().split())
    if A / B > C / D:
        res.append('ALICE')
    elif A / B < C / D:
        res.append('BOB')
    else:
        res.append('DRAW')

for i in range(len(res)):
    print('#{} {}'.format(i+1, res[i]))
