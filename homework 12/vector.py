class Vector2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def add(self, a):
        sum = Vector2D(self.x + a.x, self.y + a.y)
        return sum
    def add2(self, a):
        self.x += a.x
        self.y += a.y
        return self
    def sub(self, a):
        dif = Vector2D(self.x - a.x, self.y - a.y)
        return dif
    def sub2(self, a):
        self.x -= a.x
        self.y -= a.y
        return self
    def mult(self, t):
        mul = Vector2D(self.x * t, self.y * t)
        return mul
    def mult2(self, t):
        self.x *= t
        self.y *= t
        return self
    def str(self):
        return self.x, self.y
    def len(self):
        return ((self.x)**2 + (self.y)**2)**0.5





k = Vector2D(3,5)
a = Vector2D(3,1)
print(k.str())
print(k.len())