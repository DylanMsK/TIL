# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PwGK6AcIDFAUq&categoryId=AV5PwGK6AcIDFAUq&categoryType=CODE'

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(int(input())):
    N, K = map(int, input().split())
    scores = []
    for i in range(N):
        M, F, A = map(int, input().split())
        score = (M * 0.35) + (F * 0.45) + (A * 0.2)
        scores.append(score)
    K = scores[K-1]
    K = (sorted(scores, reverse=True).index(K)) // (N // 10)
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    
    print(f'#{_+1} {grade[K]}')