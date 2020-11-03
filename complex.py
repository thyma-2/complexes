import math
#utilisation
#argument x la partie réel
#argument y la partie imaginaire
# + - * / += -= *= /= == != ** **= implémentés
 
class complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __add__(self, other):
        return complex(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)
    
    def __truediv__(self, other):
        a = complex(self.x * other.x + self.y * other.y, - self.x * other.y + self.y * other.x)
        b = other.x * other.x + other.y * other.y
        a.x /= b
        a.y /= b
        return a
        
    def __str__(self):
        return str(self.x) + " " + str(self.y) + "i"
        
    def  __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def  __isub_(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    
    def  __imul__(self, other):
        a = self.x * other.x - self.y * other.y
        b = self.x * other.y + self.y * other.x
        self.x = a
        self.y = b
        return self
    
    def __idiv__(self, other):
        a = self.x * other.x + self.y * other.y / other.x * other.x + other.y * other.y
        b = - self.x * other.y + self.y * other.x / other.x * other.x + other.y * other.y
        self.x = a
        self.y = b
        return self
    
    def __eq__(self, other):
        if (self.x == other.x):
            if (self.y == other.y):
                return True
        return False
    
    def __ne__(self, other):
        if (self.x == other.x):
            if (self.y == other.y):
                return False
        return True
    
    def __pow__(self, puissance):
        ret = complex(1,0)
        for i in range(0, puissance):
            ret *= self
        return ret
    
     
    def __ipow__(self, puissance):
        save = complex(self.x, self.y)
        for i in range(0, puissance - 1):
            self *= save
        return self

    def module(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def arg(self, deg : bool = False):
        mod = self.module()
        if deg == False:
            return math.acos(self.x / mod)
        return math.acos(self.x / mod) * 57.29577951
