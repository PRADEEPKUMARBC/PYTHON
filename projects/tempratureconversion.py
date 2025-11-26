# Python temprature conversion

unit = input("Is thtemprature is in celsius or fahrenheit (C or F) : ")
temp = float(input("Enter the temprature : "))

if unit == "C":
    temp = temp * 9/5 + 32
    unit = "F°"
    print(f"temprature in fahrenheit is : {temp} {unit}")
elif unit == "F":
    temp = (temp - 32) * 5/9
    unit = "C°"
    print(f"temprature in celsius : {temp} {unit}")
else:
    print(f" {unit} is Invalid Unit")