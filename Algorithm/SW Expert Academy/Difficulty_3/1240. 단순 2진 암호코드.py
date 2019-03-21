# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE'
import sys
sys.stdin = open('input.txt', 'r')


def decode(binary):
    if '1' not in binary:
        return None
    result = []
    idx = 0
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '1':
            idx = i+1
            break
    for i in range(idx, -1, -7):
        if binary[i-7:i] in nums:
            result.append(nums.index(binary[i-7:i]))
    return result[::-1]


nums = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for _ in range(int(input())):
    N, M = map(int, input().split())
    code = []
    for i in range(N):
        row = input()
        if code:
            continue
        code = decode(row)
    result = 0
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

