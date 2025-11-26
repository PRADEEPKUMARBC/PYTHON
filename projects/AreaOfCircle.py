# import math

# radius = int(input("Enter the radius of the circle : "))

# area = math.pi * pow(radius,2)

# print(f"the area of the circle is {round(area,2)} cm²")

import math

a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))

problem = pow(a,2) + pow(b,2)

c = math.floor(math.sqrt(problem))

print(f"The length of side c is: {c} cm")