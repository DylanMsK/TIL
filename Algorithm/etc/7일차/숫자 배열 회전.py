import sys
sys.stdin = open('숫자_input.txt', 'r')

def rotate(arr):
    row, col = len(arr), len(arr[0])
    brr = [[0] * col for i in range(row)]
    for y in range(row):
        for x in range(col):
            brr[x][col-1-y] = arr[y][x]
    return brr

for _ in range(int(input())):
    N = int(input())
    arr = list(input().split() for i in range(N))
    arr90 = rotate(arr)
    arr180 = rotate(arr90)
    arr270 = rotate(arr180)
    print(f'#{_+1}')
    for i in range(N):
        print(''.join(arr90[i]), ''.join(arr180[i]), ''.join(arr270[i]))



# Todo Linked list 
# def rotate(arr):
#     brr = [[0]*N for i in range(N)]
#     for i in range():
#         for j in range(N):
#             brr[i][j] = arr[N-1-j][i]
#     return brr



# for _ in range(int(input())):
#     N = int(input())
#     arr = [input().split() for i in range(N)]

#     print(f'#{_+1}')