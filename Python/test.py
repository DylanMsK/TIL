def my_3sqrt(x):
    n = 1
    m = x
    for t in range(1, 200):
        k = n+((m-n)/2)
        if k**3 > x:
            m = k
        elif k**3 < x:
            n = k
        else :
            return k
    return (m+n)/2

def my_sqrt1(n):
    a, b = 0, n
    result = 0
    while abs(result ** 2 - n) > 1e-4:
        result = (a+b)/2
        if result**2 < n:
            a = result
        else:
            b = result
    return result


print(my_sqrt1(8))