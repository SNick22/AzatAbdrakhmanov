class RationalFraction:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def reduce(self):
        for i in range(min(abs(self.x), abs(self.y)), 0, -1):
            if self.x % i == 0 and self.y % i == 0:
                self.x //= i
                self.y //= i
                break
    def add(self, a):
        summ = RationalFraction(self.x * a.y + a.x * self.y, self.y * a.y)
        summ.reduce()
        return summ
    def add2(self, a):
        self.x = self.x * a.y + a.x * self.y
        self.y = self.y * a.y
        self.reduce()
        return self
    def sub(self, a):
        dif = RationalFraction(self.x * a.y - a.x * self.y, self.y * a.y)
        dif.reduce()
        return dif
    def sub2(self, a):
        self.x = self.x * a.y - a.x * self.y
        self.y = self.y * a.y
        self.reduce()
        return self
    def mult(self, a):
        mul = RationalFraction(self.x * a.x, self.y * a.y)
        mul.reduce()
        return mul
    def mult2(self, a):
        self.x *= a.x
        self.y *= a.y
        self.reduce()
        return self
    def div(self, a):
        mul = RationalFraction(self.x * a.y, self.y * a.x)
        mul.reduce()
        return mul
    def div2(self, a):
        self.x *= a.y
        self.y *= a.x
        self.reduce()
        return self
    def str(self):
        print(self.x, '/', self.y)
    def value(self):
        return self.x / self.y
    def equals(self, a):
        if self.value() > a.value():
            print('k>a')
        if self.value() == a.value():
            print('k=a')
        if self.value() < a.value():
            print('k<a')
    def numberPart(self):
        return self.x // self.y

k = RationalFraction(8,2)
a = RationalFraction(1,4)
print(k.numberPart())