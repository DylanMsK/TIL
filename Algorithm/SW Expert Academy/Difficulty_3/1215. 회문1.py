# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE'

def palind(arr, l):
    cnt = 0
    for y in range(len(arr)):
        for x in range(len(arr)-l+1):
            flag = 1
            for s in range(l//2):
                if arr[y][x+s] != arr[y][x+l-1-s]:
                    flag = 0
                    break
            if flag:
                cnt += 1
            flag = 1
            for s in range(l//2):
                if arr[x+s][y] != arr[x+l-1-s][y]:
                    flag = 0
                    break
            if flag:
                cnt += 1
    return cnt

for _ in range(10):
    l = int(input())
    arr = [input() for i in range(8)]
    cnt = palind(arr, l)
    print(f"#{_+1} {cnt}")