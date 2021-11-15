from chapter1_functions import at_least_18, tutorial, choosing_class
from fighting_functions import guard_fight, fungus_monster_fight, witch_fight, boss_phase1_battle, boss_phase2_battle
from colorama import Fore

def main():
  RED = '\033[38;5;196m'
  replay = 0
  while replay == 0:
    health_potion = 0
    monster = {'monster': 
    ['health', 'attack', 'advantage'],
    'guard': [16, 10, 0], 'fungus_monster':[20, 5, 0], 'witch':[20,50, -1], 'horseman_phase1' : [25, 5, 1], 'horseman_phase2': [50, 10, 2]}
    print(Fore.WHITE + "The following game is rated M for Mature. You must be at least 18 to play.")
    at_least_18(int(input("Please enter your age: ")))
    name = input("What is your name? ")
    print("Hello " + Fore.GREEN + name + Fore.WHITE + '!!' )
    
    tutorial(input("Before we begin would you like a tutorial? (answer: a. yes b. no) "))
    class_choice = choosing_class(name)
    health = class_choice[1]
    attack = class_choice[2]
    armor_class = class_choice[3]
    
    health_after_fight = guard_fight(class_choice[0], name, health, monster['guard'][0], health_potion, attack, monster['guard'][2], monster['guard'][1], armor_class, 'guard')
    health = health_after_fight[0]
    health_potion = health_after_fight[1]

    if health > 0:
      health_after_fight = fungus_monster_fight(health, monster['fungus_monster'][0], health_potion, attack, monster['fungus_monster'][2], monster['fungus_monster'][1], armor_class, 'fungus monster')
      health = health_after_fight[0]
      health_potion = health_after_fight[1]
      print(health)
      if health > 0:
        health_after_fight = witch_fight(name,health, monster['witch'][0], health_potion, attack, monster['witch'][2], monster['witch'][1], armor_class, 'witch')
        health = health_after_fight[0]
        health_potion = health_after_fight[1]
        attack = health_after_fight[2]
        armor_class = health_after_fight[3]
        print(health)

        if health > 0:
          health_after_fight = boss_phase1_battle(health, monster['horseman_phase1'][0], health_potion, attack, monster['horseman_phase1'][2], monster['horseman_phase1'][1], armor_class, 'horseman')
          health = health_after_fight[0]
          health_potion = health_after_fight[1]
          
          if health > 0:
            health = boss_phase2_battle(name, health, monster['horseman_phase2'][0], health_potion, attack, monster['horseman_phase2'][2], monster['horseman_phase2'][1], armor_class, 'horseman')

    if health <= 0:
      print(RED + "You lose\n")

    play_again = input(Fore.WHITE + 'Would you like to play again?\n a. yes\n b. no\n')
    if play_again == "b":
      replay = 1

if __name__ == "__main__":
    main()