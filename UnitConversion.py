
def length_conversion(number, ops):
    if ops == 1:
        convert = number / 1000
        return convert
    elif ops == 2 :
        convert = number * 1000
        return convert
    elif ops == 3:
        convert = number /1000 
        return convert
    elif ops == 4:
        convert = number / 100
        return convert
    elif ops == 5:
        convert = number * 100000
        return convert 
    elif ops == 6:
        convert = number / 100000
        return convert
    else:
        return "XX  Invalid Input XX"

def liquid_conversion(number,ops):
    if ops == 1:
        convert = number * 1000
        return convert
    elif ops == 2:
        convert = number / 1000
        return convert  
    else:
        return "Invalid Operation"
    

def temperature_conversion(number,ops):
    if ops == 1:
        convert = number * (9/5) + 32
        return convert
    elif ops == 2:
        convert = number + 273.15
        return convert
    elif ops == 3:
        convert = number * 1000
        return convert
    elif ops == 4:
        convert = (number - 32 ) * 5/9 + 273.15
        return convert
    elif ops == 5:
        convert = number - 273.15
        return convert
    elif ops == 6:
        convert = (number - 273.15)* 1.8 +32
        return convert
    else:
        return " XX  Invalid Operation  XX"



def weight_conversion(number,ops):
    if ops == 1:
        convert = number * 1000
        return convert
    elif ops == 2:
        convert = number * 2.205
        return convert
    elif ops == 3:
        convert = (32* number - 32)* 5/9
        return convert
    elif ops == 4:
        convert = number * 1000
        return convert
    elif ops == 5:
        convert = number * 453.6
        return convert
    elif ops == 6:
        convert = number / 2.205
        return convert
    else:
        return " XX  Invalid Operation  XX"


print("This is a Unit Converter")
value = int(input("Choose from following numbers :1.Length Conversion, 2.Liquid Conversion, 3.Temperature Conversion, 4.Weight Conversion: "))

if value == 1:
    val= int(input("1.Convert meter into kilometer, 2.Convert kilometer into meters , 3.Convert meter into centimeter, 4.Convert centimeter into meter, 5.Convert kilometer into centimeter, 6.Convert centimeter into kilometer: "))
    give_number =int(input("The value to convert: "))
    print(f"The converted value is {length_conversion(give_number,val)}")

elif value == 2:
    val= int(input("1.Convert liters into milliliters, 2.Convert milliliters into liters"))
    give_number =int(input("The value to convert: "))
    print(f"The converted value is {liquid_conversion(give_number,val)}")

elif value == 3:
    val= int(input("1.Convert celsius into fahrenheit, 2.Convert celsius into Kelvin , 3.Convert fahrenheit into celsius, 4.Convert fahrenheit into kelvin, 5.Convert kelvin into celsius, 6.Convert kelvin into fahrenheit: "))
    give_number =int(input("The value to convert: "))
    print(f"The converted value is {temperature_conversion(give_number,val)}")

elif value == 4:
    val= int(input("1.Convert kilogram into gram, 2.Convert kilogram into pounds, 3.Convert gram into kilogram, 4. Convert gram into pounds, 5.Convert pounds into gram, 6.Convert pounds into kilogram"))
    give_number =int(input("The value to convert: "))
    print(f"The converted value is {weight_conversion(give_number,val)}")
else:
    print("XX  Invalid Input  XX")


# if __name__ == "__main___":
#     main()
