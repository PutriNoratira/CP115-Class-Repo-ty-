import random

# Getting input from user
className = input("Enter your class name:")

# Generate random number
randomNumber = random.randint(1, 100)

# Displaying the output
print("Your random number is " + str(randomNumber))
print("Your class is " + className)