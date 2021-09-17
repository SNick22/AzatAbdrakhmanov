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