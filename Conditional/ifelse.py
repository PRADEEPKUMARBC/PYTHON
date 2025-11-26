# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age : "))

if age >= 18:
    print("you are eligible to vote")
elif age < 0 :
    print("you haven't been born yet")
else :
    print("you must be 18+ be signed up to vote ")