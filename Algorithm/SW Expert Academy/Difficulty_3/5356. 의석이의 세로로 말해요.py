for _ in range(int(input())):
    string = [list(input()) for i in range(5)]
    max_ = len(max(string, key=lambda x: len(x)))
    result = ''
    for idx in range(max_):
        for s in string:
            if idx >= len(s):
                continue
            result += s[idx]

    print("#{} {}".format(_+1, result))