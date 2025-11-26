# Python Weight converter

weight = float(input("Enter the weight : "))
unit = input("Kilograms or pounds (K or L) : ")

if unit == "K":
    weight = weight * 2.20462
    unit = "kgs"
elif unit == "L":
    weight = weight / 2.20462
    unit = "lbs"
else :
    print(f" {unit} is Invalid Unit")

print(f"your weight is : {weight} {unit}")