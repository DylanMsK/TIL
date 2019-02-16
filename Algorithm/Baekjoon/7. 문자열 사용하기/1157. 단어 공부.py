# url = 'https://www.acmicpc.net/problem/1157'

import sys

string = sys.stdin.readline().strip().upper()
char_dict = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}
for i in string:
    char_dict[i] += 1

nums = sorted(char_dict.items(), key=lambda x: x[1])
if nums[-1][1] == nums[-2][1]:
    print('?')
else:
    print(nums[-1][0])