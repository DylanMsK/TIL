# url = 'https://www.acmicpc.net/problem/10871'

N, X = map(int, input().split())
A = list(map(int, input().split()))

print(' '.join([str(A[i]) for i in range(N) if A[i] < X]))