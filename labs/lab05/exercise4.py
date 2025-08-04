# Getting input from users
itemName1 = str(input("Enter item 1 name:"))
item1 = float(input("Enter item 1 price:RM"))
itemName2 = str(input("Enter item 2 name:"))
item2 = float(input("Enter item 2 price:RM"))
itemName3 = str(input("Enter item 3 name:"))
item3 = float(input("Enter item 3 price:RM"))
taxPercentage = float(0.06)

# Calculating subtotal, tax amount, total amount
subTotal = float(item1 + item2 + item3)
taxAmount = float(subTotal * taxPercentage)
totalAmount = float(subTotal + taxAmount)

# Displaying the output
print("Your subtotal is:RM" + str(round(subTotal,2)))
print("Your tax amount is:RM" + str(round(taxAmount,2)))
print("Your total amount is:RM" + str(round(totalAmount,2)))