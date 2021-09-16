#задание 4
print('Введите первую строку')
a = input()
print('Введите вторую строку')
b = input()
if (sorted(a) == sorted(b)) == 1:
    print ('Это анаграммы')
else:
    print ('Это не анаграммы')
#задание 5
arr = []
print ('Введите количество чисел в массиве')
n = int(input())
print ('Вводите цифры массива по одному')
for i in range (n):
    arr.append(input())
print(arr)
#создаём пустую строку, чтобы добавлять в неё цифры из массива
s = ''
for c in range (n):
    s += str(arr[c])
d = int(s) + 1
#преобразуем число обратно в массив
arr.clear()
for e in str(d):
    arr.append(e)
print(arr)
#задание 6
arr = []
print ('Введите количество чисел в массиве')
n = int(input())
print ('Вводите цифры массива по одному')
for i in range (n):
    arr.append(input())
print(arr)
print('Введите число')
a = int(input())
#отнимаем от числа по очереди каждый элемент массива и проверяем, находится ли результат разницы в массиве
k = 0
for i in range(n):
    b = int(arr[i])
    if (a-b) in arr:
        print('Числа', b, 'и', a-b, 'дают в сумме число', a)
        k += 1
        break
if k == 0:
    print ('Никакие два числа в массиве не дают в сумме', a)
