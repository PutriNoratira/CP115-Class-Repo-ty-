applicant_age = int(input())
vision_test = input()
written_score = int(input())
driving_score = int(input())
medical_clearance = input()

passed_core_reqs = (applicant_age >= 18 and vision_test.lower() == "pass" and written_score >= 80 and driving_score >= 85)
is_commercial_age = (applicant_age >= 21)
passed_medical = (medical_clearance.lower() == "pass")

if passed_core_reqs and is_commercial_age and passed_medical:
    license_class = "Class A (Commercial)"
elif passed_core_reqs:
    license_class = "Class B (Regular)"
else:
    total_reqs_met = (applicant_age >= 18) + (vision_test.lower() == "pass") + (written_score >= 80) + (driving_score >= 85) + passed_medical
                     
    if total_reqs_met >= 2:
        license_class = "Restricted License"
    else:
        license_class = "Application Denied"

print(license_class)