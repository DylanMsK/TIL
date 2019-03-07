# url = 'https://www.acmicpc.net/problem/2659'

def find_min(num):
    init = [i for i in str(num)]
    num1 = int(''.join(init[1:] + init[:1]))
    num2 = int(''.join(init[2:] + init[:2]))
    num3 = int(''.join(init[3:] + init[:3]))
    num4 = int(''.join(init[::-1]))
    return min(num1, num2, num3, num4)

num = int(''.join(input().split()))
timenum = find_min(num)

result = []
for i in range(1111, timenum):
    if '0' in str(i):
        continue
    if find_min(i) not in result:
        result.append(i)
        
print(len(result) + 1)