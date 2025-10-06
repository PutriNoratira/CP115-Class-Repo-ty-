# Problem: Teacher must count students first!
num_students = int(input("How many students? "))
total = 0

for i in range(num_students):
    grade = float(input("Enter grade: "))
    total += grade

average = total / num_students
print(f"Average: {average}")