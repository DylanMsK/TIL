def my_len(s):
    cnt = 0
    for _ in s:
        cnt += 1
    return cnt

def my_int(string):
    sum_ = 0
    cnt = 0
    for s in string[::-1]:
        sum_ += (ord(s)-ord('0')) * (10**cnt)
        cnt += 1
    return sum_

for _ in range(my_int(input())):
    s1, s2 = input(), input()
    res = 0
    for i in range(my_len(s2)-my_len(s1)+1):
        if s1 == s2[i:i+my_len(s1)]:
            res = 1
            break
    print(f'#{_+1} {res}')