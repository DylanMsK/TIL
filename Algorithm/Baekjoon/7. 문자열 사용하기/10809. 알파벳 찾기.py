# url = 'https://www.acmicpc.net/problem/10809'


x = input()
for i in range(ord('a'), ord('z')+1):
    if chr(i) in x:
        print(x.index(chr(i)), end=' ')
    else:
        print('-1', end=' ')
