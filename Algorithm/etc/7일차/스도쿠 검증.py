for _ in range(int(input())):
    arr = [list(map(int, input().split())) for i in range(9)]
    flag = True
    # Col & Row
    for i in range(9):
        tempR = [0] * 9
        tempC = [0] * 9
        for j in range(9):
            tempR[j] = arr[i][j]
            tempC[j] = arr[j][i]
        if len(set(tempR)) != 9 or len(set(tempC)) != 9:
            flag = False
            break

    if flag:
        # Box
        temp = [[0] * 9 for k in range(3)]
        for i in range(9):
            for j in range(0, 9, 3):
                temp[j // 3][((i % 3) * 3) + (j % 3)] = arr[i][j]
                temp[(j+1) // 3][((i % 3) * 3) + ((j+1) % 3)] = arr[i][j+1]
                temp[(j+2) // 3][((i % 3) * 3) + ((j+2) % 3)] = arr[i][j+2]

            if i in [2, 5, 8]:
                for t in temp:
                    if len(set(t)) != 9:
                        flag = False
                        break
                if flag:
                    temp = [[0] * 9 for k in range(3)]
                else:
                    break

    print("#{} {}".format(_+1, int(flag)))
