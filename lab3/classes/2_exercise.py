class shape():
    def area(self):
        return 0
class square(shape):
    def __init__(self, leng):
        self.leng=leng
    def area(self):
        return self.leng * self.leng

side=float(input("Enter side: "))   
mysquare=square(side)
print("Area of square:", mysquare.area())
myshape=shape()
print("Area of shape:", myshape.area())