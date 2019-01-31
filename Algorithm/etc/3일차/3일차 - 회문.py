def isPalindrom(arr, length):
    for i in range(len(arr)):
        for idx in range(len(arr)+1-length):
            for k in range(length//2):
                if arr[i][idx+k] != arr[i][idx+length-1-k]:
                    break
                elif k+1 == length//2:
                    return arr[i][idx:idx+length]
            for k in range(length//2):
                if arr[idx+k][i] != arr[idx+length-1-k][i]:
                    break
                elif k+1 == length//2:
                    temp = []
                    for l in range(idx, idx+length):
                        temp.append(arr[l][i])
                    return temp
    return 0


for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    print(f'#{_+1}', end=' ')
    if isPalindrom(arr, M):
        print(''.join(isPalindrom(arr, M)))