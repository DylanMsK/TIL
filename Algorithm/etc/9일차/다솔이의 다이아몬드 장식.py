# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWSNw5jKzwMDFAUr&categoryId=AWSNw5jKzwMDFAUr&categoryType=CODE'

for _ in range(int(input())):
    s = input()
    l1 = '..#..'
    l2 = '.#.#.'
    l3 = '#.{}.#'.format(s[0])
    for idx in range(1, len(s)):
        l1 += '.#..'
        l2 += '#.#.'
        l3 += '.{}.#'.format(s[idx])

    print(l1)
    print(l2)
    print(l3)
    print(l2)
    print(l1)