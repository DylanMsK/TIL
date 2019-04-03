def dfs(x, y, length, string):
    global res
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return
    else:
        string += arr[y][x]
        if length == 7:
            # if string not in res:
            res.append(string)
        else:
            dfs(x+1, y, length+1, string)
            dfs(x-1, y, length+1, string)
            dfs(x, y+1, length+1, string)
            dfs(x, y-1, length+1, string)


for tc in range(int(input())):
    arr = [input().split() for _ in range(4)]
    res = []
    for y in range(4):
        for x in range(4):
            dfs(x, y, 1, arr[y][x])

    print(f'#{tc+1} {len(set(res))}')