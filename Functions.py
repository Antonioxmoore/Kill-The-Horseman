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
