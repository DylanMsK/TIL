
n = int(input())

for idx, i in enumerate(range(n)):
    time = list(map(int, input().split()))

    hour = time[0] + time[2]
    minute = time[1] + time[-1]
    if minute >= 60:
        minute -= 60
        hour += 1
    if hour > 12:
        hour -= 12
    print(f'#{idx+1} {hour} {minute}')