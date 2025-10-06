position = input()
overtime_hours = int(input())
is_weekend = input()

if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18
else:
    hourly_rate = 0

base_overtime = overtime_hours * (1.5 * hourly_rate)

weekend_bonus = 0
if is_weekend == "Yes":
    weekend_bonus = overtime_hours * 6

overtime_pay = base_overtime + weekend_bonus
total_pay = overtime_pay

print(hourly_rate)
print(overtime_pay)
print(total_pay)