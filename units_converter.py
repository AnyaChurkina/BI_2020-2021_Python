a = input("Which parameter would you like to convert: length, weight, pressure, volume, speed?")
if a == "length":
    unit1 = input("Which unit would you like to convert from? Available units: sm/m/km")
    unit2 = input("Which unit would you like to convert to? Available units: sm/m/km")
    number = float(input("Enter your number: "))
    if unit1 == "sm" and unit2 == "m":
        result = number/100
    elif unit1 == "sm" and unit2 == "km":
        result = number/100000
    elif unit1 == "m" and unit2 == "sm":
        result = number*100
    elif unit1 == "m" and unit2 == "km":
        result = number/1000
    elif unit1 == "km" and unit2 == "m":
        result = number*1000
    elif unit1 == "km" and unit2 == "sm":
        result = number*100000
if a == "weight":
    unit1 = input("Which unit would you like to convert from? Available units: kg/g/mg")
    unit2 = input("Which unit would you like to convert to? Available units: kg/g/mg")
    number = float(input("Enter your number: "))
    if unit1 == "kg" and unit2 == "g":
        result = number*1000
    elif unit1 == "kg" and unit2 == "mg":
        result = number*1000000
    elif unit1 == "g" and unit2 == "mg":
        result = number*1000
    elif unit1 == "g" and unit2 == "kg":
        result = number/1000
    elif unit1 == "mg" and unit2 == "g":
        result = number/1000
    elif unit1 == "mg" and unit2 == "kg":
        result = number/1000000
if a == "pressure":
    unit1 = input("Which unit would you like to convert from? Available units: Pa/atm/Bar")
    unit2 = input("Which unit would you like to convert to? Available units: Pa/atm/Bar")
    number = float(input("Enter your number: "))
    if unit1 == "Pa" and unit2 == "Bar":
        result = number/100000
    elif unit1 == "Pa" and unit2 == "atm":
        result = number/101325
    elif unit1 == "atm" and unit2 == "Bar":
        result = number*1.013
    elif unit1 == "atm" and unit2 == "Pa":
        result = number*101325
    elif unit1 == "Bar" and unit2 == "Pa":
        result = number*100000
    elif unit1 == "Bar" and unit2 == "atm":
        result = number/1.013
if a == "volume":
    unit1 = input("Which unit would you like to convert from? Available units: L/ml")
    unit2 = input("Which unit would you like to convert to? Available units: L/ml")
    number = float(input("Enter your number: "))
    if unit1 == "L" and unit2 == "ml":
        result = number*1000
    elif unit1 == "ml" and unit2 == "L":
        result = number/1000
if a == "speed":
    unit1 = input("Which unit would you like to convert from? Available units: m/s, km/h")
    unit2 = input("Which unit would you like to convert to? Available units: m/s, km/h")
    number = float(input("Enter your number: "))
    if unit1 == "km/h" and unit2 == "m/s":
        result = number/3.6
    elif unit1 == "m/s" and unit2 == "km/h":
        result = number*3.6
else:
    print("Unknown parameter! Try again.")
print(result)
