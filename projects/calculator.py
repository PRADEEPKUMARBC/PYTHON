# Python Calculator

operator = int(input("Enter the operator (+,-,*,/) : "))
num1 = int(input("Enter the first number  : "))
num2 = int(input("Enter the second number : "))

if operator == "+" :
    sum = num1 + num2
    print(round(sum))
elif operator == "-" :
    diff = num1 - num2
    print(round(diff))
elif operator == "*" :
    mul = num1 * num2
    print(round(mul))
elif operator == "/" :
    div = num1 / num2
    print(round(div))
else :
    print("Invalid Operator")