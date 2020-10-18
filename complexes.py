#utilisation
#argument x la partie réel
#argument y la partie imaginaire
# + - * / += -= *= /= == != implémentés
# ** **= pas encore testés
 
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
    
     
    def __ipow__(self, other):
        save = self
        for i in range(0, puissance - 1):
            self *= save
        return self

def test_complexes():    
    Ob1 = complex(1, 2)
    Ob2 = complex(2, 3)
    Ob3 = complex(-4, 5)
    
    print ("test addition 1")
    assert complex(-2, 8) == Ob2 + Ob3
    print("ok")
    print ("test addition 2")
    Ob2 += Ob1
    assert complex(3, 5) == Ob2
    print("ok")
    
    print ("test soustraction 1")
    assert Ob2 - Ob3 == complex(7, 0)
    print("ok")
    print ("test soustraction 2")
    Ob2 -= Ob1
    assert Ob2 == complex(2, 3)
    print("ok")
    
    print ("test multiplication 1")
    assert Ob2 * Ob1 == complex(-4, 7)
    print("ok")
    Ob2 *= Ob3
    print ("test multiplication 2")
    assert Ob2 == complex(-23, -2)
    print("ok")
    
    print ("test division 1")
    Ob2 /= Ob3
    assert Ob2 == complex(2, 3)
    print("ok")
    print("test division 2")
    assert Ob3 / Ob1 == complex(1.2, 2.6)
    print ("ok")
    
    
    print ("test non egualitee 1")
    assert Ob2 != Ob1
    print ("ok")
    print ("test non egualitee 2")
    assert Ob2 != Ob3
    print ("ok")
    print ("test non egualitee 3")
    assert Ob1 != Ob3
    print ("ok")


test_complexes()