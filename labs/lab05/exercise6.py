# Getting input from users
minutesTime = float(input("Enter time in minutes:"))

# Converting into hour
hoursTime = float(minutesTime // 60)
excessTime = float(minutesTime % 60)

# Displaying the output
print ("Original minutes are " + str(minutesTime))
print(str(hoursTime) + " Hours " + str(excessTime) + " Minutes ")