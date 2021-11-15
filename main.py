import time
from Functions import chapter_1_attack, run, monster_attack, at_least_18, tutorial, full_battle, choosing_class, guard_fight
from random import randint
from colorama import Fore

def main():
  RED = '\033[38;5;196m'
  replay = 0

  while replay == 0:
    health_potion = 0
    monster = {'monster': 
    ['health', 'attack', 'advantage'],
    'guard': [16, 10, 0], 'fungus_monster':[20, 5, 0], 'witch':[20,50, -1], 'horseman_phase1' : [25, 5, 2], 'horseman_phase2': [50, 10, 4]}

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
      print("TIME FOR BATTLE\n")
      time.sleep(1)
      running = 0
      while health > 0 and monster['fungus_monster'][0] > 0 and running == 0:
        if health_potion > 0:
          battle = input('a. Attack \nb. Run \nc. drink a health potion \n')
        if health_potion == 0:
          battle = input('a. Attack \nb. Run \n')

        if battle == 'a':
          damage = chapter_1_attack(attack, monster['fungus_monster'][2])
          monster['fungus_monster'][0] = monster['fungus_monster'][0] - damage

        if battle == 'b':
          running += run(monster['fungus_monster'][2])

        if battle == 'c' and health_potion > 0:
          print(Fore.GREEN + 'You drink a health potion and gain 10 health' + Fore.WHITE)
          health += 10
          health_potion -= 1
          
        if monster['fungus_monster'][0] > 0 and running == 0:
          print('OPPONENT\'S TURN')
          opponent_attack = monster_attack(monster['fungus_monster'][1], monster['fungus_monster'][2], armor_class, 'fungus monster')
          health = health - opponent_attack
        print('You have ' + str(health) + ' health\n')
      
      if monster['fungus_monster'][0] <= 0:
        print('You kill the monster.\n')
        time.sleep(2)
        print('You find 2 health potions\n')
        health_potion += 2
        time.sleep(2)
      
      if running == 1:
        print('You run as fast as you can from the monster\n')
        time.sleep(2)
      
      if health > 0:
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
          
          if choice == 'c':
            print(Fore.YELLOW + 'Wicth: Oh? You want to fight?\n' + Fore.WHITE)
            print("TIME FOR BATTLE\n")
            running = 0
            while health > 0 and monster['witch'][0] > 0 and running == 0:
              
              if health_potion > 0:
                battle = input('a. Attack \nb. Run \nc. drink a health potion \n')
              
              if health_potion == 0:
                battle = input('a. Attack \nb. Run \n')

              if battle == 'a':
                damage = chapter_1_attack(attack, monster['witch'][2])
                monster['witch'][0] = monster['witch'][0] - damage

              if battle == 'b':
                running += run(monster['witch'][2])

              if battle == 'c' and health_potion > 0:
                print(Fore.GREEN + 'You drink a health potion and gain 10 health' + Fore.WHITE)
                health += 10
                health_potion -= 1
                
              if monster['witch'][0] > 0 and running == 0:
                print('OPPONENT\'S TURN')
                opponent_attack = monster_attack(monster['witch'][1], monster['witch'][2], armor_class, 'witch')
                health = health - opponent_attack
              print('You have ' + str(health) + ' health\n')
            
            if monster['witch'][0] <= 0:
              print(Fore.GREEN + 'You wound the witch. She lets out a violent screams. She disappears leaving only her clothes. You pick up her robe and put it on over your armor. Your armor class is increased by 5.\n' + Fore.WHITE)
              time.sleep(5)
            
            if running == 1:
              print('You manage to run away from the wicth as she screams out to you.\n')
              time.sleep(2)
              print(Fore.YELLOW + 'Witch: I\'LL GET YOU ONE DAY\n' + Fore.WHITE)
              time.sleep(2)
            
        if health > 0:
          print(Fore.GREEN + 'Attack Increased by 3\n' + Fore.WHITE)
          attack += 3
          health += 10
          print('You finally arrive at the castle. You walk in and the walls are covered in fungus. In the center of a room a man sits in a tall chair with a bird mask on\n')
          time.sleep(5)
          print(Fore.BLUE + 'Horseman: You might wanna put on a mask. Don\'t want to breathe in the spores. I am the horsman of conquest. Now we shall fight to the death\n' + Fore.WHITE)
          time.sleep(5)
          print("TIME FOR BATTLE")
          time.sleep(1)
          running = 0
          while health > 0 and monster['horseman_phase1'][0] > 0:
              
            if health_potion > 0:
                battle = input('a. Attack \nb. drink a health potion \n')
              
            if health_potion == 0:
                battle = input('a. Attack \n')

            if battle == 'a':
              damage = chapter_1_attack(attack, monster['horseman_phase1'][2])
              monster['horseman_phase1'][0] = monster['horseman_phase1'][0] - damage

            if battle == 'b':
              print(Fore.GREEN + 'You drink a health potion and gain 10 health' + Fore.WHITE)
              health += 10
              health_potion -= 1
                
            if monster['horseman_phase1'][0] > 0:
              print('OPPONENT\'S TURN')
              opponent_attack = monster_attack(monster['horseman_phase1'][1], monster['horseman_phase1'][2], armor_class, 'horseman')
              health = health - opponent_attack
            print('You have ' + str(health) + ' health\n')
          if monster['horseman_phase1'][0] <= 0 and health > 0:
            print('The horseman screams in pain\n')
            time.sleep(1)
            print(Fore.BLUE + 'Horseman: You\'re stronger than I thought\n')
            time.sleep(2)
            print(RED + 'Wings covered in black feather come out of the horseman\'s back. It is clear he\'s not done yet\n' + Fore.WHITE)
            time.sleep(3)
            print("TIME FOR BATTLE")
            time.sleep(1)
            health += 20
            while health > 0 and monster['horseman_phase2'][0] > 0:
                
              if health_potion > 0:
                  battle = input('a. Attack \nb. drink a health potion \n')
                
              if health_potion == 0:
                  battle = input('a. Attack \n')

              if battle == 'a':
                damage = chapter_1_attack(attack, monster['horseman_phase2'][2])
                monster['horseman_phase2'][0] = monster['horseman_phase2'][0] - damage

              if battle == 'b':
                print(Fore.GREEN + 'You drink a health potion and gain 10 health' + Fore.WHITE)
                health += 10
                health_potion -= 1
                  
              if monster['horseman_phase2'][0] > 0:
                print('OPPONENT\'S TURN')
                opponent_attack = monster_attack(monster['horseman_phase2'][1], monster['horseman_phase2'][2], armor_class, 'horseman')
                health = health - opponent_attack
              print('You have ' + str(health) + ' health\n')

            if monster['horseman_phase2'][0] <= 0:
              print('YOU DID IT. You slay the horseman. 1 down and 3 to go, but those are stories for another day.\n')
              time.sleep(3)
              print("TO BE CONTINUED\n")
              time.sleep(5)
              print('Thank you ' + name + ' for playing my game. I hope you had fun and enjoyed your journey\n')
              time.sleep(4)

    if health <= 0:
      print(RED + "You lose\n")

    play_again = input(Fore.WHITE + 'Would you like to play again?\n a. yes\n b. no\n')
    if play_again == "b":
      replay = 1

if __name__ == "__main__":
    main()