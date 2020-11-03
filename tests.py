from complex import complex
import math

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

print ("test puissance 1")
a = complex(0, 1)
assert (a ** 6) == complex(-1, 0)
print("ok")
a **= 6
print ("test puissance 2")
assert a == complex(-1, 0)
print("ok")

print ("test module 1")
assert a.module() == 1
print ("ok")
print ("test module 2")
assert Ob2.module() == 13**0.5
print ("ok")

print ("test argument 1")
assert a.arg() == math.pi
print ("ok")
print ("test argument 2")
assert abs(Ob2.arg(True) - 56.3099) < 0.0001
print ("ok")
