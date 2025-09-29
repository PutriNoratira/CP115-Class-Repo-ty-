num_rounds = int(input())

# TODO: Your code here
# Initialize variables
final_score = 0.0
rounds_processed = 0

# Loop for the specified number of rounds
for i in range(num_rounds):
    round_score = int(input())
    
    # Apply the scoring rules
    if round_score > 100:
        final_score += round_score * 1.2
    else:
        final_score += round_score
        
    # Increment the counter
    rounds_processed += 1

# Print the final score formatted
print(f"{final_score:.1f}")

print(rounds_processed)