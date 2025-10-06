price = float(input())

# TODO: Your code here
# Initialize variables
total_cost = 0.0
item_count = 0

while price >= 0:
    total_cost += price
    item_count += 1
    price = float(input())

print(item_count)
print(f"{total_cost:.2f}")
