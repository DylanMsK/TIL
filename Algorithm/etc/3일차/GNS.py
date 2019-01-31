for _ in range(int(input())):
    T = input().split()
    print(T[0])
    s = b'%b' % input().encode()
    nums = {b'Z': 'ZRO', b'ON': 'ONE', b'W': 'TWO', b'HR': 'THR', b'OR': 'FOR', b'IV': 'FIV', b'X': 'SIX', b'VN': 'SVN', b'EG': 'EGT', b'NI': 'NIN'}
    for i in nums:
        print(f'{nums[i]} ' * s.count(i), end='')
    print()
