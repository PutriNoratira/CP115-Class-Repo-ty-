num_days = int(input())
danger_threshold = float(input())

# Initialize counters
total_temperature = 0.0
danger_days = 0

# Loop for the specified number of days
for i in range(num_days):
    daily_temperature = float(input())
    total_temperature += daily_temperature

    if daily_temperature > danger_threshold:
        danger_days += 1

# Calculate the average temperature
if num_days > 0:
    average_temp = total_temperature / num_days
else:
    average_temp = 0.0

# Print the final results
print(danger_days)
print(f"{average_temp:.1f}")