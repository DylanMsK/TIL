# url = 'https://www.acmicpc.net/problem/1021'

N, M = map(int,input().split())
remove_idx = list(map(int, input().split()))
while remove_idx:
    idx = remove_idx[0]
    if N