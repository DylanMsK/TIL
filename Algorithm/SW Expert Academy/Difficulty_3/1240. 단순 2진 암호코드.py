# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE'
import sys
sys.stdin = open('input.txt', 'r')


def decode(binary):
    result = []
    for i in range(0, len(binary), 7):
        if binary[i:i+7] in nums:
            result.append(nums.index(binary[i:i+7]))
    return result


nums = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for _ in range(int(input())):
    N, M = map(int, input().split())
    code = []
    for i in range(N):
        row = input()
        print(row)
        if code:
            continue
        temp = decode(row)
        if temp:
            code = temp[:]
    result = 0
    print(code)
    if len(code) != 8:
        pass
    else:
        even = 0
        odd = 0
        for i in range(8):
            if i % 2:
                odd += code[i]
            else:
                even += code[i]
        if not (odd + 3*even) % 10:
            result = odd + even

    print(f'#{_+1} {result}')
    break

