import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pypassword = print("Here is your password:",end="")
# for l in range(0,nr_letters):
#   l = random.choice(letters)
#   print(l)
# for s in range(0,nr_symbols):
#   s = random.choice(symbols)
#   print(s)
# for n in range(0,nr_numbers):
#   n = random.choice(numbers)
#   print(n)  
for p in range(0,nr_letters+nr_symbols+nr_numbers):
  p = random.choice(letters+symbols+numbers)
  print(p, end="")
