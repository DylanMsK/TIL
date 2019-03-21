import sys
sys.stdin = open('scan_input.txt', 'r')


hex_dict = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

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


def find_hex(string, M):
    if string.count('0') == M:
        return None
    zero = 1
    if len(string) <= 26:
        zero += 1
    elif len(string) <= 50:
        zero += 2
    elif len(string) <= 126:
        zero += 3
    elif len(string) <= 250:
        zero += 3
    else:
        zero += 3

    for i in string.split('0' * zero):
        if i and i.strip('0') not in hex_code:
            if i.strip('0'):
                hex_code.append(i.strip('0'))


def hex_to_bin(hex):
    binary = ''
    for c in hex:
        binary += hex_dict[c]
    return binary


def bin_to_deci(binary):
    deci = ''
    while 1:
        if binary[-1] == '0':
            binary = '0' + binary[:-1]
        else:
            break

    length = len(binary) // 56
    print(len(binary), length)
    print(binary)
    if length > 1 or len(binary) > 60 * length:
        temp = ''
        if len(binary) > 60 * length:
            length += 1
        for c in range(len(binary)-1, -1, -1*(length)):
            temp = binary[c] + temp
        if len(temp) % 56 != 0:
            temp = '0' * (len(temp) % 56) + temp
        binary = temp
    # print(binary)
    for idx in range(len(binary)-1, -1, -1):
        if binary[idx] == '0':
            print(binary)
            continue
        else:
            for c in range(idx+1, -1, -7):
                if len(deci) == 8:
                    break
                deci = bin_dict[binary[c-7:c]] + deci
            break
    return deci


def check(decimal):
    odd, even = 0, 0
    for i in range(len(decimal)):
        if i % 2:
            odd += int(decimal[i])
        else:
            even += int(decimal[i])
    if not (even * 3 + odd) % 10:
        return odd + even
    else:
        return 0


for _ in range(int(input())):
    N, M = map(int, input().split())
    print(N, M)

    hex_code = []
    for i in range(N):
        string = input()
        find_hex(string, M)
    print(hex_code)
    bin_code = []
    for hex in hex_code:
        if hex:
            bin_code.append(hex_to_bin(hex))

    print(bin_code)
    deci_code = []
    for binary in bin_code:
        # print(binary)
        deci_code.append(bin_to_deci(binary))
    print(deci_code)

    codes = []
    for code in deci_code:
        codes.append(check(code))
    print(codes)


    print(f'#{_+1} {sum(codes)}')
    print()