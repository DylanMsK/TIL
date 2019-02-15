# url = 'https://www.acmicpc.net/problem/1181'

# def my_word_soring(lst):
#     for i in range(len(lst)):
#         min_ = i
#         for j in range(i+1, len(lst)):
#             idx = 0
#             while idx < 4:
#                 if ord(lst[min_][idx]) == ord(lst[j][idx]):
#                     idx += 1
#                 elif ord(lst[min_][idx]) > ord(lst[j][idx]):
#                     min_ = j
#                     break
#                 else:
#                     break
#         lst[i], lst[min_] = lst[min_], lst[i]
#     return lst

lst = [''] * int(input())
for _ in range(len(lst)):
    lst[_] = input()

# for i in sorted(sorted(set(lst)), key=len):
#     print(i)

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

for i in sorted(string_dict.keys()):
    for j in sorted(string_dict[i]):
        print(j)