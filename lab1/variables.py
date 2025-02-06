x = 4
y = "asd"
print(x)
print(y)

x = "asd"
# is the same as
x = 'asd'


x = 4
y = "asd"
print(type(x))
print(type(y))

a = 9
A = "dsa"
#A will not overwrite a


myVariableName = "asd"
MyVariableName = "asd"
my_variable_name = "asd"

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


x = y = z = "hhh"
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = "awesome"

def Myfunc():
  print("Python is " + x)

Myfunc()


x = "awesome"

def Myfunc():
  x = "fantastic"
  print("Python is " + x)

Myfunc()

print("Python is " + x)


# Exercise 1
carname = "ferrari"

# Exercise 2
x = 50

# Exercise 3
x = 5
y = 10
print(x + y)

# Exercise 4
x = 5
y = 10
z = x + y
print(z)

# Exercise 5
x, y, z = "Orange", "Banana", "Cherry"

# Exercise 6
x = y = z = "Orange"

# Exercise 7
def myfunc():
    global x
    x = "fantastic"