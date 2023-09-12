class Vector2D :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # + 연산에 대응 됩니다.
        if other.a :
            a = other.a
            b = other.b
        else :
            a = other
            b = other
        return Vector2D(self.x + a, self.y + b)

    def __mul__(self, other):
        return Vector2D((self.x * other.a)+100, (self.y * other.b)+100)

class test:
    def __init__(self, a, b):
        self.a = a
        self.b = b


v1 = Vector2D(1,2)
v2 = test(3,4)

print(100 * 200)
print(100.1 * 200.1)

v3 = v1 + v2
v4 = v1 * v2
print(v3.x, v3.y)
print(v4.x, v4.y)
