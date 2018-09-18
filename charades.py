import os
import time
from PIL import Image


def replay():
  """
  Asks the user if they would want to try the game again.
  """

  choice = input("\nDo you want to play again?[y/n] ")
  if choice[0] == 'y':
    time.sleep(3)
    os.system('clear') 
    gameplay()
  elif choice[0] == 'n':
    print("\nThanks for playing. Good bye.")
  else:
    print("\nI think you may have had a stroke, please try again.")
    replay()


def gameplay():
  """
  Runs the game until either the user wins or they lose
  """

  # charade items
  items = {
    "alien": {
      "hint 1": "space",
      "hint 2": "rib cage",
      "hint 3": "ripley"
    },
    "the little mermaid": {
      "hint 1": "underwater",
      "hint 2": "trident",
      "hint 3": "prince"
    },
    "iron man": {
      "hint 1": "tower",
      "hint 2": "rich",
      "hint 3": "friday"
    },
    "x-men": {
      "hint 1": "wheelchair",
      "hint 2": "shapeshiifter",
      "hint 3": "claws"
    },
    "blade": {
      "hint 1": "sword",
      "hint 2": "whistler",
      "hint 3": "daywalker"
    },
    "jaws": {
      "hint 1": "water",
      "hint 2": "bigger boat",
      "hint 3": "great white"
    }
  }

  playing = True
  points = 0
  tries = 0


  #game play
  while playing:
    for item in items:
      for hint, value in items[item].items():
        print(f"\n{hint} : {value}")

        answer = input("\nCan you name the movie? ")
        if answer.lower() == item:
          print("\nGood job. You are correct.")
          points += 5
          break
        else:
          print("\nIncorrect. You'll receive the next hint")
          tries += 1

      if tries == 3:
        print(f"\nYou racked up {points} points.")
        print("\nUnfortunately, you're out of the game. Sorry.")
        Image.open('images/fail.jpg').show()
        time.sleep(3)
        playing = False
        break
      else:
        tries = 0
    
    #ends game play
    playing = False


  #clear screen
  os.system('clear')
  if points == 30:
    print(f"\nYou racked up {points} points.")
    Image.open('images/congrats.jpg').show()
    time.sleep(3)

  replay()



# game greeting
print("Welcome to my charade game!!!!!\n")
print("There are currently 6 items that you need to guess. They all belong to the movies category and have 3 hints that will be displayed.")
print("If you guess correctly, you will gain 5 points. So try to rack up as much points as you can and win the game to get a surpised.")
print("If you fail to answer, you will lose. So be sure to think before you answer.\n")

time.sleep(5)
os.system('clear')
gameplay()