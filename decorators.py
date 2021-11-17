import time

def printing(func):
    def wrap():
        a = time.time()
        res = func()
        b = time.time()
        print('Время выполнения функции',b-a,'секунд')
        return res
    return wrap

@printing
def example():
    for i in range(1000):
        for y in range(1000):
            2**y
    print(i)

example()