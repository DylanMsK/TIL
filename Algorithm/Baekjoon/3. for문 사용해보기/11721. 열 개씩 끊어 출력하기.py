# url = 'https://www.acmicpc.net/problem/11721'

# 다른사람
# st = input()
# for i in range(0,len(st),10):
#     print(st[i:i+10])



res = ''
for i in input():
    res += i
    if len(res)==10:
        print(res)
        res = ''
print(res)