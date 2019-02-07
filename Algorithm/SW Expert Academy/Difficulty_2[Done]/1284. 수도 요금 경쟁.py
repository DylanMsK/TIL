# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV189xUaI8UCFAZN&categoryId=AV189xUaI8UCFAZN&categoryType=CODE'

for _ in range(int(input())):
    P,Q,R,S,W=map(int,input().split())
    A,B=P*W,max(Q,Q+max(W-R,0)*S)
    print(f'#{_+1} {min(A,B)}')