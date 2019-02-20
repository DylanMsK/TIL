import sys
sys.stdin = open('/Users/dylan/Desktop/github/TIL/Algorithm/SW Expert Academy/Intermediate/최빈수_input.txt', 'r')

for _ in range(int(input())):
    tc = input()
    scores = list(map(int, input().split()))
    score_dict = {i: 0 for i in range(0, 101)}
    for score in scores:
        score_dict[score] += 1
    max_ = max(score_dict.keys(), key=lambda x: score_dict[x])
    print(f'#{tc} {max_}')