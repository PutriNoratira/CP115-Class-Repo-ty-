# Getting user input (always returns a string)
studentName = input("Enter your name: ")
studentAge = int(input("Enter your age: "))
studentCourse = input("Enter your course code: ")

# Formatted output using string concatenation
print("Student: " + studentName + (str(type(studentName))))
print("Age: " + str(studentAge) + (str(type(studentAge))))
print("Course: " + studentCourse + (str(type(studentCourse))))