# url = 'https://www.acmicpc.net/problem/1427'

string = input()

nums_dict = {str(k): 0 for k in range(9, -1, -1)}
for s in string:
    nums_dict[s] += 1

for i in nums_dict:
    print(i * nums_dict[i], end='')
print()