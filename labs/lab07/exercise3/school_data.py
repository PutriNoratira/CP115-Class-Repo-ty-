#Import math
import random
from math import sqrt

#Student Information
student_name = "Abdul Aidil Shah bin Ajibir"
student_id = "MC2515113649"
student_age = 18

#Course Information
course_code = "CP115"
course_name = "Computer Programming"

#Determining random score
score_1 = random.randint(70, 95)
score_2 = random.randint(75, 100)

#Calculating total score
total_score = score_1 + score_2

#String operation
upper_name = str(student_name.upper())
lower_name = str(student_name.lower())
length_name = len(student_name)

#Calculate square root 
sqrt_score = sqrt(total_score)