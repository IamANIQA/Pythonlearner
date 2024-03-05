rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  

game = [rock, paper, scissors]
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(game[choose])
import random
random_choose = random.randint(0,2)
print("Computer chose: ")
print(game[random_choose])

if choose == random_choose: 
  print("It is a draw!")
elif choose == 0 and random_choose == 1:
  print("You lose.")
elif choose == 0 and random_choose == 2:
  print("You win.")
elif choose == 1 and random_choose == 0:
  print("You win")
elif choose == 1 and random_choose == 2:
  print("You lose.")
elif choose == 2 and random_choose == 0:
  print("You lose.")
elif choose == 2 and random_choose == 1:
  print("You win.")
elif choose >= 3 and random_choose >= 3:
  print("Try to play the game again!!!")
