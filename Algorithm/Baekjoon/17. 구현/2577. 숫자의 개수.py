# url = 'https://www.acmicpc.net/problem/2577'

A = int(input())
B = int(input())
C = int(input())
mul = str(A * B * C)

num_dict = {str(i): 0 for i in range(10)}
for num in mul:
    num_dict[num] += 1
for i in num_dict.values():
    print(i)



# for i in range(10):
#     print(mul.count(str(i)))