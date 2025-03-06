import re
with open("row_8-10.txt") as lol:
    data=lol.read()
print("Exercise-8")
matching=re.findall(r"[A-Z][^A-Z]", data)
print(matching)

print("Exercise-9")
matching=re.findall("[A-Z][a-z]*", data)
print(matching)

print("Exercise-10")
matching=re.sub(r"[A-Z]",'_', data)
print(matching)