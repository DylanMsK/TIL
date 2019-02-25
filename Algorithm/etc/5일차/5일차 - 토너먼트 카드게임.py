import sys
sys.stdin = open('C:\\Users\\student\\PycharmProjects\\TT\\python5\\카드게임_input.txt', 'r')


def win(group1, group2):
    flag = 1
    if group1[1] == 1:
        if group2[1] == 2:
            flag = 0
    elif group1[1] == 2:
        if group2[1] == 3:
            flag = 0
    else:
        if group2[1] == 1:
            flag = 0
    if flag:
        return group1
    return group2


def grouping(lst):
    if len(lst) == 2:
        winner = win(lst[0], lst[1])
        return winner

    elif len(lst) == 1:
        return lst[0]

    else:
        i = 1
        j = len(lst)

        if len(lst) % 2 == 0:
            group1 = lst[:(i+j)//2]
            group2 = lst[(i+j)//2:]

        else:
            group1 = lst[:(i+j)//2]
            group2 = lst[(i+j)//2:]

        group1 = grouping(group1)
        group2 = grouping(group2)
        return win(group1, group2)

for _ in range(int(input())):
    N = int(input())
    lst = [(i, j) for i, j in zip(range(1, N+1), list(map(int, input().split())))]
    winner = grouping(lst)
    print(f'#{_+1} {winner[0]}')

