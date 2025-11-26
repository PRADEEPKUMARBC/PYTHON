# while loop = execute some code WHILE some conditions remains true


# name = input("Enter your name : ")
# while name == "":
#     print("Please enter a valid name ")
#     name = input("Enter your name : ")

# print(f"Hello , {name} !")


# age = int(input("ENter your age : "))

# while age < 0:
#     print("age can not be negative")
#     age = int(input("ENter your age : "))

# print(f"Your age is {age} ")


# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter a another food you like ( q or quit ) : ")

# print("bye")


num = int(input("ENter a number between 0 - 10 : "))

while num < 0  or num > 10 :
    print(f"{num} is out of range")
    num = int(input("Enter a number between 0 - 10 : "))

print(f"your number is {num}")