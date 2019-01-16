# url = 'https://www.acmicpc.net/problem/1546'

n = int(input())

score = list(map(int, input().split()))
new = [i/(max(score))*100 for i in score]
print('%.4f'%(sum(new)/n))