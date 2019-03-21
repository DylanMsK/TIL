def get_deci(num, notation):
    deci = 0
    for i in range(len(num)):
        deci += int(num[i]) * notation ** (len(num)-1-i)
    return deci


def check(new, num2, tri):
    if abs(new - tri) % 3:
        return False
    
    power = 0
    for i in range(len(num2)):
        if abs(new - tri) < 3 ** i:
            power = i
            break

    for i in range(3):
        temp = num2[:]
        temp[-power] = str(i)
        if new == get_deci(temp, 3):
            return True
    return False


for _ in range(int(input())):
    num1 = list(input())
    num2 = list(input())
    bi, tri = get_deci(num1, 2), get_deci(num2, 3)

    for i in range(len(num1)):
        temp = num1[:]
        if temp[i] == '1':
            temp[i] = '0'
        else:
            temp[i] = '1'
        new = get_deci(temp, 2)
        if check(new, num2, tri):
            break
            
    print(f'#{_+1} {new}')