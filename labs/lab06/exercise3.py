#Getting input from user
full_name = input("Enter your full name:")

#Converting case and counting length
upper_case_full_name = full_name.upper()
lower_case_full_name = full_name.lower()

#Displaying output
print("Uppercase:" + upper_case_full_name)
print("Lowercase:" + lower_case_full_name)
print("Length:" + (str(len(full_name))))