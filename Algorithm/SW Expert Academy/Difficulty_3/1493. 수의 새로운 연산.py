# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b-QGqADMBBASw&categoryId=AV2b-QGqADMBBASw&categoryType=CODE'

def new_num(x, y):
    return ((x * (x+1)) // 2) + (x * (y-1)) + ((y-1) * (y-2) // 2)


for _ in range(int(input())):
    a, b = map(int, input().split())
    a_loc, b_loc = (), ()
    for x in range(1, 150):
        for y in range(1, 150):
            if new_num(x, y) == a:
               a_loc = (x, y)
            if new_num(x, y) == b:
                b_loc = (x, y)
            elif new_num(x, y) > a and new_num(x, y) > b:
                continue
        if a_loc and b_loc:
            break

    num_loc = (a_loc[0]+b_loc[0], a_loc[1]+b_loc[1])
    result = new_num(num_loc[0], num_loc[1])

    print("#{} {}".format(_+1, result))