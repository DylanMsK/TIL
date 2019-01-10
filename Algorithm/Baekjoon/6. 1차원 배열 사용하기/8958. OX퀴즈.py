# url = 'https://www.acmicpc.net/problem/8958'

n = int(input())

for i in range(n):
    scores = input()
    result = 0
    temp = 0
    for j in scores:
        if j == 'O':
            temp += 1
            result += temp
        else:
            temp = 0

    print(result)