main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

# TODO: Your code here

# Main course prices
if main_course == "Chicken":
    main_course_cost = 10.00
elif main_course == "Beef":
    main_course_cost = 12.00
elif main_course == "Fish":
    main_course_cost = 11.00
else:
    main_course_cost = 0.00

# Drink prices
if drink == "Soft Drink":
    drink_cost = 2.00
elif drink == "Coffee":
    drink_cost = 3.00
else:
    drink_cost = 0.00

# Dessert prices
if dessert == "Ice Cream":
    dessert_cost = 4.00
elif dessert == "Cake":
    dessert_cost = 5.00
else:
    dessert_cost = 0.00

# Total food cost
total_food_cost = main_course_cost + drink_cost + dessert_cost

# Add 10% service charge
final_bill = total_food_cost * 1.10

# Discounts
if customer_age > 60:
    final_bill *= 0.85   # 15% off
elif customer_age < 18:
    final_bill *= 0.90   # 10% off

print(f"{final_bill:.2f}")