# url = 'https://www.acmicpc.net/problem/10039'

scores = []
for i in range(5):
    scores.append(int(input()))

_sum = 0
for i in scores:
    if i <= 40:
        _sum += 40
    else:
        _sum += i

print(_sum//5)