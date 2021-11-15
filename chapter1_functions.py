from colorama import Fore
import time

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