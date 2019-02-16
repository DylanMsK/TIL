# url = 'https://www.acmicpc.net/problem/2941'

s =  input()

alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in alp:
    cnt += s.count(i)
    s = ' '.join(s.split(i))

for i in s:
    if i == ' ':
        continue
    cnt += 1

print(cnt)



# cnt = 0
# idx = 0
# while idx < len(s):
#     if s[idx] == 'c':
#         if s[idx+1:idx+2] == '=':
#             cnt += 1
#             idx += 2
#             continue
#         elif s[idx+1:idx+2] == '-':
#             cnt += 1
#             idx += 2
#             continue
#         else:
#             cnt += 1
#             idx += 1
#             continue
#     elif s[idx] == 'd':
#         if s[idx+1:idx+3] == 'z=':
#             cnt += 1
#             idx += 3
#         elif s[idx+1:idx+2] == '-':
#             cnt += 1
#             idx += 2
#         else:
#             cnt += 1
#             idx += 1
#     elif s[idx] == 'l':
#         if s[idx+1:idx+2] == 'j':
#             cnt += 1
#             idx += 2
#         else:
#             cnt += 1
#             idx += 1
#     elif s[idx] == 'n':
#         if s[idx+1:idx+2] == 'j':
#             cnt += 1
#             idx += 2
#         else:
#             cnt += 1
#             idx += 2
#     elif s[idx] == 's':
#         if s[idx+1:idx+2] == '=':
#             cnt += 1
#             idx += 2
#         else:
#             cnt += 1
#             idx += 2
#     elif s[idx] == 'z':
#         if s[idx+1:idx+2] == '=':
#             cnt += 1
#             idx += 2
#         else:
#             cnt += 1
#             idx += 1
#     else:
#         cnt += 1
#         idx += 1
# print(cnt)

