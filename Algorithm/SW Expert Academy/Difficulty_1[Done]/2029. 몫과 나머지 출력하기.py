n = int(input())

for i in range(n):
    x = input().split()
    a, b = int(x[0]), int(x[-1])
    print(f'#{i+1} {a//b} {a%b}')