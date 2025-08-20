# 1. Square: given side -> perimeter and area
side = float(input("Enter side of square: "))
perimeter = 4 * side
area = side ** 2
print("Square perimeter:", perimeter)
print("Square area:", area)

# 2. Circle: given diameter -> length (circumference)
import math
diameter = float(input("\nEnter diameter of circle: "))
length = math.pi * diameter   # circumference = π * d
print("Circle length:", length)

# 3. Mean of two numbers
a = float(input("\nEnter first number (a): "))
b = float(input("Enter second number (b): "))
mean = (a + b) / 2
print("Mean of a and b:", mean)

# 4. Sum, product and square of each number
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2

print("\nSum of a and b:", sum_ab)
print("Product of a and b:", product_ab)
print("Square of a:", square_a)
print("Square of b:", square_b)
