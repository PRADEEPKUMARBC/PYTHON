
# name = input("Enter your full Name : ")
# phone_number = input("Enter your Phone Number : ")

# results = len(name)
# result = name.find("k")
# result = name.rfind("q")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.replace("_", " ")
# result = name.isalpha()


# print(results)
# print(result)
# print(name)

# result = phone_number.replace("-", "")

# print(result)

# Pradeepkumar b c

username = input("Enter a usename : ")

if len(username) < 10 :
    print("Username must be at least 10 characters")
elif not username.find("_") >= -1 :
    print("Username must contain _ ")
elif not username.isalpha():
    print("Username must only contain letters and _ ")
else:
    print( f" welcome {username} ")

