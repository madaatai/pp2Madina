def fahrenheit_to_celcius(fahrenheit):
    celcius=(5/9)*(fahrenheit-32)
    return celcius
fahren=float(input("Enter a temperature in Fahrenheit:"))
celc=fahrenheit_to_celcius(fahren)
print(fahren, "fahrenheits equal to the", celc, "celcius")