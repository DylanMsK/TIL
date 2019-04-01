# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWAe5G8afT0DFAUw&categoryId=AWAe5G8afT0DFAUw&categoryType=CODE'


for tc in range(int(input())):
    A, B = map(int, input().split())

    print('#{} {}'.format(tc+1, (A//B)**2))