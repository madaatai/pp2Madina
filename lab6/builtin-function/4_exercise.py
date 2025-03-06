import math
import time

def delayed_sqrt(number, del_milisec):
    time.sleep(del_milisec/1000)
    result=math.sqrt(number)
    print(f"Square root of {number} after {del_milisec} miliseconds is {result}")

number=int(input("Enter the num:"))
delay_ms=int(input("Enter delay in milliseconds:"))
delayed_sqrt(number, delay_ms)