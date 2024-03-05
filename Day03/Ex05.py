print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

new_name1 = name1.lower()
new_name2 = name2.lower()

check_t = int(new_name1.count("t") + new_name2.count("t"))
check_r = int(new_name1.count("r") + new_name2.count("r"))
check_u = int(new_name1.count("u") + new_name2.count("u"))
check_e = int(new_name1.count("e") + new_name2.count("e"))

total1 = check_t + check_r + check_u + check_e

check_l = int(new_name1.count("l") + new_name2.count("l"))
check_o = int(new_name1.count("o") + new_name2.count("o"))
check_v = int(new_name1.count("v") + new_name2.count("v"))
check_e1 = int(new_name1.count("e") + new_name2.count("e"))

total2 = check_l + check_o + check_v + check_e1

love_score = int(str(total1) + str(total2))
print(love_score)