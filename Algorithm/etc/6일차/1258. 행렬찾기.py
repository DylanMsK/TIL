# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18LoAqItcCFAZN&categoryId=AV18LoAqItcCFAZN&categoryType=CODE'
import sys
sys.stdin = open('C:\\Users\\student\\Desktop\\github\\TIL\\Algorithm\\etc\\6일차\\행렬찾기_input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    arrays = []
    flag = True
    while flag:
        flag = False
        for y in range(n):
            for x in range(n):
                if arr[y][x]:
                    flag = True
                    lt = (y, x)
                    break
            if flag:
                break

        if flag:
            dx = dy = 0
            for y in range(lt[0], n):
                if arr[y][lt[1]] == 0:
                    break
                dy += 1

            for x in range(lt[1], n):
                if arr[lt[0]][x] == 0:
                    break
                dx += 1
            
            for y in range(lt[0], lt[0]+dy):
                for x in range(lt[1], lt[1]+dx):
                    arr[y][x] = 0

            arrays.append((dy, dx))

    arrays = sorted(arrays, key=lambda x: (x[0]*x[1], x[0]))

    print(f'#{_+1} {len(arrays)} {" ".join([str(j) for i in arrays for j in i])}')