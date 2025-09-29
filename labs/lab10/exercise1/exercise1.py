position = input()
overtime_hours = int(input())
is_weekend = input()

# 1. Use the correct base hourly rates for this exercise
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18
else:
    hourly_rate = 0

overtime_pay = overtime_hours * (1.5 * hourly_rate)

weekend_bonus = 0
if is_weekend == "Yes":
    weekend_bonus = overtime_hours * 5

# 4. Calculate the final total pay
total_pay = overtime_pay + weekend_bonus

print(hourly_rate)
print(overtime_pay)
print(total_pay)