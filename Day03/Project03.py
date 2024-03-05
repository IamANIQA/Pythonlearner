print ("Welcome to Treasure Island.")
print ("Your mission is to find the treasure.")
print ("You're at a cross road.")

want_togo = input('Where do you want to go? Type "Left" or "Right". ')
if want_togo == "Left":
  swim_wait = input('''You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.''')
  if swim_wait == "wait":
    which_door = input('''You arrive at the island unharmed. There is a house with three doors. One is red,one is yellow and one is blue. Which color do you choose? ''')
    if which_door == "red":
      print("You are burned by fire.Game over.")
    elif which_door == "yellow":
      print("You win! You found the treasure.")
    elif which_door == "blue":
      print("You are eaten by beasts.Game over")
    else:
      print("Game over.")

  else:
      print("You are attacked by trout.Game over.")
else:
    print("You fall into a hole.Game over.")