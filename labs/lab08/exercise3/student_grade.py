#student marks
marks_1 = 78
marks_2 = 85
marks_3 = 92
marks_4 = 67
marks_5 = 88

total_points = (marks_1 + marks_2 + marks_3 + marks_4 + marks_5)
average = total_points / 5
percentage_score_1 = (marks_1 / total_points) * 100
percentage_score_2 = (marks_2 / total_points) * 100
percentage_score_3 = (marks_3 / total_points) * 100
percentage_score_4 = (marks_4 / total_points) * 100
percentage_score_5 = (marks_5 / total_points) * 100

print (f"Test\tEach Test Score\nTest 1\t{marks_1}\nTest 2\t{marks_2}\nTest 3\t{marks_3}\nTest 4\t{marks_4}\nTest 5\t{marks_5}")
print (f"Average score is {average}")
print (f"Total point is {total_points}")
print (f"Test\tEach Score Percentage Out Of Total Mark\nTest 1\t{percentage_score_1}\nTest 2\t{percentage_score_2}\nTest 3\t{percentage_score_3}\nTest 4\t{percentage_score_4}\nTest 5\t{percentage_score_5}")