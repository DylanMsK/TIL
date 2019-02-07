n = input()

for i in range(1, int(n)+1):
    cnt = 0
    if ('3' in str(i)) or ('6' in str(i)) or ('9' in str(i)):
        cnt += str(i).count('3') + str(i).count('6') + str(i).count('9')
    if cnt == 0:
        print(i, end=' ')
    else:
        print('-'*cnt, end=' ')