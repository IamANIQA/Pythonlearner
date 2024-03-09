# Challenge 02 : Replacing Blanks with Guess
word_list = ["avdvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

print(f'Pssst,the solution is {chosen_word}.')
# count_chosen_word = len(chosen_word)
# for d in range(0,count_chosen_word):
#   print("_",end="")
# print("\n")

guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        print(guess, end="")
    else:
        print("_", end="")
