# SWEA Difficulty2

### [1204. 최빈수 구하기](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE)

```python
for _ in range(int(input())):
    T = int(input())
    lst = list(map(int, input().split()))
    score = max(lst, key=lst.count)
    print(f'#{T} {score}')
```
