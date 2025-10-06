student_gpa = float(input())
total_score = int(input())
number_extracurricular = input()
completed_interview = input()

# TODO: Your code here
# Initialize a counter
met_requirements = 0

if student_gpa >= 3.0:
    met_requirements += 1

if total_score >= 1200:
    met_requirements += 1

if int(number_extracurricular) >= 1:
    met_requirements += 1

if completed_interview.lower() == 'yes':
    met_requirements += 1

# Determine the admission status
if met_requirements == 4:
    admission_status = "Accepted"
elif met_requirements == 3:
    admission_status = "Waitlisted"
else:
    admission_status = "Rejected"

print(admission_status)