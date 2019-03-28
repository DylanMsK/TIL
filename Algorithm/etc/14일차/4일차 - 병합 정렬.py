def merge_sort(lst):
    global cnt
    n = len(lst)
    if n <= 1:
        return lst
    elif n == 2:
        if lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
            cnt += 1
        return lst
    left = merge_sort(lst[0:n//2])
    right = merge_sort(lst[n//2:n])

    if left[-1] > right[-1]:
        cnt += 1

    result = [-1] * n

    left_len = len(left)
    right_len = len(right)
    
    while left_len > 0 or right_len > 0:
        if left_len > 0 and right_len > 0:
            if left[left_len-1] >= right[right_len-1]:
                result[n-1] = left[left_len-1]
                left_len -= 1
            else:
                result[n-1] = right[right_len-1]
                right_len -=1
            n -=1
        elif left_len > 0:
            result[:n] = left[:left_len]
            break
        elif right_len > 0:
            result[:n] = right[:right_len]
            break

    return result


for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    lst = merge_sort(lst)
    print(f'#{_+1} {lst[N//2]} {cnt}')