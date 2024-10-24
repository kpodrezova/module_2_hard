n = int(input('Введите чисто от 3 до 20: '))
password = ''
for i in range(1, n):
    for j in range(1, n):
        if j <= i:
            continue
        if n % (i + j) == 0:
            password += str(i) + str(j)
print('Пароль: ', password)

