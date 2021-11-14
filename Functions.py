from random import randint
from colorama import Fore
import time

def chapter_1_attack(player_attack, monster_advantage):
  RED = '\033[38;5;196m'
  player_roll = randint(1,20)
  monster_roll = randint(1,20) + monster_advantage
  print('you rolled a ' + str(player_roll))
  
  if player_roll > monster_roll:
    print(Fore.GREEN + 'You hit\n' + Fore.WHITE)
    time.sleep(1.5)
    print('Time to roll damage\n')
    time.sleep(1.5)
    hit_roll = randint(1,6)
    print('You rolled a ' + str(hit_roll))
    print('Now we add your attack to your roll\n')
    time.sleep(1.5)
    damage = hit_roll + player_attack
    print(Fore.GREEN + 'You did ' + str(damage) + ' damage!\n' + Fore.WHITE)
    time.sleep(1.5)
    return damage
  print(RED + 'You miss\n' + Fore.WHITE)
  time.sleep(1.5)
  damage = 0
  return damage

def run(monster_advantage):
  RED = '\033[38;5;196m'
  print('You try to run\n')
  time.sleep(1.5)
  player_roll = randint(1, 20)
  monster_roll = randint(1, 20)
  
  if player_roll > monster_roll:
    print(Fore.GREEN + 'You manage to get away\n' + Fore.WHITE)
    time.sleep(1.5)
    return 1
  print(RED + 'You don\'t get away\n' + Fore.WHITE)
  time.sleep(1.5)
  return 0

def monster_attack(mon_attack,monster_advantage, armor_class, name_of_monster):
  RED = '\033[38;5;196m'
  attack = randint(1,20) + monster_advantage
  
  if attack > armor_class:
    print(RED + "They hit you.\n" + Fore.WHITE)
    time.sleep(1.5)
    print(RED + 'The ' + name_of_monster +' does ' + str(mon_attack) + ' damage to you.\n' + Fore.WHITE)
    time.sleep(1.5)
    return mon_attack
  print(Fore.GREEN + 'The ' + name_of_monster + ' misses\n' + Fore.WHITE)
  time.sleep(1.5)
  return 0

def at_least_18(age):
  RED = '\033[38;5;196m'
  
  if age >= 18:
    print("Welcome to the game")

  elif age < 18:
    while age < 18:
      print(RED + "Sorry you are too young to play" + Fore.WHITE)
      print("The following game is rated M for Muture. You must be at least 18 to play.")
      age = int(input("Please enter your age:"))
      time.sleep(1)
    print("I could have sworn you were younger. Whatever. WELCOME TO THE GAME")
  time.sleep(1)
  return

def tutorial(answer):
  if answer == 'b':
      return

  elif answer == 'a':
    print("Through out the game I, the computer, will narrarate, and ask you multiple choice questions with a, b, c, and d answers\n")
    print('do you understand?')
    understanding = input("a. yes" " b. no " )

    if understanding == 'a':
      return

    elif understanding == 'b':
      while understanding == 'b':
        print('Ummmm...')
        time.sleep(1)
        print("I didn't expect you to say that. Let me repeat myself.\n")
        time.sleep(1)
        print("Through out the game I, the computer, will narrarate, and ask you multiple choice questions with a, b, c, and d answers\n")
        print('do you understand?\n')
        time.sleep(3)
        understanding = input("a. yes" " b. no " )

def full_battle(health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name):
  print("TIME FOR BATTLE\n")
  running = 0
  while health > 0 and monster_health> 0 and running == 0:
    
    if health_potion > 0:
      battle = input('a. Attack \nb. Run \nc. drink a health potion \n')
    
    if health_potion == 0:
      battle = input('a. Attack \nb. Run \n')

    if battle == 'a':
      damage = chapter_1_attack(attack, monster_advantage)
      monster_health -= damage

    if battle == 'b':
      running += run(monster_advantage)

    if battle == 'c' and health_potion > 0:
      print(Fore.GREEN + 'You drink a health potion and gain 10 health' + Fore.WHITE)
      health += 10
      health_potion -= 1
      
    if monster_health > 0 and running == 0:
      print('OPPONENT\'S TURN')
      opponent_attack = monster_attack(mon_attack, monster_advantage, armor_class, monster_name)
      health = health - opponent_attack
    print('You have ' + str(health) + ' health\n')
  return [health, running, monster_health, health_potion]

def guard_fight(class_choice, name, health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name):
  RED = '\033[38;5;196m'
  print(class_choice + " is a great choice.\n NOW WE BEGIN\n CHAPTER 1 \nYou are a traveling adventure hired by the church to defeat the 4 horsemen of the apocalypse. The 4 horsemen have taken over Python World, and the church has deemed them in need of disposing. \nYou walk up to a large stone wall with 2 wooden doors in the middle. You can't see through to the other side. A man wearing a suit of armor comes up to you\n")
  time.sleep(3)
  print(Fore.GREEN + "Guard: You must be the legendary " + Fore.WHITE + name + Fore.GREEN + ". I've heard so much about you. The horsemen of conquest has taken over the town behind this wall. I can open the doors for you but it is very dangerous.\n" + Fore.WHITE)
  time.sleep(3)

  choice = input("\na. Let the guard open the door \nb. attack guard \n")

  if choice == 'a':
    print('The guard opens the wooden doors.\n')
    time.sleep(1)
    print('Good luck '+ Fore.GREEN + name + Fore.WHITE + "!\n")
    time.sleep(1)

  if choice == 'b':
    print(Fore.GREEN + 'What....\n')
    time.sleep(2)
    print(RED + 'Why are you doing this?' + Fore.WHITE)
    time.sleep(1.5)
    game_data = full_battle(health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name)
    health = game_data[0]
    health_potion = game_data[3]
    
    if game_data[2] <= 0:
      print(Fore.GREEN + 'You kill the guard\n' + Fore.WHITE)
      time.sleep(1)
      print('You check the guards dead body. You find a key to the door and a ' + Fore.GREEN + 'health potion\n' + Fore.WHITE)
      time.sleep(2)
      health_potion += 1
  
    if game_data[1] == 1:
      print('You run away from the guard and manage to climb the wall. While climbing down to the other side, you slip and fall. You must roll a 20 sided die to see if you take damage from the fall\n')
      time.sleep(2.5)
      save_roll = randint(1, 20)
      print('You rolled a ' + str(save_roll))
      time.sleep(3)

      if save_roll < 11:
        print(RED + 'You sprain your ankle\n' + Fore.WHITE)
        health -= 5
        print('You have ' + str(health) + ' health\n')
        time.sleep(1)
      
      else:
        print(Fore.GREEN + 'You don\'t take damage\n' + Fore.WHITE)
        time.sleep(1)
  return [health, health_potion]

def choosing_class(name):
  print('Great! Now we can begin ' + Fore.GREEN + name + Fore.WHITE + '.\n')
  time.sleep(1)
  print('First you must choose your class\n \nFirst you have the knight. You are a noble swordman who\'s trained their whole life. A good all around class. Moderate health, attack, and armor class\n \nNext there\'s the nomad. You\'ve spent your whole life living in the wild, never in a city, always traveling and exploring the wonders of the world. low health, moderate attack, and high armor class\n \nThen you have the druid. You\'ve lived in a temple your whole life, helping and serving the people of your land. High Health, low attack, and moderate armor class \n \nThen there is the brawler. Your answer to everything is your fist. Moderate health, high attack, low armor  class\n \nLastly, there\'s the Beserker class. You\'re an absolute maniac, and don\'t care about your own well being. High health and attack, very low armor class\n')

  class_choice = input("What class will you choose? \na. Knight \nb. nomad \nc. druid \nd. brawler \ne. berzerker \n")

  if class_choice == 'a':
    return ['knight', 30, 5, 11]

  elif class_choice == "b":
    return ['nomad', 20, 5, 13]

  elif class_choice == "c":
    return ['druid', 40, 3, 11]

  elif class_choice == "d":
    return ['brawler', 30, 7, 9]

  elif class_choice == "e":
    return ['berzerker', 40, 7, 5]
