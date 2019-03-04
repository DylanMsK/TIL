# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b-QGqADMBBASw&categoryId=AV2b-QGqADMBBASw&categoryType=CODE'

def find_loaction(num):
    init = 1
    row_diff = 1
    for x in range(99):
        col_diff = row_diff
        col = init
        for y in range(99):
            if col == num:
                return (x + 1, y + 1)
            elif col > num:
                break
            col = col + col_diff
            col_diff += 1
        row_diff += 1
        init += row_diff


for _ in range(int(input())):
    a, b = map(int, input().split())
    a_loc, b_loc = find_loaction(a), find_loaction(b)

    init = 1
    x_diff = 2
    x = 1
    while x < a_loc[0] + b_loc[0]:
        init += x_diff
        x_diff += 1
        x += 1
    y_diff = a_loc[1] + b_loc[1]
    y = 1
    while y < a_loc[1] + b_loc[1]:
        init += y_diff
        y_diff += 1
        y += 1

    print("#{} {}".format(_+1, init))