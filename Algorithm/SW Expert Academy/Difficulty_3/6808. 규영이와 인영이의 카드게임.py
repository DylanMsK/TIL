# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWgv9va6HnkDFAW0&categoryId=AWgv9va6HnkDFAW0&categoryType=CODE'

for _ in range(int(input())):
    a = list(map(int, input().split()))
    b = [i for i range(1, 19) if i not in a]
    

    print(f'#{_+1} {} {}')