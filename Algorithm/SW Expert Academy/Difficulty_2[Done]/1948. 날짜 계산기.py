# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PnnU6AOsDFAUq&categoryId=AV5PnnU6AOsDFAUq&categoryType=CODE'


for _ in range(int(input())):
    sm, sd, em, ed = map(int, input().split())
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = (sum(days[:em-1])+ed) - (sum(days[:sm-1])+sd) + 1
    print('#'+str(_+1), result)