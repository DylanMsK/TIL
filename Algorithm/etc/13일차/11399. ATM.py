# url = 'https://www.acmicpc.net/problem/11399'
import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

sum_ = 0
for i in range(N):
    sum_ += lst[i] * (N-i)

print(sum_)
