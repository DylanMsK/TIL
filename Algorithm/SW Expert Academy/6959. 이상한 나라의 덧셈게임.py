# url = 'https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWjlH0k63joDFAVT&categoryId=AWjlH0k63joDFAVT&categoryType=CODE'
import sys
sys.stdin = open('C:\\Users\\student\\Desktop\\github\\TIL\\Algorithm\\SW Expert Academy\\input.txt', 'r')


for _ in range(int(input())):
    N = input().strip()

    flag = 1
    while len(N) > 1:
        N = str(int(N[0]) + int(N[1])) + N[2:]
        flag *= -1
    print(f"#{_+1} {'B' if flag > 0 else 'A'}")



    # cnt = 0
    # while len(N) > 1:
    #     result = ''
    #     length = len(N)
    #     if length % 2 == 1:
    #         for i in range(0, length-1, 2):
    #             result += str(int(N[i]) + int(N[i+1]))
    #             cnt += 1
    #         result += N[-1]
    #     else:
    #         for i in range(0, length, 2):
    #             result += str(int(N[i]) + int(N[i+1]))
    #             cnt += 1
    #     N = result
    # if cnt == 0:
    #     win = 'B'
    # elif cnt % 2 == 0:
    #     win = 'B'
    # else:
    #     win = 'A'
    # print(f"#{_+1} {win}")



