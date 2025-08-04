# Getting input from users
mark1 = float(input("Enter mark 1:"))
mark2 = float(input("Enter mark 2:"))
mark3 = float(input("Enter mark 3:"))

# Calculating totalScore, average
totalScore = float(mark1 + mark2 + mark3)
average = float(totalScore / 3)

# Displaying the output
print("Your mark 1 is " + str(mark1))
print("Your mark 1 is " + str(mark2))
print("Your mark 1 is " + str(mark3))
print("Your total mark is " + str(totalScore))
print("Your average mark is " + str(round((average))))