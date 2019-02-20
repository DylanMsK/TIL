import sys
sys.stdin = open('/Users/dylan/Desktop/github/TIL/Algorithm/SW Expert Academy/Intermediate/Flatten_input.txt', 'r')

for _ in range(10):
    dump = int(input())
    lst = list(map(int, input().split()))

    height = {}
    min_, max_ = 100, 0
    for i in lst:
        if i < min_:
            min_ = i
        if i > max_:
            max_ = i
        if i not in height:
            height[i] = 0
            height[i] += 1
        else:
            height[i] += 1
    temp = list(height.keys())
    while dump >= 0:
        if height[temp[-1]] == 0:
            temp.pop()
        if height[temp[0]] == 0:
            temp = temp[1:]
        
        height[temp[-1]] -= 1
        height[temp[-2]] += 1
        height[temp[1]] += 1
        height[temp[0]] -= 1
        dump -= 1


    print(f'#{_+1} {temp[-1]-temp[0]}')