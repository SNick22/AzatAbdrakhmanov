#задание 4
print('Введите первую строку')
a = input()
print('Введите вторую строку')
b = input()
if (sorted(a) == sorted(b)) == 1:
    print ('Это анаграммы')
else:
    print ('Это не анаграммы')