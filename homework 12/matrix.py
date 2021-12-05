class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def str(self):
        print(self.x, self.y)
class Matrix2x2:
    def __init__(self, s = [[0,0], [0,0]]):
        self.s = s
    def set(self, i, j, x):
        self.s[i-1][j-1] = x
    def add(self, second):
        new = Matrix2x2([[self.s[0][0] + second.s[0][0],self.s[0][1] + second.s[0][1]],
                         [self.s[1][0] + second.s[1][0],self.s[1][1] + second.s[1][1]]])
        return new
    def add2(self, second):
        self.s[0][0] += second.s[0][0]
        self.s[0][1] += second.s[0][1]
        self.s[1][0] += second.s[1][0]
        self.s[1][1] += second.s[1][1]
        return self
    def sub(self, second):
        new = Matrix2x2([[self.s[0][0] - second.s[0][0], self.s[0][1] - second.s[0][1]],
                         [self.s[1][0] - second.s[1][0], self.s[1][1] - second.s[1][1]]])
        return new
    def sub2(self, second):
        self.s[0][0] -= second.s[0][0]
        self.s[0][1] -= second.s[0][1]
        self.s[1][0] -= second.s[1][0]
        self.s[1][1] -= second.s[1][1]
        return self
    def multNumber(self, x):
        new = Matrix2x2([[self.s[0][0] * x, self.s[0][1] * x],
                         [self.s[1][0] * x, self.s[1][1] * x]])
        return new
    def multNumber2(self, x):
        self.s[0][0] *= x
        self.s[0][1] *= x
        self.s[1][0] *= x
        self.s[1][1] *= x
        return self
    def mult(self, second):
        new = Matrix2x2([[self.s[0][0] * second.s[0][0] + self.s[0][1] * second.s[1][0],
                          self.s[0][0] * second.s[0][1] + self.s[0][1] * second.s[1][1]],
                         [self.s[1][0] * second.s[0][0] + self.s[1][1] * second.s[1][0],
                          self.s[1][0] * second.s[0][1] + self.s[1][1] * second.s[1][1]]])
        return new
    def mult2(self, second):
        newself00 = self.s[0][0] * second.s[0][0] + self.s[0][1] * second.s[1][0]
        newself01 = self.s[0][0] * second.s[0][1] + self.s[0][1] * second.s[1][1]
        newself10 = self.s[1][0] * second.s[0][0] + self.s[1][1] * second.s[1][0]
        self.s[1][1] = self.s[1][0] * second.s[0][1] + self.s[1][1] * second.s[1][1]
        self.s[0][0] = newself00
        self.s[0][1] = newself01
        self.s[1][0] = newself10
        return self
    def det(self):
        return self.s[0][0] * self.s[1][1] - self.s[0][1] * self.s[1][0]
    def transpon(self):
        self.s[0][1], self.s[1][0] = self.s[1][0], self.s[0][1]
        return self
    def inverseMatrix(self):
        if self.det() == 0:
            return print('Error 404 (обратной матрицы не существует)'), print([0,0]), print([0,0])
        else:
            a = 1 / self.det()
            new = (self.transpon()).multNumber(a)
            new.s[0][0], new.s[1][1] = new.s[1][1],  new.s[0][0]
            return new
    def equivalentDiagonal(self):
        self.s[1][0] = 0
        self.s[0][1] = 0
        return self
    def multVector(self, vector):
        newvec = Vector2D(self.s[0][0] * vector.x + self.s[0][1] * vector.y,
                          self.s[1][0] * vector.x + self.s[1][1] * vector.y)
        return newvec


first = Matrix2x2([[1,1], [1,1]])
second = Matrix2x2([[9,-6], [6,-4]])
vector = Vector2D(3,4)
first.multVector(vector).str()
