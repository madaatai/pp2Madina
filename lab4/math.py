from math import *

def fromDegreeToRadian():
    degree = int(input('Input degree: '))
    radian = degree * pi / 180
    return f"Output radian: {radian}"

def areaOfTrapezoid():
    h = int(input('Height: '))
    a = int(input("Base, first value: "))
    b = int(input("Base, second value: "))
    return (a + b) * h / 2

def areaOfPolygon():
    n = int(input('Number of sides: '))
    s = int(input('Length of a side: '))
    area = (n * s ** 2) / (4 * tan(pi / n))
    return f"Area of polygon: {area}"

def areaOfParallellogram(a, b, angle):
    a = int(input('First side: '))
    b = int(input('Second side: '))
    angle = int(input('Angle: '))
    area = a * b * sin(angle)
    return f"Area of parallellogram: {area}"