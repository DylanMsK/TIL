# url = 'https://www.acmicpc.net/problem/1929'

M, N = map(int, input().split())

result = []
for num in range(M, N+1):
    if num == 1:
        continue
    if num < 11:
        if num in [2, 3, 5, 7]:
            result.append(num)
            continue
    else:
        if num % 2 == 0:
            continue
        elif num % 3 == 0:
            continue
        elif num % 5 == 0:
            continue
        elif num % 7 == 0:
            continue
        else:
            flag = True
            for i in result:
                if num % i == 0:
                    flag = False
                    break
            if flag:
                print(num)
                result.append(num)
 
for i in result:
    print(i)
    
    
    # if num < 11:
    #     if num in [2, 3, 5, 7]:
    #         print(num)
    #         continue
    # else:
    #     if num % 2 == 0:
    #         continue
    #     elif num % 3 == 0:
    #         continue
    #     elif num % 5 == 0:
    #         continue
    #     elif num % 7 == 0:
    #         continue
    #     else:
    #         flag = True
    #         for i in range(11, num):
    #             if num % i == 0:
    #                 flag = False
    #                 break
            
    #         if flag:
    #             print(num)
