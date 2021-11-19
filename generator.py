def generator(limit):
    for i in range(2, limit+1):
        k = 0
        for s in range(1, i+1):
            if i%s == 0:
                k+=1
        if k == 2:
            yield i
my_generator = generator(101)
for i in my_generator:
    print(i)