n = int(input())
cal = {1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31}

for idx in range(n):
    date = input()
    year, month, day = date[:4], date[4:6], date[6:]
    if not (float(month) in cal.keys()) or not (float(day) in range(1, cal[float(month)]+1)):
        print(f'#{idx+1} -1')
    else:
        print(f'#{idx+1} {year}/{month}/{day}')