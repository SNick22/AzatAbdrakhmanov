import time, codecs
f = codecs.open('log.txt', 'w', 'utf-8')


def printing(func):
    def wrap(*args):
        f.write('Функция вызвалась в ' + str(time.ctime()) + '\n')
        a = time.time()
        res = func(*args)
        b = time.time()
        f.write('Функция закончила выполнение в ' + str(time.ctime()) + '\n')
        f.write('Время выполнения функции ' + str(b-a) + ' секунд' + '\n')
        f.write('Аргументы функции ' + str('{}'.format(*args)) + '\n')
        f.write('Результат выполнения  ' + str(res))
        return res
    return wrap


@printing
def example(y):
    time.sleep(2)
    return y**2


example(24)
