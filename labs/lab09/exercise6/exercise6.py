position = input()
overtime_hours = int(input())
is_weekend = input()

# Base Hourly Rate
if position == "Manager":
    base_hourly_rate = 30.00
elif position == "Supervisor":
    base_hourly_rate = 20.00
elif position == "Staff":
    base_hourly_rate = 15.00
elif position == "Intern":
    base_hourly_rate = 8.00
else:
    base_hourly_rate = 0.00

# Overtime Pay calculation
if overtime_hours <= 8:
    overtime_pay = overtime_hours * base_hourly_rate * 1.5
else:
    overtime_pay = (8 * base_hourly_rate * 1.5) + ((overtime_hours - 8) * base_hourly_rate * 2.0)

# Weekend bonus rule (RM5/hour)
if is_weekend == "Yes":
    overtime_pay += overtime_hours * 5

print(overtime_pay)