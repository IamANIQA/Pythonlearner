# Challenge 01 : Picking a Random Words and Checking Answers
word_list = ["avdvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

# chosen =chosen_word.split(" , ")

user_guess = input("Guess a letter:")
guess = user_guess.lower()
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
