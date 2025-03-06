import string
zattxt="C:\\Users\\Aldo\\Desktop\\github.python\\python\\lab6\\zat.txt"
with open(zattxt) as zat:
    data=zat.read()
print(len(list(data.split("\n"))))