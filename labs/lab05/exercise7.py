import math

# Getting input from user
number = int(input("Choose a number"))

# Calculating square root, square (power of 2), cube (power of 3), and sine value
numberSq = float(math.sqrt(number))
numberPowerSq = float(number ** 2)
numberPowerCb = float(number ** 3)
numberSine = float(math.sin(number))

# Displaying the output
print("Square root of " + str(number) + " is " + str(numberSq))
print("Power of 2 of " + str(number) + " is " + str(numberPowerSq))
print("Power of 3 of " + str(number) + " is " + str(numberPowerCb))
print("Sine value of " + str(number) + " is " + str(numberSine))