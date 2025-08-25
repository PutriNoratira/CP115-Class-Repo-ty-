main_dishes_qty = 3
main_dishes_price = 25
appetizers_qty = 2
appetizers_price = 12
drink_qty = 4
drink_price = 8

#calculating total bill and total price based on quantity, price each piece, tax and delivery fee
total_bill = (3 * 25) + (2 * 12) + (4 * 8)
total_price = total_bill + (total_bill * 0.10) + 5 #delivery fee
each_amount = int(total_price // 6)

print (f"Total Price is  RM{total_price}")
print (f"Each person need to pay RM{each_amount}")