age = int(input())
accident_count = int(input())

if age < 25:
    base_premium = 2400
elif 25 <= age <= 50:
    base_premium = 1800
else:
    base_premium = 2000

if accident_count == 0:
    discount_amount = base_premium * 0.10
    final_premium = base_premium - discount_amount
else:
    discount_amount = 0
    if accident_count in (1, 2):
        final_premium = base_premium + 300
    else:  # accident_count >= 3
        final_premium = base_premium + 600

# Cast the final values to integers before printing
print(base_premium)
print(int(final_premium))
print(int(discount_amount))