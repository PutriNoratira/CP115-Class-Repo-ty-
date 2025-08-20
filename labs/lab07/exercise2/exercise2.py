#import module
import shopping_data

#using variable from my own module
print ("===Using my own module===")
print(f"Product Bought\t\tCost/Item\tQuantity\t\tTotal Cost")
print(f"{shopping_data.product_1}\t\t\t{shopping_data.milk}\t\t{shopping_data.qty_milk}\t\t\t{shopping_data.total_milk}")
print(f"{shopping_data.product_2}\t\t\t{shopping_data.bread}\t\t{shopping_data.qty_bread}\t\t\t{shopping_data.total_bread}")
print(f"{shopping_data.product_3}\t\t{shopping_data.ice_cream}\t\t{shopping_data.qty_ice_cream}\t\t\t{shopping_data.total_ice_cream}")
print(f"{shopping_data.product_4}\t\t{shopping_data.chocolate}\t\t{shopping_data.qty_chocolate}\t\t\t{shopping_data.total_chocolate}")
