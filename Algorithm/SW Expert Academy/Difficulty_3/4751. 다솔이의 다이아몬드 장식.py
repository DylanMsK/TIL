# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWSNw5jKzwMDFAUr&categoryId=AWSNw5jKzwMDFAUr&categoryType=CODE'

def add(letter):
    global l1, l2, l3
    l1 += '.#..'
    l2 += '#.#.'
    l3 += '.{}.#'.format(letter)


for _ in range(int(input())):
    s = input()
    l1 = '..#..'
    l2 = '.#.#.'
    l3 = '#.{}.#'.format(s[0])
    for idx in range(1, len(s)):
        add(s[idx])

    print(l1)
    print(l2)
    print(l3)
    print(l2)
    print(l1)