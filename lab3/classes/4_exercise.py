import math
class Points:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def show(self):
        print(f"Points are: ({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x=new_x
        self.y=new_y
    def distance(self, another_p):
        return math.sqrt((self.x-another_p.x)**2 + (self.y-another_p.y)**2)

a=float(input("x: "))
b=float(input("y: "))
p1=Points(a, b)
p2=Points(a, b)

p1.show()

k=float(input("x1: "))
l=float(input("y1: "))
p1.move(k, l)
p1.show()

print(f"Distance beetwen points: {p1.distance(p2)}")