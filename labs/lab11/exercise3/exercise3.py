target_points = int(input())

# TODO: Your code here
# Initialize the counters
total_points = 0
rounds_played = 0

# Loop continues as long as the total is less
while total_points < target_points:
    points_added = int(input())
    
    # Add the new points
    total_points += points_added
    
    # Count this as one round
    rounds_played += 1

# Print the final results
print(total_points)
print(rounds_played)