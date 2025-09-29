monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

# Initialize variables
interest_rate = 0.0
approval_status = "Rejected"
max_loan_amount = monthly_income * 5

# Check for approval
if monthly_income >= 4000 and credit_score >= 600 and loan_amount <= max_loan_amount:
    approval_status = "Approved"
    
    if credit_score >= 700:
        interest_rate = 3.5
    else:
        interest_rate = 5.5

print(interest_rate)
print(max_loan_amount)
print(approval_status)