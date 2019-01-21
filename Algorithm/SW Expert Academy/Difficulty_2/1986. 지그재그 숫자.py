# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PxmBqAe8DFAUq&categoryId=AV5PxmBqAe8DFAUq&categoryType=CODE'


for _ in range(int(input())):
    print(f'#{_+1} {sum([i if i % 2 else -i for i in range(1, int(input())+1)])}')