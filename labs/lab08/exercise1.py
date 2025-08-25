score1 = 85
score2 = 92.5
score3 = 78

average = (score1 + score2 + score3) / 3
average_int = int(average)
print (f"{average}, type: {type(average)} \t {average_int}, type: {type(average_int)}\n")

random_calc = score1 ** 2 / score2 + score3 % 7
print (f"{random_calc}, type: {type(random_calc)}\n")

score_2 = int(score2)
score_1 = float(score1)
print(f"{score_2}, type: {type(score_2)} \t {score_1}, type: {type(score_1)}")
print ("\nThe result become different due to casting that we made, therefore, we practically change the data type of score 2 from float to integer and data type of score 1 from integer to float")