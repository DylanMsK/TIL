# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14P0c6AAUCFAYi&categoryId=AV14P0c6AAUCFAYi&categoryType=CODE'

for _ in range(10):
    tc = input()
    sample = input()
    string = input()
    length = len(sample)
    cnt = 0
    for s in range(len(string)):
        if string[s] == sample[0]:
            if string[s:s+length] == sample:
                cnt += 1
            else:
                continue
    print(f"#{tc} {cnt}")
