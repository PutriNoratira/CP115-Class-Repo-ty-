#Storing variable
item_name = "Coffee"
price_item = 3.50

#Getting input
quantity_item = (int(input("How much coffee you bought:")))

#Calculating total
total_price = price_item * quantity_item

# Creating a formatted table
customer_receipt = "==========RECEIPT==========\n\nItem\tPrice\tQuantity\tTotal\nCoffee\t$3.50\t2\t\t$7.00\n\n==========================="
print(customer_receipt)