day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()

# TODO your code here

# 1. Base price
if day_type == "Weekday":
    if customer_type == "Adult":
        base_price = 15
    elif customer_type == "Child":
        base_price = 10
    elif customer_type == "Senior":
        base_price = 12
else:  # weekend
    if customer_type == "Adult":
        base_price = 18
    elif customer_type == "Child":
        base_price = 12
    elif customer_type == "Senior":
        base_price = 15

# 2. Final price starts as base price
final_price = base_price

# 3. Evening surcharge (after 6pm)
if show_time > 18:
    final_price += 3

# 4. Student discount (weekdays only)
if is_student == "Yes" and day_type == "Weekday":
    final_price *= 0.9

print(base_price)
print(final_price)