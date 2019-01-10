# url = 'https://www.acmicpc.net/problem/2920'

x = input().split()

asc = [str(i) for i in range(1, 9)]
desc = [str(i) for i in range(8, 0, -1)]
if x == asc:
    print('ascending')
elif x == desc:
    print('descending')
else:
    print('mixed')