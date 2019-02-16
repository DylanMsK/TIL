# Algorithm
## isPrime
#### 소수(Prime Number)
소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.<br>예를 들어, 5는 1x5 또는 5x1로 수를 곱한 결과를 적는 유일한 방법이 그 수 자신을 포함하기 때문에 5는 소수이다.<br>그러나 6은 자신보다 작은 두 숫자(2×3)의 곱이므로 소수가 아닌데, 이렇듯 1보다 큰 자연수 중 소수가 아닌 것은 합성수라고 한다.<br>1과 그 수 자신 이외의 자연수로는 나눌 수 없는 자연수로 정의하기도 한다. - 위키피디아 -

#### 10000 이하의 정수에서 소수 구하기
1. 모든 수를 순회하며 계산 (4.012014 sec)
    ```python
    start = time.time()

    prime_nums = []
    for i in range(2, n+1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag:
            prime_nums.append(i)
    # print(prime_nums)

    print(time.time() - start)
    ```
2. 1번 방법에 break 추가 (0.460254 sec)
    ```python
    start = time.time()

    prime_nums = []
    for i in range(2, n+1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            prime_nums.append(i)
    # print(prime_nums)

    print(time.time() - start)
    ```
3. 소수로 나누어 지지 않는 수 (0.058916 sec)
    ```python
    start = time.time()

    prime_nums = [2]
    for i in range(2, n+1):
        flag = True
        for j in prime_nums:
            if i % j == 0:
                flag = False
                break
        if flag:
            prime_nums.append(i)
    # print(prime_nums)

    print(time.time() - start)
    ```
4. 에라토스테네스의 접근 (0.010469 sec)
    ```python
    start = time.time()

    temp_prime = list(0 if i in [0, 1] else i for i in range(n+1))
    for i in range(2, n+1):
        if i == 0:
            continue
        for j in range(i*2, n+1, i):
            temp_prime[j] = 0

    prime_nums = [i for i in temp_prime if i != 0]
    # print(prime_nums)

    print(time.time() - start)
    ```
5. 에라토스테네스의 체 + 루트 n까지만 확인 (0.003866 sec)
    ```python
    start = time.time()

    temp_prime = list(0 if i in [0, 1] else i for i in range(n+1))
    for i in range(2, round((n+1)**0.5):
        if i == 0:
            continue
        for j in range(i*2, n+1, i):
            temp_prime[j] = 0

    prime_nums = [i for i in temp_prime if i != 0]
    # print(prime_nums)

    print(time.time() - start)
    ```


## Stack
대표적인 LIFO(Last In First Out) 형태의 자료구조

- 자료구조: 자료를 선형으로 저장할 저장소

    - 저장소 자체를 스택이라고 부르기도 함
    - 스택에서 마지막 삽입된 원소의 위치를 top이라고 함

- 연산

    - 삽입: 스택에 자료를 저장, 보통 push라고 함
    - 삭제: 스택에서 자료를 꺼냄, 스택의 윗 부분부터 꺼내며 보통 pop이라고 함 







