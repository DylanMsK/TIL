def isPalindrom(string, length):
    for i in range(100):
        for idx in range(101-length):
            for k in range(length//2):
                if string[i][idx+k] != string[i][idx+length-1-k]:
                    break
                elif k+1 == (length//2):
                    return length
            for k in range(length//2):
                if string[idx+k][i] != string[idx+length-1-k][i]:
                    break
                elif k+1 == (length//2):
                    return length
    return 0


for _ in range(10):
    print('#' + input(), end=' ')
    arr = [b'%b'%input().encode() for i in range(100)]

    for i in range(100, 0, -1):
        length = isPalindrom(arr, i)
        if length:
            print(length)
            break
