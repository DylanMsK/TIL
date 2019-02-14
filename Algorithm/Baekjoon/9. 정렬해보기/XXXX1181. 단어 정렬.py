# url = 'https://www.acmicpc.net/problem/1181'

n = int(input())
lst = [''] * n

for _ in range(n):
    lst[_] = input()

string_dict = {}
for s in lst:
    length = len(s)
    if length in string_dict:
        if s in string_dict[length]:
            continue
        else:
            string_dict[length].append(s)
    else:
        string_dict[length] = []
        string_dict[length].append(s)


print(string_dict)