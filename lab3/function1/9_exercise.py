import math
def volume_of_sphere(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume

radius=int(input("Enter radius:"))
print("Volume of the sphere is:", volume_of_sphere(radius))