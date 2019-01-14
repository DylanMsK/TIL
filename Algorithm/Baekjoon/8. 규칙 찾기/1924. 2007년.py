# url = 'https://www.acmicpc.net/problem/1924'


days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
m, d = map(int, input().split())
print(day[(sum(days[:m]) + d)%7])