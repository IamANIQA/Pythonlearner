names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
count_names = len(names)

import random

random_index = random.randint(0, count_names - 1)
random_name = names[random_index]

print(f"{random_name} is going to buy the meal today!")