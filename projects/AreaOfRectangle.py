# Exercise 1: Calculate the area of a rectangle

width = int(input("Enter the width of the rectangle: "))
length = int(input("Enter the length of the rectangle: "))

rectangle = width * length

print(f"The area of the triangle is: {rectangle} cm²")

# Exercise 2: Shopping Cart Program

item = input("which item would you like to buy: ")
price = float(input(f"What is the price of {item}: "))
quantity = int(input(f"How many {item} would you like to buy: "))

total = price * quantity

print(f" you have bought {quantity} {item}")
print(f" Your total is: ${total}")