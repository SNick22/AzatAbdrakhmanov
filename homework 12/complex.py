import math
class ComplexNumber:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b
    def add(self, second):
        new = ComplexNumber(self.a + second.a, self.b + second.b)
        return new
    def add2(self, second):
        self.a += second.a
        self.b += second.b
        return self
    def sub(self, second):
        new2 = ComplexNumber(self.a - second.a, self.b - second.b)
        return new2
    def sub2(self, second):
        self.a -= second.a
        self.b -= second.b
        return self
    def multNumber(self, number):
        new3 = ComplexNumber(self.a * number, self.b * number)
        return new3
    def multNumber2(self, number):
        self.a *= number
        self.b *= number
        return self
    def mult(self, second):
        new4 = ComplexNumber(self.a * second.a - self.b * second.b, self.a * second.b + second.a * self.b)
        return new4
    def mult2(self, second):
        newselfa = self.a * second.a - self.b * second.b
        self.b = self.a * second.b + second.a * self.b
        self.a = newselfa
        return self
    def div(self, second):
        new5 =  ComplexNumber((self.a * second.a + self.b * second.b) / (second.a ** 2 + second.b ** 2),
                              (second.a * self.b - self.a * second.b) / (second.a ** 2 + second.b ** 2))
        return new5
    def div2(self, second):
        newselfa = (self.a * second.a + self.b * second.b) / (second.a ** 2 + second.b ** 2)
        self.b = (second.a * self.b - self.a * second.b) / (second.a ** 2 + second.b ** 2)
        self.a = newselfa
        return self
    def len(self):
        return ((self.a)**2 + (self.b)**2)**0.5
    def str(self):
        if self.b >= 0:
            print(self.a, '+', self.b, '* i')
        else:
            self.b = -self.b
            print(self.a, '-', self.b, '* i')
    def arg(self):
        if self.a > 0:
            return math.atan(self.b / self.a)
        if self.a < 0 and self.b > 0:
            return math.pi + math.atan(self.b / self.a)
        if self.a < 0 and self.b < 0:
            return -math.pi + math.atan(self.b / self.a)
    def pow(self, double):
        t = self.len() ** double
        newselfa = t * math.cos(double * self.arg())
        self.b = t * math.sin(double * self.arg())
        self.a = newselfa
        return self
    def equals(self, second):
        if self.len() > second.len():
            print('модуль first >  модуль second')
        if self.len() == second.len():
            print('модуль first =  модуль second')
        if self.len() < second.len():
            print('модуль first <  модуль second')




first = ComplexNumber(2, 5)
second = ComplexNumber(-1, 1)
first.equals(second)