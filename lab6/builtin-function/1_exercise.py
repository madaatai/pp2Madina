import math
def prod():
    try:
        numbers=list(map(int, input("Enter the num:").split()))
        if not numbers:
            print("Error")
            return
        result=math.prod(numbers)
        print(result)
    except ValueError:
        print("Enter valid value")

prod()