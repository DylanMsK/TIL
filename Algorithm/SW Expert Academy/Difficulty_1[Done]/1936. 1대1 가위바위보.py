x = input().split()

a, b = int(x[0]), int(x[-1])

if a == 1:
    if b == 2:
        print('B')
    else:
        print('A')
elif a == 2:
    if b == 1:
        print('A')
    else:
        print('B')
else:
    if b == 1:
        print('B')
    else:
        print('A')