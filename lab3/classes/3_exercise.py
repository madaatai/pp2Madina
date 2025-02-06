class Shape():
    def area(self):
        return 0
class Rectangle():
    def __init__(self, leng, width):
        self.leng=leng
        self.width=width
    def area(self):
        return self.leng * self.width
    
leng=float(input("Enter a lenght: "))
width=float(input("Enter a width: "))
myrect=Rectangle(leng, width)
print("Area of rectangle: ", myrect.area())