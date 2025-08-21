import random
from random import choice, shuffle

restaurant_name = "THE SKY LARK"
restaurant_location = "B1, PEAK OF GALAS HILLS"
menu_1 = "CHICKEN TENDER"
menu_2 = "COCONUT MILKSHAKE"
menu_3 = "RIVER CHOCOLATE"

name_upper = restaurant_name.upper()
name_lower = restaurant_name.lower()
length_location = len(restaurant_location)

random_choice = choice (['1', '2', '3'])
customer_number = random.randint (100, 999)