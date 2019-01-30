# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PR4DKAG0DFAUq&categoryId=AV5PR4DKAG0DFAUq&categoryType=CODE'

import sys
sys.stdin = open('input.txt', 'r')


base64 = [chr(i) for i in range(ord('A'), ord('Z')+1)]
base64 += [chr(i) for i in range(ord('a'), ord('z')+1)]
base64 += [str(i) for i in range(10)]
base64 += ['+', '/']

def incoding(num):
    lst = [0]*6
    for i in range(5, -1, -1):
        if not num:
            break
        if num >= 2**i:
            num -= 2**i
            lst[5-i] += 1
    s = ''.join([str(i) for i in lst])
    return s

def decoding(bit):
    num = 0
    for i in range(7, -1, -1):
        if int(bit[7-i]):
            num += 2**i
    return num


for _ in range(int(input())):
    s = input()
    raw = ''
    for i in range(0, len(s), 4):
        for j in s[i:i+4]:
            raw += incoding(base64.index(j))
    result = ''
    for i in range(0, len(raw), 8):
        num = decoding(raw[i:i+8])
        result += chr(num)
    print(f'#{_+1} {result}')