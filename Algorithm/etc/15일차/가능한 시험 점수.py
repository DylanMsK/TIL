for tc in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    scores = [0 for i in range(sum(nums)+1)]
    # scores = [0] * (sum(nums)+1)
    scores[0] = 1
    visited = [0]
    for num in nums:
        temp = visited[:]
        for i in temp:
            if not scores[i+num]:
                scores[i+num] = 1 
                visited.append(i+num)


    print('#{} {}'.format(tc+1, sum(scores)))

