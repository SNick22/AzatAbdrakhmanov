from abc import ABC, abstractmethod

class geometric_figure(ABC):
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
class circle(geometric_figure):
    def __init__(self, rad):
        """

        :param rad: circle radius
        """
        self.rad = rad
    def square(self):
        return (self.rad)**2 * 3.14
    def perimeter(self):
        return 2*(self.rad) * 3.14
class quadrangle(geometric_figure, ABC):
    def __init__(self, a, b):
        """

        :param a: left side
        :param b: top side
        """
        self.a = a
        self.b = b
class rectangle(quadrangle):
    def square(self):
        return self.a * self.b
    def perimeter(self):
        return (self.a + self.b)*2
class trapezoid(quadrangle):
    def __init__(self, a, b, c, d, h):
        """

        :param a: left side
        :param b: top side
        :param c: right side
        :param d: down side
        :param h: height
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h
    def square(self):
        return ((self.b + self.d)/2) * self.h
    def perimeter(self):
        return self.a + self.b + self.c + self.d
class parallelogram(quadrangle):
    def __init__(self, a, b, h):
        """

        :param a: left side
        :param b: top side
        :param h: height
        """
        self.a = a
        self.b = b
        self.h = h
    def square(self):
        return self.a * self.h
    def perimeter(self):
        return (self.a + self.b)*2
par = parallelogram(3,5,2)
krug = circle(10)
tr = trapezoid(4,3,8,6,5)
print(par.square())
print(krug.perimeter())
print(tr.square())