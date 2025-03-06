import re
with open("row1-7.txt") as lol:
    data=lol.read()

print("Exercise-1")
matching=re.findall("a.*b", data)
print(matching)

print("Exercise-2")
matching=re.findall("a.*bb+|abbb+", data)
print(matching)

print("Exercise-3")
matching=re.findall("[a-z]_+[a-z]+", data)
print(matching)

print("Exercise-4")
matching=re.findall(r"[A-Z][a-z]+", data)
print(matching)

print("Exercise-5")
matching=re.findall(r"a+.b", data)
print(matching)

print("Exercise-6")
matching=re.sub(r"[., ]",':', data)
print(matching)

print("Exercise-7")
matching=re.sub(r"_",'', data)
print(matching)