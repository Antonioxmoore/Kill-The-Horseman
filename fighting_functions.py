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

def fungus_monster_fight(health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name):
  RED = '\033[38;5;196m'
  print(Fore.GREEN + 'Attack Increased by 1\n' + Fore.WHITE)
  attack +=1
  print('On the other side of the wall, you find a village in ruins. Buildings are crumbled and vegetation is overgrown. Mushrooms and fungus also seem to be growing around the village. There is one path in the village leading to a castle (That must be where the horseman is)\n')
  time.sleep(5)
  print('You walk along the path and come across a ' + RED + 'tall man covered in fungus and mushrooms.\n')
  time.sleep(2)
  print('fungus monster: uggrhh ugrrhhhh\n' + Fore.WHITE)
  time.sleep(1.5)
  print('You seem to not be able to understand the monster. The fungus monster attacks\n')
  time.sleep(1)

  game_data = full_battle(health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name)
  health = game_data[0]
  health_potion = game_data[3]
  
  if game_data[2] <= 0:
    print('You kill the monster.\n')
    time.sleep(2)
    print('You find 2 health potions\n')
    health_potion += 2
    time.sleep(2)

  if game_data[1] == 1:
    print('You run as fast as you can from the monster\n')
    time.sleep(2)
  return [health, health_potion]

def drink_potion(choice, health, attack):
  RED = '\033[38;5;196m'
  if choice == 'a':
    print('she hands you a potion.\n')
    print('witch: drink this.\n')
    drink = input('Do you drink it? \na. yes \nb. no \n')
    if drink == 'a':
      print(Fore.RED + "you drink the strange liquid\n" + Fore.WHITE)
      save_roll = randint(1, 20)
      time.sleep(5)
      
      if save_roll > 12:
        print(Fore.GREEN + 'You feel light. Almost like you can fly. You gain 15 health\n' + Fore.WHITE)
        time.sleep(1)
      
      if save_roll < 12:
        print(Fore.RED + 'You feel light. You start to wobble until you fall to the ground.\n')
        print(RED + 'YOU DIE\n')
        health = 0
        time.sleep(1)
    if drink == 'b':
      print(Fore.RED + 'The witch looks disappointed, but lets you leave\n' + Fore.WHITE)
      time.sleep(1)
  if choice == 'b':
    print(Fore.YELLOW + 'Witch: Ah you choose' + RED + ' strength' + Fore.YELLOW + '. Here drink this.' + Fore.WHITE)
    time.sleep(1)
    print('She hands you a ' + RED + 'red' + Fore.WHITE + ' potion.')
    drink = input('Do you drink it? \na. yes \nb no\n')
    if drink == 'a':
      print(Fore.RED + 'You drink the foul tasting potion.\n')
      save_roll = randint(1, 20)
      time.sleep(5)
      if save_roll > 14:
        print(Fore.GREEN + 'After drinking it you instantly feel stronger. You gain 5 attack.\n' + Fore.WHITE)
        attack += 5
        time.sleep(2)
      
      if save_roll < 15:
        print(Fore.GREEN + 'After drinking it you instantly feel stronger, ')
        time.sleep(2)
        print(Fore.RED + 'but...\n')
        time.sleep(3)
        "The witch begins to laugh as you start to fall to the ground.\n"
        time.sleep(2)
        print(RED + 'YOU DIE\n')
        health = 0
    if drink == 'b':
      print('The witch looks disappointed, but lets you leave\n')
      time.sleep(1)
  return [health, attack]

def witch_fight(name, health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name):
  RED = '\033[38;5;196m'
  print(Fore.GREEN + 'Attack Increased by 2' + Fore.WHITE)
  time.sleep(1)
  attack += 2
  print('You continue down the path and see an old lady in robes sitting in the middle of the path.\n')
  time.sleep(2)
  talk_to_witch = input('Do you talk to her? \na. yes \nb. no \n')
  if talk_to_witch == 'a':
    print(Fore.YELLOW + 'Witch: I\'ve been waiting for you ' + Fore.GREEN + name + Fore.YELLOW + '.\n')
    time.sleep(1)
    choice = input('Do you want ' + Fore.GREEN + 'life ' + Fore.YELLOW + 'or ' + RED + 'strength' + Fore.YELLOW + '?' + Fore.WHITE + '\na. life \nb. strength \nc. attack the witch. (not recomended)\n')

    if choice == 'a' or choice == 'b':
      health_health_potion = drink_potion(choice, health, attack)
      health = health_health_potion[0]
      health_potion = health_health_potion[1]

    if choice == 'c':
      
      game_data = full_battle(health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name)
      health = game_data[0]
      health_potion = game_data[3]
      
      if game_data[2] <= 0:
        print(Fore.GREEN + 'You wound the witch. She lets out a violent screams. She disappears leaving only her clothes. You pick up her robe and put it on over your armor. Your armor class is increased by 5.\n' + Fore.WHITE)
        armor_class += 5
        time.sleep(5)

      if game_data[1] == 1:
        print('You manage to run away from the wicth as she screams out to you.\n')
        time.sleep(2)
        print(Fore.YELLOW + 'Witch: I\'LL GET YOU ONE DAY\n' + Fore.WHITE)
        time.sleep(2)
  return [health, health_potion, attack, armor_class]

def final_full_battle(health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name):
  print("TIME FOR BATTLE\n")
  while health > 0 and monster_health> 0:
    
    if health_potion > 0:
      battle = input('a. Attack \n c. drink a health potion \n')
    
    if health_potion == 0:
      battle = input('a. Attack \n')

    if battle == 'a':
      damage = chapter_1_attack(attack, monster_advantage)
      monster_health -= damage

    if battle == 'c' and health_potion > 0:
      print(Fore.GREEN + 'You drink a health potion and gain 10 health' + Fore.WHITE)
      health += 10
      health_potion -= 1
      
    if monster_health > 0:
      print('OPPONENT\'S TURN')
      opponent_attack = monster_attack(mon_attack, monster_advantage, armor_class, monster_name)
      health = health - opponent_attack
    print('You have ' + str(health) + ' health\n')
  return [health, monster_health, health_potion]

def boss_phase1_battle(health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name):
  RED = '\033[38;5;196m'
  print(Fore.GREEN + 'Attack Increased by 3\n' + Fore.WHITE)
  attack += 3
  health += 10
  print('You finally arrive at the castle. You walk in and the walls are covered in fungus. In the center of a room a man sits in a tall chair with a bird mask on\n')
  time.sleep(5)
  print(Fore.BLUE + 'Horseman: You might wanna put on a mask. Don\'t want to breathe in the spores. I am the horsman of conquest. Now we shall fight to the death\n' + Fore.WHITE)
  time.sleep(5)

  game_data = final_full_battle(health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name)
  health = game_data[0]
  health_potion = game_data[2]
    
  if game_data[1] <= 0:
    print('The horseman screams in pain\n')
    time.sleep(1)
    print(Fore.BLUE + 'Horseman: You\'re stronger than I thought\n')
    time.sleep(2)
    print(RED + 'Wings covered in black feather come out of the horseman\'s back. It is clear he\'s not done yet\n' + Fore.WHITE)
    time.sleep(3)
    print("TIME FOR BATTLE")
    time.sleep(1)
    health += 20
  return [health, health_potion]

def boss_phase2_battle(name, health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name):
  game_data = final_full_battle(health, monster_health, health_potion, attack, monster_advantage, mon_attack, armor_class, monster_name)
  health = game_data[0]
  health_potion = game_data[2]
    
  if game_data[1] <= 0:
    print('YOU DID IT. You slay the horseman. 1 down and 3 to go, but those are stories for another day.\n')
    time.sleep(3)
    print("TO BE CONTINUED\n")
    time.sleep(5)
    print('Thank you ' + name + ' for playing my game. I hope you had fun and enjoyed your journey\n')
    time.sleep(4)
  return health