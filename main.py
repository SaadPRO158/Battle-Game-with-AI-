#!/bin/python3
import random, time
from player import *
from special import *
from helper import *

print("Welcome to the battle game.")
print("")
time.sleep(1)
while True:
  print("Do you want to be the hero or the villain? (Type 'h' for hero and 'v' for villain.)")
  mode = input(">")

  if mode != 'h' and mode != 'v':
    while True:
      print("Invalid input.")
      mode = input(">")
      print("")
      
      if mode == 'h' or mode == 'v':
        break

  heroes = ['Spiderman', 'Pikachu', 'Hercules', 'Jedi']
  villains = ['Voldemort', 'Thanos', 'Medusa']
  if mode == 'h':
    print("The computer will be the villain, and you will be the hero.")
    userchars = heroes
    botchars = villains
  else:
    print("The computer will be the hero, and you will be the villain.")
    userchars = villains
    botchars = heroes

  print("")
  time.sleep(1)
  print("Do you want to choose your character or do you want it to be random? (Type 'c' for choose and 'r' for random.)")
  answer = input(">")
  print("")


    
  if answer != 'c' and answer != 'r':
    while True:
      print("Invalid input.")
      answer = input(">")
      print("")
      
      if answer == 'c' or answer == 'r':
        break

  if answer == 'c':
    print("Choose one of the following characters to fight against the enemy!")
    print("")
    
    time.sleep(1)
    for i in userchars:
      print(i)
    player = input(">")
    print("")
      
    if player not in userchars:
      while True:
        print("Please enter one of the characters mentioned above.")
        player = input(">")
        print("")
        
        if player in userchars:
          break

  elif answer == 'r':
    player = random.choice(userchars)
    print("Your character is...")
    time.sleep(1)
    print(player + "!")
    print("")
    time.sleep(1)
    

  villain = random.choice(botchars)

  if player == "Spiderman":
    user = Spiderman()
        
  elif player == "Pikachu":
    user = Pikachu()
      
  elif player == "Hercules":
    user = Hercules()
      
  elif player == "Jedi":
    user = Jedi()

  elif player == "Voldemort":
    user = Voldemort()

  elif player == 'Thanos':
    user = Thanos()

  elif player == "Medusa":
    user = Medusa()

  if villain == "Spiderman":
    bot = Spiderman()
        
  elif villain == "Pikachu":
    bot = Pikachu()
      
  elif villain == "Hercules":
    bot = Hercules()
      
  elif villain == "Jedi":
    bot = Jedi()

  if villain == 'Voldemort':
    bot = Voldemort()

  elif villain == 'Thanos':
    bot = Thanos()
    
  elif villain == "Medusa":
    bot = Medusa()
    

  print("The enemy {} will be fighting against is...".format(player))
  time.sleep(1)
  print("{}!".format(villain))

  time.sleep(1)
  get_status(user, bot)
  time.sleep(1)

  while True:
    user_move(user, bot)
    time.sleep(1)
    
    if user.health <= 0:
      print("{} has no more health...".format(player))
      time.sleep(1)
      print("Computer wins!")
      break

    elif bot.health <= 0:
      print("{} has no more health...".format(villain))
      time.sleep(1)
      print("You win!")
      break
    
    bot_move(user, bot)
    time.sleep(1)
    
    if user.health <= 0:
      print("{} has no more health...".format(player))
      time.sleep(1)
      print("Computer wins!")
      break

    elif bot.health <= 0:
      print("{} has no more health...".format(villain))
      time.sleep(1)
      print("You win!")
      break
  
  time.sleep(1)
  print("__________________________________________")
  time.sleep(1)
  print("Want to play another round? y/n")
  time.sleep(1)
  new_round = input(">")

  while new_round != 'y' and new_round != 'yes' and new_round != 'n' and new_round != 'no':
    print("")
    print("Invalid input.")
    time.sleep(1)
    new_round = input(">")
  
  if new_round == 'y' or new_round == 'yes':
    print("")
  
  elif new_round == 'n' or new_round == 'no':
    print("")
    print("Okay then.")
    break