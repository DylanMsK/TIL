# url = 'https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWhVVhNaS8EDFAW_&contestProbId=AV139KOaABgCFAYh&probBoxId=AWhZCuG6gTsDFAW_+&type=PROBLEM&problemBoxTitle=1%EC%9B%9417%EC%9D%BC&problemBoxCnt=++1+'


import sys
sys.stdin = open('input.txt', 'r')

# for _ in range(10):
#     dump = int(input())
#     boxes = list(map(int, input().split()))
#     avg = int(sum(boxes) / 100)
#     temp = 0
#     cnt = []
#     for i in range(100, 0, -1):
#         if i in boxes:
#             temp += boxes.count(i)
#             cnt.append(temp)
#         else:
#             cnt.append(temp)

#     for i in cnt:
#         dump -= i
#         if dump == 0:

#     print(f'#{_+1}\n{cnt[::-1]}')



for _ in range(10):
    dump = int(input())
    sort = sorted(list(map(int, input().split())))
    for i in range(dump):
        sort = sorted(sort)
        if sort[-1] - sort[0] <= 1:
            break
        sort[-1] -= 1
        sort[0] += 1
    print(f'#{_+1} {max(sort)-min(sort)}')