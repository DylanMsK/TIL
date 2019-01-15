# url = 'https://www.acmicpc.net/problem/1475'


n = input()

lst = [n.count(str(i)) if i not in [6, 9] else 0 for i in range(10)]
nums = n.count('6') + n.count('9')
cnt = max(lst)
if cnt * 2 >= nums:
    print(cnt)
else:
    nums -= cnt*2
    while nums > 0:
        cnt += 1
        nums -= 2
    print(cnt)
