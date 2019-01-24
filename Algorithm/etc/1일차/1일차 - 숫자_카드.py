# url = 'https://www.swexpertacademy.com/main/learn/course/lectureProblemViewer.do'

import sys
sys.stdin = open('숫자카드_input.txt', 'r')


T = int(input())
for _ in range(T):
    N = int(input())
    a = input()
    nums = {int(i): a.count(i) for i in set(a)}
    max_ = sorted(nums.values())[-1]
    max_key = []
    for key, val in nums.items():
        if val == max_:
            max_key.append(key)
    max_num = sorted(max_key)[-1]
    print(f'#{_+1} {max_num} {a.count(str(max_num))}')