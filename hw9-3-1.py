#author: DMH 1/18/21

temp = float(input("What is the temp?"))
mode = input("Is this is Celsius or Fahrenheit?")
if mode.lower() == 'celsius':
        f = (temp * 1.8) + 32
        print(f + ' is the degrees in Fahrenheit')
if mode.lower() == 'fahrenheit':
        c = (temp - 32) * (5 / 9)
        print(c + ' is the degrees in celcius')
try:
    temp = float(input("What is the temp?"))
    mode = input("Is this is Celsius or Fahrenheit?")
    if mode.lower() == 'celsius':
        f = (temp * 1.8) + 32
        print(f + ' is the degrees in Fahrenheit')
    if mode.lower() == 'fahrenheit':
        c = (temp - 32) * (5 / 9)
        print(c + ' is the degrees in celcius')
except NameError:
    print("Please only type in either Celsius or Fahrenheit")
