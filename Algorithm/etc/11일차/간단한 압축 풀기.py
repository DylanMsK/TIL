for _ in range(int(input())):
    N = int(input())
    result = ''
    for i in range(N):
        s = input().split()
        result += s[0] * int(s[1])

    print("#{}".format(_+1))
    for i in range(0, len(result), 10):
        print(result[i:i+10])