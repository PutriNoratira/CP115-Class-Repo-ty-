import math

# Getting user input
circleRadius = float(input("Enter circle's radius:"))

# Calculating the area and circumference
circleArea = float(math.pi*(circleRadius**2))
circleCircumference = float(2*(math.pi*circleRadius))

# Displaying the output
print("The circle area:"+ str(circleArea))
print("The circle circumference:"+ str(circleCircumference))