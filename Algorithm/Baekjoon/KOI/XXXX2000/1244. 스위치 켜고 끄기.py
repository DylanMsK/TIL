# url = 'https://www.acmicpc.net/problem/1244'

def boy(num):
    idx = num - 1
    while idx < len(switch):
        if switch[idx] == '0':
            switch[idx] = '1'
        else:
            switch[idx] = '0'
        idx += num


def girl(num):
    diff = 0
    idx = num - 1
    while 1:
        diff += 1
        if idx-diff < 0 or idx+diff >= len(switch):
            break
        if switch[idx-diff] == switch[idx+diff]:
            continue
        else:
            break
    diff -= 1
    for i in range(idx-diff, idx+diff+1):
        if switch[i] == '0':
            switch[i] = '1'
        else:
            switch[i] = '0'


N = int(input())
switch =input().split()
s_num = int(input())
for _ in range(s_num):
    sex, num = map(int, input().split())
    if sex == 1:
        boy(num)
    elif sex == 2:
        girl(num)

for i in range(0, len(switch), 20):
    print(" ".join(switch[i:i+20]))
