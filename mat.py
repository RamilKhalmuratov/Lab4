#Write a Python program to convert degree to radian.

import math

degree = float(input("Input degree: "))
radian = round(degree * (math.pi / 180), 6)
print("Output radian:", radian)

#Write a Python program to calculate the area of a trapezoid.

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area = 0.5 * (base1 + base2) * height
print("Expected Output:", area)

#Write a Python program to calculate the area of regular polygon.

import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = (n * s * s) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area)

#Write a Python program to calculate the area of a parallelogram.

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print(area)