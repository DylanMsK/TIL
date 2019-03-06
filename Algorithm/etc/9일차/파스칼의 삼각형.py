for _ in range(int(input())):
    N = int(input())
    result = [[1]]
    for i in range(1, N):
        next = []
        for j in range(len(result[-1])+1):
            next.append(sum(result[-1][max(0, j-1):j+1]))
        result.append(next)

    print('#{}'.format(_+1))
    for i in result:
        print(' '.join([str(j) for j in i]))
