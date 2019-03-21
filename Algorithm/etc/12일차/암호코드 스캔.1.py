import sys
sys.stdin = open('scan_input.txt', 'r')

bin_dict = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}


def hex_to_bin(hex):
    hex = hex.replace('1', '0001')
    hex = hex.replace('2', '0010')
    hex = hex.replace('3', '0011')
    hex = hex.replace('4', '0100')
    hex = hex.replace('5', '0101')
    hex = hex.replace('6', '0110')
    hex = hex.replace('7', '0111')
    hex = hex.replace('8', '1000')
    hex = hex.replace('9', '1001')
    hex = hex.replace('A', '1010')
    hex = hex.replace('B', '1011')
    hex = hex.replace('C', '1100')
    hex = hex.replace('D', '1101')
    hex = hex.replace('E', '1110')
    hex = hex.replace('F', '1111')
    return hex

    
def find_hexa(binary):
    temp = binary[::-1]
    mul = 1
    while 1:
        temp = temp.lstrip('0')
        nums = ''
        for i in range(0, len(temp), mul):
            if len(nums) == 7:
                break
            nums += i
        if nums[::-1] in bin_dict:
            break
    








for _ in range(int(input())):
    N, M = map(int, input().split())

    bin_code = []
    for i in range(N):
        row = input()
        if row.count('0') == M:
            continue
        temp = hex_to_bin(row.strip('0'))
        if temp not in bin_code:
            bin_code.append(temp)

    print(f'#{_+1} ')
    break