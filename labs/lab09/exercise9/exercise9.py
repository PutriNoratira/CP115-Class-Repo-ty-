applicant_age = int(input())
vision_test = input()
written_score = int(input())
driving_score = int(input())
medical_clearance = input()

# TODO: Your code here
# Initialize a counter
requirements_met = 0

if vision_test.lower() == 'pass':
    requirements_met += 1

if written_score >= 80:
    requirements_met += 1

if driving_score >= 85:
    requirements_met += 1

if medical_clearance.lower() == 'pass':
    requirements_met += 1

# Determine the license class based on requirements met and age
if requirements_met == 4 and applicant_age >= 21:
    license_class = "Class A (Commercial)"
elif requirements_met == 4 and applicant_age >= 18:
    license_class = "Class B (Regular)"
elif requirements_met == 2 or requirements_met == 3:
    license_class = "Restricted License"
else:
    license_class = "Application Denied"

print(license_class)