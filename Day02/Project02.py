print ("Welcome to the tip calculator")

total_bill = input("What was the total bill? ")
new_bill = int(total_bill)

percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15 ?")
tip = int(percentage_tip)
new_tip = float ((tip / 100 ) + 1)

split_bill = input("How many people to split the bill? ")
new_split_bill = int(split_bill)

each_pay = float((new_bill * new_tip) / new_split_bill )

each_person_pay = round(each_pay)

print(f"Each person should pay: {each_person_pay}")