for _ in range(int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    for i in range(M):
        lst.append(lst.pop(0))

    print(f'#{_+1} {lst[0]}')



# 다른방법
# for _ in range(int(input())):
#     N, M = map(int, input().split())
#     lst = list(map(int, input().split()))
#     print(f'#{_+1} {lst[M%N]}')