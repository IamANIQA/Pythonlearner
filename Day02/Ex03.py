age = input("What is your current age? ")
new_age = int(age)

days = 365
weeks = 52
months = 12

total_age = 90
age_left = total_age - new_age

new_days = new_age * days
new_weeks = new_age * weeks
new_months = new_age * months

print(
    f"You have {new_days} days , {new_weeks} weeks and {new_months} months left."
)
